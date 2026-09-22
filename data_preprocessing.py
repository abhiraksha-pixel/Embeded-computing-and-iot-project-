import pandas as pd


# Load the dataset
data = pd.read_csv("dataset/iot_traffic.csv")

print("=" * 60)
print("          IoT DATA PREPROCESSING")
print("=" * 60)

print("\nOriginal dataset:")
print(data.head())


# Convert NORMAL and ATTACK into numbers
data["status"] = data["status"].map({
    "NORMAL": 0,
    "ATTACK": 1
})


# Convert categorical features into numerical features
data = pd.get_dummies(
    data,
    columns=["device", "protocol"],
    dtype=int
)


print("\nProcessed dataset:")
print(data.head())


print("\nProcessed columns:")
for column in data.columns:
    print(column)


print("\nDataset shape after preprocessing:")
print(f"Rows    : {data.shape[0]}")
print(f"Columns : {data.shape[1]}")


# Save the processed dataset
data.to_csv("dataset/processed_iot_traffic.csv", index=False)

print("\nProcessed dataset saved to:")
print("dataset/processed_iot_traffic.csv")