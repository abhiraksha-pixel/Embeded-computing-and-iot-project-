import json
import os
from datetime import datetime

import joblib
import pandas as pd
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "edge_ai_ids/abhi_esp32_iot_data"

MODEL_FILE = "intrusion_model.pkl"

TRAFFIC_LOG_FILE = "logs/traffic_log.csv"
INTRUSION_LOG_FILE = "logs/intrusion_log.csv"

model = joblib.load(MODEL_FILE)

print("Random Forest model loaded")
print("Expected features:")
print(list(model.feature_names_in_))
print("--------------------------------")

os.makedirs("logs", exist_ok=True)


def convert_iot_data_to_features(data):

    meter = int(data.get("meter", 0))
    motion = int(data.get("motion", 0))

    if meter > 3000 or motion == 1:
        packet_size = 1200
        packets_per_second = 300
        connections = 50
        duration = 3
    else:
        packet_size = 200
        packets_per_second = 5
        connections = 2
        duration = 15

    features = {
        "packet_size": packet_size,
        "packets_per_second": packets_per_second,
        "connections": connections,
        "duration": duration,

        "device_Smart_Camera_01": 0,
        "device_Smart_Light_01": 0,
        "device_Smart_Lock_01": 0,
        "device_Smart_Meter_01": 0,
        "device_Smart_Thermostat_01": 1,

        "protocol_MQTT": 1,
        "protocol_TCP": 0,
        "protocol_UDP": 0
    }

    return features


def write_traffic_log(data, status, confidence, features):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    record = {
        "timestamp": timestamp,
        "device": data.get("device", "Unknown"),
        "packet_size": features["packet_size"],
        "packets_per_second": features["packets_per_second"],
        "connections": features["connections"],
        "duration": features["duration"],
        "protocol": "MQTT",
        "confidence": round(confidence, 2),
        "status": status
    }

    df = pd.DataFrame([record])

    if os.path.exists(TRAFFIC_LOG_FILE):
        df.to_csv(
            TRAFFIC_LOG_FILE,
            mode="a",
            header=False,
            index=False
        )
    else:
        df.to_csv(
            TRAFFIC_LOG_FILE,
            mode="w",
            header=True,
            index=False
        )


def write_intrusion_log(data, confidence, features):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    record = {
        "timestamp": timestamp,
        "device": data.get("device", "Unknown"),
        "packet_size": features["packet_size"],
        "packets_per_second": features["packets_per_second"],
        "connections": features["connections"],
        "duration": features["duration"],
        "protocol": "MQTT",
        "confidence": round(confidence, 2),
        "status": "ATTACK"
    }

    df = pd.DataFrame([record])

    if os.path.exists(INTRUSION_LOG_FILE):
        df.to_csv(
            INTRUSION_LOG_FILE,
            mode="a",
            header=False,
            index=False
        )
    else:
        df.to_csv(
            INTRUSION_LOG_FILE,
            mode="w",
            header=True,
            index=False
        )


def on_connect(client, userdata, flags, reason_code, properties):

    print("Connected to MQTT broker")
    print("Connection result:", reason_code)

    client.subscribe(TOPIC)

    print("Subscribed to:", TOPIC)
    print("--------------------------------")


def on_message(client, userdata, message):

    try:

        data = json.loads(message.payload.decode())

        print("Received Wokwi IoT data:")
        print(data)

        features = convert_iot_data_to_features(data)

        input_data = pd.DataFrame(
            [features],
            columns=model.feature_names_in_
        )

        prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]

        if prediction == 1:
            status = "ATTACK"
        else:
            status = "NORMAL"

        confidence = max(probabilities) * 100

        print("AI Analysis:")
        print("Status:", status)
        print("Confidence:", round(confidence, 2), "%")

        write_traffic_log(
            data,
            status,
            confidence,
            features
        )

        print("Traffic log updated")

        if status == "ATTACK":

            write_intrusion_log(
                data,
                confidence,
                features
            )

            print("Intrusion log updated")
            print("ALERT: Intrusion detected!")

        print("--------------------------------")

    except Exception as error:

        print("Error processing MQTT data:")
        print(error)
        print("--------------------------------")


client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)

client.on_connect = on_connect
client.on_message = on_message

print("Starting Edge-AI MQTT Gateway...")
print("Connecting to MQTT broker...")

client.connect(
    BROKER,
    PORT,
    60
)

client.loop_forever()
