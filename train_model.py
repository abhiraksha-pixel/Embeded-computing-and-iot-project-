import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# Load the processed dataset
data = pd.read_csv("dataset/processed_iot_traffic.csv")


print("=" * 60)
print("             IoT INTRUSION DETECTION")
print("                 MODEL TRAINING")
print("=" * 60)


# Separate features and target
X = data.drop("status", axis=1)
y = data["status"]


print("\nFeatures used for training:")
print(list(X.columns))


print("\nTarget:")
print("0 = NORMAL")
print("1 = ATTACK")


# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


print("\nDataset split:")
print(f"Training records : {len(X_train)}")
print(f"Testing records  : {len(X_test)}")


# Create the Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


print("\nTraining Random Forest model...")

# Train the model
model.fit(X_train, y_train)


print("Training completed!")


# Make predictions on test data
y_pred = model.predict(X_test)


# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(f"{accuracy * 100:.2f}%")


# Display detailed performance
print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=["NORMAL", "ATTACK"]
))


# Save the trained model
joblib.dump(model, "intrusion_model.pkl")

print("\nModel saved successfully:")
print("intrusion_model.pkl")