from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

TRAFFIC_LOG_FILE = "logs/traffic_log.csv"
INTRUSION_LOG_FILE = "logs/intrusion_log.csv"


# ============================================================
# DATA LOADING FUNCTIONS
# ============================================================

def load_traffic_data():
    if os.path.exists(TRAFFIC_LOG_FILE):
        return pd.read_csv(TRAFFIC_LOG_FILE)

    return pd.DataFrame()


def load_intrusion_data():
    if os.path.exists(INTRUSION_LOG_FILE):
        return pd.read_csv(INTRUSION_LOG_FILE)

    return pd.DataFrame()


# ============================================================
# IoT DATA API
# ============================================================

@app.route("/api/iot-data", methods=["POST"])
def receive_iot_data():

    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "No JSON data received"
        }), 400

    print("Received IoT data:")
    print(data)

    return jsonify({
        "status": "success",
        "message": "IoT data received",
        "data": data
    })


# ============================================================
# DASHBOARD
# ============================================================

@app.route("/")
def dashboard():

    traffic_data = load_traffic_data()
    intrusion_data = load_intrusion_data()

    if traffic_data.empty:

        total_traffic = 0
        normal_traffic = 0
        total_attacks = 0
        attack_percentage = 0
        device_attacks = {}

    else:

        total_traffic = len(traffic_data)

        normal_traffic = len(
            traffic_data[
                traffic_data["status"] == "NORMAL"
            ]
        )

        total_attacks = len(
            traffic_data[
                traffic_data["status"] == "ATTACK"
            ]
        )

        attack_percentage = round(
            (total_attacks / total_traffic) * 100,
            2
        )

        attack_data = traffic_data[
            traffic_data["status"] == "ATTACK"
        ]

        device_attacks = (
            attack_data["device"]
            .value_counts()
            .to_dict()
        )

    if intrusion_data.empty:

        recent_alerts = []
        average_confidence = 0

    else:

        recent_alerts = (
            intrusion_data
            .tail(10)
            .to_dict("records")
        )

        if "confidence" in intrusion_data.columns:

            average_confidence = round(
                intrusion_data["confidence"].mean(),
                2
            )

        else:

            average_confidence = 0

    return render_template(
        "dashboard.html",
        total_traffic=total_traffic,
        normal_traffic=normal_traffic,
        total_attacks=total_attacks,
        attack_percentage=attack_percentage,
        device_attacks=device_attacks,
        recent_alerts=recent_alerts,
        average_confidence=average_confidence
    )


# ============================================================
# MONITORING
# ============================================================

@app.route("/monitoring")
def monitoring():

    traffic_data = load_traffic_data()
    intrusion_data = load_intrusion_data()

    # --------------------------------------------------------
    # TRAFFIC DATA
    # --------------------------------------------------------

    if traffic_data.empty:

        total_traffic = 0
        normal_traffic = 0
        total_attacks = 0
        attack_percentage = 0
        latest_status = "NO DATA"
        latest_timestamp = "N/A"

    else:

        total_traffic = len(traffic_data)

        normal_traffic = len(
            traffic_data[
                traffic_data["status"] == "NORMAL"
            ]
        )

        total_attacks = len(
            traffic_data[
                traffic_data["status"] == "ATTACK"
            ]
        )

        attack_percentage = round(
            (total_attacks / total_traffic) * 100,
            2
        )

        latest_status = traffic_data.iloc[-1]["status"]

        latest_timestamp = traffic_data.iloc[-1]["timestamp"]


    # --------------------------------------------------------
    # INTRUSION DATA
    # --------------------------------------------------------

    if intrusion_data.empty:

        average_confidence = 0
        recent_alerts = []

    else:

        # Calculate average ML prediction confidence

        if "confidence" in intrusion_data.columns:

            average_confidence = round(
                intrusion_data["confidence"].mean(),
                2
            )

        else:

            average_confidence = 0


        # Get latest 10 intrusion alerts

        recent_alerts = (
            intrusion_data
            .tail(10)
            .to_dict("records")
        )


    # --------------------------------------------------------
    # SEND DATA TO MONITORING PAGE
    # --------------------------------------------------------

    return render_template(
        "monitoring.html",

        total_traffic=total_traffic,

        normal_traffic=normal_traffic,

        total_attacks=total_attacks,

        attack_percentage=attack_percentage,

        latest_status=latest_status,

        latest_timestamp=latest_timestamp,

        average_confidence=average_confidence,

        recent_alerts=recent_alerts
    )


# ============================================================
# IoT DEVICES
# ============================================================

@app.route("/devices")
def devices():

    data = load_traffic_data()

    devices = [
        "Smart_Light_01",
        "Smart_Thermostat_01",
        "Smart_Camera_01",
        "Smart_Lock_01",
        "Smart_Meter_01"
    ]

    device_data = []

    for device in devices:

        if data.empty:

            device_traffic = 0
            device_attacks = 0
            device_normal = 0

        else:

            device_records = data[
                data["device"] == device
            ]

            device_traffic = len(device_records)

            device_attacks = len(
                device_records[
                    device_records["status"] == "ATTACK"
                ]
            )

            device_normal = len(
                device_records[
                    device_records["status"] == "NORMAL"
                ]
            )

        if device_attacks > 0:

            security_status = "ATTACK DETECTED"

        else:

            security_status = "SECURE"

        device_data.append({
            "name": device,
            "traffic": device_traffic,
            "attacks": device_attacks,
            "normal": device_normal,
            "status": security_status
        })

    return render_template(
        "devices.html",
        device_data=device_data
    )


# ============================================================
# INTRUSION LOGS
# ============================================================

@app.route("/logs")
def logs():

    data = load_intrusion_data()

    if data.empty:

        alerts = []

    else:

        alerts = data.to_dict("records")

    return render_template(
        "logs.html",
        alerts=alerts
    )


# ============================================================
# ANALYTICS
# ============================================================

@app.route("/analytics")
def analytics():

    traffic_data = load_traffic_data()

    if traffic_data.empty:

        total_traffic = 0
        normal_traffic = 0
        total_attacks = 0
        attack_percentage = 0
        device_attacks = {}

    else:

        total_traffic = len(traffic_data)

        normal_traffic = len(
            traffic_data[
                traffic_data["status"] == "NORMAL"
            ]
        )

        total_attacks = len(
            traffic_data[
                traffic_data["status"] == "ATTACK"
            ]
        )

        attack_percentage = round(
            (total_attacks / total_traffic) * 100,
            2
        )

        attack_data = traffic_data[
            traffic_data["status"] == "ATTACK"
        ]

        device_attacks = (
            attack_data["device"]
            .value_counts()
            .to_dict()
        )

    return render_template(
        "analytics.html",
        total_traffic=total_traffic,
        normal_traffic=normal_traffic,
        total_attacks=total_attacks,
        attack_percentage=attack_percentage,
        device_attacks=device_attacks
    )


# ============================================================
# MODEL PERFORMANCE
# ============================================================

@app.route("/model")
def model():

    model_file = "intrusion_model.pkl"

    if not os.path.exists(model_file):

        return render_template(
            "model.html",
            model_name="Model Not Found",
            number_of_trees=0,
            number_of_features=0,
            features=[],
            model_status="NOT AVAILABLE"
        )

    import joblib

    trained_model = joblib.load(model_file)

    model_name = type(trained_model).__name__


    # --------------------------------------------------------
    # NUMBER OF TREES
    # --------------------------------------------------------

    if hasattr(trained_model, "n_estimators"):

        number_of_trees = trained_model.n_estimators

    else:

        number_of_trees = 0


    # --------------------------------------------------------
    # NUMBER OF FEATURES
    # --------------------------------------------------------

    if hasattr(trained_model, "n_features_in_"):

        number_of_features = trained_model.n_features_in_

    else:

        number_of_features = 0


    # --------------------------------------------------------
    # FEATURE NAMES
    # --------------------------------------------------------

    if hasattr(trained_model, "feature_names_in_"):

        features = list(
            trained_model.feature_names_in_
        )

    else:

        features = []


    return render_template(
        "model.html",
        model_name=model_name,
        number_of_trees=number_of_trees,
        number_of_features=number_of_features,
        features=features,
        model_status="LOADED"
    )


# ============================================================
# START FLASK SERVER
# ============================================================

if __name__ == "__main__":

    app.run(debug=True)