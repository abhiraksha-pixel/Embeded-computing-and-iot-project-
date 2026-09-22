import random
import time
import joblib
import pandas as pd
from datetime import datetime


# Load the trained ML model
model = joblib.load("intrusion_model.pkl")


# Virtual IoT devices
devices = [
    "Smart_Light_01",
    "Smart_Thermostat_01",
    "Smart_Camera_01",
    "Smart_Lock_01",
    "Smart_Meter_01"
]


# File where intrusion alerts will be stored
LOG_FILE = "logs/intrusion_log.csv"

# File where all analyzed traffic will be stored
TRAFFIC_LOG_FILE = "logs/traffic_log.csv"

def generate_traffic(device):
    """Generate traffic for a virtual IoT device."""

    if random.random() < 0.8:

        packet_size = random.randint(100, 500)
        packets_per_second = random.randint(1, 15)
        connections = random.randint(1, 3)
        protocol = random.choice(["TCP", "UDP", "MQTT"])
        duration = random.randint(5, 30)

    else:

        packet_size = random.randint(1000, 1500)
        packets_per_second = random.randint(200, 500)
        connections = random.randint(20, 100)
        protocol = random.choice(["TCP", "UDP"])
        duration = random.randint(1, 5)

    return {
        "device": device,
        "packet_size": packet_size,
        "packets_per_second": packets_per_second,
        "connections": connections,
        "protocol": protocol,
        "duration": duration
    }


def prepare_features(traffic):
    """Convert traffic into ML model input."""

    data = pd.DataFrame([traffic])

    data = pd.get_dummies(
        data,
        columns=["device", "protocol"],
        dtype=int
    )

    # Add missing columns required by the model
    for column in model.feature_names_in_:
        if column not in data.columns:
            data[column] = 0

    # Keep the same feature order used during training
    data = data[model.feature_names_in_]

    return data


def log_intrusion(device, traffic, confidence):
    """Save a detected intrusion to the CSV log."""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = {
        "timestamp": timestamp,
        "device": device,
        "packet_size": traffic["packet_size"],
        "packets_per_second": traffic["packets_per_second"],
        "connections": traffic["connections"],
        "protocol": traffic["protocol"],
        "duration": traffic["duration"],
        "confidence": round(confidence, 2),
        "status": "ATTACK"
    }

    log_data = pd.DataFrame([log_entry])

    # Append to existing log file
    log_data.to_csv(
        LOG_FILE,
        mode="a",
        header=not __import__("os").path.exists(LOG_FILE),
        index=False
    )


def log_traffic(device, traffic, confidence, prediction):
    """Save every analyzed traffic event to the CSV log."""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    status = "ATTACK" if prediction == 1 else "NORMAL"

    log_entry = {
        "timestamp": timestamp,
        "device": device,
        "packet_size": traffic["packet_size"],
        "packets_per_second": traffic["packets_per_second"],
        "connections": traffic["connections"],
        "protocol": traffic["protocol"],
        "duration": traffic["duration"],
        "confidence": round(confidence, 2),
        "status": status
    }

    log_data = pd.DataFrame([log_entry])

    log_data.to_csv(
        TRAFFIC_LOG_FILE,
        mode="a",
        header=not __import__("os").path.exists(TRAFFIC_LOG_FILE),
        index=False
    )


def display_alert(device, traffic, confidence):
    """Display an intrusion alert."""

    print("\n")
    print("!" * 70)
    print("                 ⚠ INTRUSION ALERT ⚠")
    print("!" * 70)

    print(f"Device             : {device}")
    print(f"Packet Size        : {traffic['packet_size']} bytes")
    print(f"Packets/Second     : {traffic['packets_per_second']}")
    print(f"Connections        : {traffic['connections']}")
    print(f"Protocol           : {traffic['protocol']}")
    print(f"Duration           : {traffic['duration']} seconds")
    print(f"ML Confidence      : {confidence:.2f}%")

    print("Threat Status      : SUSPICIOUS")
    print("Action             : ALERT GENERATED")
    print("Log Status         : SAVED")

    print("!" * 70)
    print()


def main():

    print("=" * 70)
    print("             EDGE-AI IoT INTRUSION DETECTION")
    print("=" * 70)

    print("\nEdge Gateway : ACTIVE")
    print("ML Model     : LOADED")
    print("Monitoring   : STARTED")
    print("Alert Log    : ENABLED")

    print("\nPress CTRL+C to stop monitoring.\n")

    total_traffic = 0
    normal_count = 0
    attack_count = 0

    try:

        while True:

            print("=" * 70)
            print("NEW MONITORING CYCLE")
            print("=" * 70)

            for device in devices:

                # Generate new traffic
                traffic = generate_traffic(device)

                # Prepare traffic for ML model
                features = prepare_features(traffic)

                # Make prediction
                prediction = model.predict(features)[0]

                # Prediction confidence
                probabilities = model.predict_proba(features)[0]
                confidence = max(probabilities) * 100
                # Save every analyzed traffic record
                log_traffic(
                  device,
                  traffic,
                  confidence,
                  prediction
                )

                total_traffic += 1

                print(f"\nDevice: {device}")
                print(f"Packet Size    : {traffic['packet_size']} bytes")
                print(f"Packets/sec    : {traffic['packets_per_second']}")
                print(f"Connections     : {traffic['connections']}")
                print(f"Protocol       : {traffic['protocol']}")

                if prediction == 0:

                    normal_count += 1

                    print("ML Prediction  : NORMAL")
                    print(f"Confidence     : {confidence:.2f}%")
                    print("Status         : ✓ SAFE")

                else:

                    attack_count += 1

                    print("ML Prediction  : ATTACK")
                    print(f"Confidence     : {confidence:.2f}%")
                    print("Status         : ⚠ INTRUSION DETECTED")

                    # Save attack to log
                    log_intrusion(
                        device,
                        traffic,
                        confidence
                    )

                    # Display alert
                    display_alert(
                        device,
                        traffic,
                        confidence
                    )

            print("\n")
            print("-" * 70)
            print("MONITORING STATISTICS")
            print("-" * 70)

            print(f"Total traffic analyzed : {total_traffic}")
            print(f"Normal traffic         : {normal_count}")
            print(f"Suspicious traffic     : {attack_count}")

            if total_traffic > 0:
                detection_rate = (attack_count / total_traffic) * 100
                print(f"Suspicious percentage   : {detection_rate:.2f}%")

            print("-" * 70)

            time.sleep(3)

    except KeyboardInterrupt:

        print("\n")
        print("=" * 70)
        print("           EDGE GATEWAY STOPPED")
        print("=" * 70)

        print(f"\nTotal traffic analyzed : {total_traffic}")
        print(f"Normal traffic         : {normal_count}")
        print(f"Suspicious traffic     : {attack_count}")

        print("\nMonitoring ended safely.")


if __name__ == "__main__":
    main()