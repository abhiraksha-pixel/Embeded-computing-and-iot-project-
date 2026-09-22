import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "edge_ai_ids/abhi_esp32_iot_data"

def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected to MQTT broker")
    print("Connection result:", reason_code)

    client.subscribe(TOPIC)

    print("Subscribed to:", TOPIC)
    print("--------------------------------")

def on_message(client, userdata, message):
    print("MQTT message received:")
    print(message.payload.decode())
    print("--------------------------------")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect
client.on_message = on_message

print("Starting MQTT test receiver...")
print("Connecting to MQTT broker...")

client.connect(BROKER, PORT, 60)

client.loop_forever()
