import random
import pandas as pd


# Virtual IoT devices
devices = [
    "Smart_Light_01",
    "Smart_Thermostat_01",
    "Smart_Camera_01",
    "Smart_Lock_01",
    "Smart_Meter_01"
]


def generate_normal_traffic(device):
    """Generate normal traffic."""

    packet_size = random.randint(100, 500)
    packets_per_second = random.randint(1, 15)
    connections = random.randint(1, 3)
    protocol = random.choice(["TCP", "UDP", "MQTT"])
    duration = random.randint(5, 30)

    return {
        "device": device,
        "packet_size": packet_size,
        "packets_per_second": packets_per_second,
        "connections": connections,
        "protocol": protocol,
        "duration": duration,
        "status": "NORMAL"
    }


def generate_attack_traffic(device):
    """Generate suspicious traffic."""

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
        "duration": duration,
        "status": "ATTACK"
    }


def generate_dataset(number_of_records=1000):
    """Generate and save the IoT traffic dataset."""

    records = []

    for _ in range(number_of_records):

        device = random.choice(devices)

        # 80% normal traffic, 20% attack traffic
        if random.random() < 0.8:
            traffic = generate_normal_traffic(device)
        else:
            traffic = generate_attack_traffic(device)

        records.append(traffic)

    # Convert the records into a Pandas DataFrame
    dataframe = pd.DataFrame(records)

    # Save dataset
    dataframe.to_csv("dataset/iot_traffic.csv", index=False)

    print("=" * 60)
    print("       IoT TRAFFIC DATASET GENERATED")
    print("=" * 60)

    print(f"\nTotal records generated: {len(dataframe)}")

    print("\nTraffic distribution:")
    print(dataframe["status"].value_counts())

    print("\nDataset saved to:")
    print("dataset/iot_traffic.csv")


if __name__ == "__main__":
    generate_dataset(1000)