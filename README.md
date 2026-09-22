Below is a **detailed, GitHub-ready `README.md`** written specifically for your implemented project. It explains the architecture, Wokwi simulation, MQTT communication, Edge-AI processing, Random Forest model, Flask dashboard, project structure, installation, execution, data flow, limitations, and future enhancements.

You can copy this entire content into:

```text
Edge_AI_IDS/README.md
```

# Edge-AI Based Intrusion Detection System for IoT Networks

A software-based Edge-AI Intrusion Detection System (IDS) that simulates an IoT network using ESP32 and Wokwi, transfers IoT telemetry through MQTT, analyzes the incoming data at an edge gateway using a Random Forest Machine Learning model, and presents the security status through a Flask-based web dashboard.

---

## 1. Project Overview

The rapid growth of Internet of Things (IoT) devices has introduced new cybersecurity challenges. IoT devices continuously generate network traffic and telemetry, making them potential targets for malicious activities.

This project demonstrates an **Edge-AI based Intrusion Detection System for IoT Networks** using a completely software-based environment.

Instead of requiring physical ESP32 boards and sensors, the project uses **Wokwi** to simulate an ESP32-based IoT environment. The simulated ESP32 collects sensor and actuator information and publishes the data through **MQTT**.

A Python-based Edge Gateway receives the MQTT messages and processes them locally. A previously trained **Random Forest classifier** analyzes the generated network-related features and classifies the traffic as:

* `NORMAL`
* `ATTACK`

The results are stored in CSV logs and visualized using a Flask web application.

The complete system demonstrates the integration of:

```text
IoT Simulation
       +
MQTT Communication
       +
Edge Computing
       +
Machine Learning
       +
Cybersecurity
       +
Web-Based Monitoring
```

---

# 2. Objectives

The main objectives of this project are:

1. To simulate an IoT network using ESP32 and Wokwi.
2. To simulate multiple IoT devices and their activities.
3. To establish MQTT-based communication between the IoT simulation and Edge Gateway.
4. To generate and preprocess IoT network traffic data.
5. To train a Machine Learning model for intrusion classification.
6. To perform traffic classification at the edge using a Random Forest model.
7. To record normal and attack events.
8. To provide a web-based dashboard for monitoring the simulated IoT environment.
9. To demonstrate how Edge AI can be integrated into an IoT cybersecurity architecture.
10. To provide a software-only environment that does not require physical IoT hardware.

---

# 3. System Architecture

The overall architecture of the project is:

```text
                  WOKWI IoT SIMULATION
                         |
                         v
                  ESP32 Controller
                         |
        -------------------------------------
        |          |          |       |      |
        v          v          v       v      v
     Smart      Smart      Smart   Smart   Smart
     Light    Thermostat   Camera   Lock    Meter
                         |
                         v
                    MQTT Publish
                         |
                         v
              HiveMQ MQTT Broker
                         |
                         v
              Python Edge Gateway
                         |
                         v
              Feature Conversion
                         |
                         v
             Random Forest Classifier
                         |
                 ----------------
                 |              |
                 v              v
              NORMAL          ATTACK
                 |              |
                 |              v
                 |       Intrusion Log
                 |              |
                 -----------+----
                            |
                            v
                       CSV Logs
                            |
                            v
                      Flask Web App
                            |
                            v
                    Security Dashboard
```

---

# 4. Complete Data Flow

The complete data flow is:

```text
Wokwi ESP32
     |
     | Sensor / actuator simulation
     v
IoT Telemetry
     |
     | MQTT
     v
HiveMQ Broker
     |
     | MQTT Subscription
     v
Python Edge Gateway
     |
     | Feature Adapter
     v
Network Feature Vector
     |
     | Machine Learning
     v
Random Forest Model
     |
     +--------------------+
     |                    |
     v                    v
 NORMAL                 ATTACK
     |                    |
     |                    v
     |             Intrusion Log
     |                    |
     +----------+---------+
                |
                v
          Traffic Logs
                |
                v
          Flask Dashboard
```

---

# 5. IoT Simulation

The project uses **Wokwi** to simulate an ESP32-based IoT environment.

The simulation contains five IoT components.

| IoT Component    | Wokwi Component | Purpose                            |
| ---------------- | --------------- | ---------------------------------- |
| Smart Light      | LED             | Simulates an IoT lighting actuator |
| Smart Thermostat | DHT22           | Provides temperature and humidity  |
| Smart Camera     | PIR Sensor      | Simulates motion detection         |
| Smart Lock       | Servo Motor     | Simulates a smart door lock        |
| Smart Meter      | Potentiometer   | Simulates meter/analog readings    |

The ESP32 controls these components and generates simulated IoT telemetry.

---

# 6. ESP32 Pin Configuration

The current Wokwi circuit uses the following GPIO connections:

| Component                   | ESP32 Pin |
| --------------------------- | --------: |
| LED / Smart Light           |   GPIO 25 |
| DHT22 Data                  |    GPIO 4 |
| PIR Output                  |   GPIO 27 |
| Servo / Smart Lock          |   GPIO 26 |
| Potentiometer / Smart Meter |   GPIO 34 |

The ESP32 firmware is located at:

```text
Wokwi_IoT_Simulation/Wokwi_IoT_Simulation.ino
```

---

# 7. ESP32 Firmware

The ESP32 firmware performs the following operations:

1. Initializes the sensors and actuators.
2. Connects to the Wokwi Wi-Fi network.
3. Connects to the MQTT broker.
4. Reads simulated sensor information.
5. Controls the simulated actuators.
6. Generates IoT telemetry.
7. Publishes the telemetry through MQTT.
8. Repeats the process continuously.

The firmware also includes a simulated network condition.

The simulation periodically generates:

```text
NORMAL
```

and:

```text
ATTACK
```

conditions to demonstrate the IDS pipeline.

---

# 8. MQTT Communication

MQTT is used as the communication protocol between the simulated ESP32 and the Python Edge Gateway.

The current MQTT configuration is:

```text
Broker:
broker.hivemq.com

Port:
1883

Topic:
edge_ai_ids/abhi_esp32_iot_data
```

The communication process is:

```text
ESP32
  |
  | Publish
  v
HiveMQ MQTT Broker
  |
  | Subscribe
  v
Python Edge Gateway
```

The ESP32 publishes JSON-formatted data.

A typical message contains information such as:

```json
{
    "device": "ESP32_IoT_Gateway",
    "temperature": 24.50,
    "humidity": 40.00,
    "motion": 0,
    "meter": 1500
}
```

The exact values change according to the simulation.

---

# 9. Machine Learning Pipeline

The Machine Learning pipeline consists of three major stages:

```text
Traffic Generation
        |
        v
Data Preprocessing
        |
        v
Random Forest Training
```

The relevant files are:

```text
traffic_generator.py
data_preprocessing.py
train_model.py
```

---

# 10. Traffic Generation

The file:

```text
traffic_generator.py
```

generates a synthetic IoT network traffic dataset.

The dataset contains attributes such as:

* Device
* Packet size
* Packets per second
* Number of connections
* Protocol
* Duration
* Status

The traffic is classified into:

```text
NORMAL
ATTACK
```

The generated dataset is stored at:

```text
dataset/iot_traffic.csv
```

The project currently contains a dataset with 1000 records.

---

# 11. Data Preprocessing

The file:

```text
data_preprocessing.py
```

prepares the generated dataset for Machine Learning.

The preprocessing includes:

### Label conversion

The traffic labels are converted into numerical values:

```text
NORMAL -> 0
ATTACK -> 1
```

### Categorical encoding

Categorical values such as:

* Device
* Protocol

are converted into numerical feature columns using one-hot encoding.

The processed dataset is stored at:

```text
dataset/processed_iot_traffic.csv
```

---

# 12. Machine Learning Model

The project uses:

```text
RandomForestClassifier
```

from Scikit-learn.

The training script is:

```text
train_model.py
```

The model configuration uses:

```text
Number of trees = 100
Random state = 42
```

The trained model is saved as:

```text
intrusion_model.pkl
```

---

# 13. Model Features

The trained Random Forest model uses 12 input features.

### Network Features

```text
packet_size
packets_per_second
connections
duration
```

### Device Features

```text
device_Smart_Camera_01
device_Smart_Light_01
device_Smart_Lock_01
device_Smart_Meter_01
device_Smart_Thermostat_01
```

### Protocol Features

```text
protocol_MQTT
protocol_TCP
protocol_UDP
```

Therefore:

```text
4 network features
+
5 device features
+
3 protocol features
=
12 features
```

---

# 14. Model Output

The model performs binary classification.

```text
0 -> NORMAL
1 -> ATTACK
```

The Edge Gateway also obtains the model's class probabilities.

For example:

```text
NORMAL = 8%
ATTACK = 92%
```

The highest probability is displayed as the prediction confidence.

Therefore:

```text
Prediction = ATTACK
Confidence = 92%
```

The confidence value represents the probability produced by the classifier. It should not be interpreted as proof that a real-world attack has occurred.

---

# 15. Edge-AI Gateway

The main Edge-AI processing is implemented in:

```text
mqtt_edge_gateway.py
```

The gateway performs the following steps:

```text
1. Load trained model
       |
2. Connect to MQTT broker
       |
3. Subscribe to IoT topic
       |
4. Receive ESP32 telemetry
       |
5. Convert telemetry to model features
       |
6. Run Random Forest prediction
       |
7. Calculate prediction confidence
       |
8. Store traffic log
       |
9. Store intrusion log if attack detected
```

---

# 16. Telemetry-to-Feature Adapter

An important part of the current implementation is the feature adapter.

The Wokwi ESP32 produces IoT telemetry such as:

```text
Temperature
Humidity
Motion
Meter
```

However, the trained Machine Learning model expects network-related features such as:

```text
Packet Size
Packets Per Second
Connections
Duration
Protocol
Device
```

Therefore, the Edge Gateway converts the simulated IoT telemetry into the feature format expected by the model.

Conceptually:

```text
Wokwi Telemetry
       |
       v
Feature Adapter
       |
       v
Network Features
       |
       v
Random Forest
```

This is a **simulation-oriented feature mapping**.

It does not represent real packet capture or real network-flow extraction.

---

# 17. Simulated Normal and Attack Conditions

The Wokwi firmware periodically generates a simulated abnormal condition.

Under a normal condition, the gateway uses lower network-feature values.

Under the simulated attack condition, the feature adapter generates higher values such as:

```text
Packet Size       = 1200
Packets/Second    = 300
Connections       = 50
Duration          = 3 seconds
```

These values are then passed to the Random Forest model.

This demonstrates how an abnormal IoT condition can be passed through the Edge-AI pipeline.

---

# 18. Logging System

The project uses CSV files for logging.

The log directory is:

```text
logs/
```

Two runtime log files are generated:

```text
logs/traffic_log.csv
logs/intrusion_log.csv
```

These runtime CSV files are intentionally excluded from the GitHub repository through `.gitignore`.

The repository contains:

```text
logs/.gitkeep
```

so that the logs directory itself is preserved.

---

# 19. Traffic Log

The traffic log contains processed traffic records.

Typical fields include:

```text
timestamp
device
packet_size
packets_per_second
connections
duration
protocol
confidence
status
```

Example:

```text
2026-09-22 11:30:15,
ESP32_IoT_Gateway,
200,
5,
2,
15,
MQTT,
99.50,
NORMAL
```

---

# 20. Intrusion Log

The intrusion log stores attack-classified records.

It contains information such as:

```text
timestamp
device
packet_size
packets_per_second
connections
duration
protocol
confidence
status
```

The record is written when the Edge Gateway classifies the traffic as:

```text
ATTACK
```

---

# 21. Flask Web Dashboard

The web application is implemented using Flask.

The main file is:

```text
app.py
```

Start the application using:

```powershell
python app.py
```

The dashboard is available at:

```text
http://127.0.0.1:5000
```

---

# 22. Dashboard Pages

The Flask application contains the following pages:

| Page              | Route         | Purpose                            |
| ----------------- | ------------- | ---------------------------------- |
| Dashboard         | `/`           | Overall security overview          |
| Monitoring        | `/monitoring` | Traffic and monitoring information |
| IoT Devices       | `/devices`    | Simulated IoT device information   |
| Intrusion Logs    | `/logs`       | Attack records                     |
| Analytics         | `/analytics`  | Traffic statistics                 |
| Model Performance | `/model`      | ML model configuration             |

---

# 23. Dashboard Page

The Dashboard provides an overall summary of the IoT security environment.

It can display:

* Total Traffic
* Normal Traffic
* Total Intrusions
* Attack Percentage
* ML Confidence
* Threat Status
* Monitoring Status
* Recent Alerts
* IoT Gateway information

---

## Total Traffic

Total number of processed traffic records.

For example:

```text
Total Traffic = 190
```

means 190 traffic records have been processed.

---

## Normal Traffic

Number of traffic records classified as:

```text
NORMAL
```

---

## Total Intrusions

Number of records classified as:

```text
ATTACK
```

---

## Attack Percentage

The attack rate is calculated using:

```text
Attack Percentage =
(Total Attacks / Total Traffic) × 100
```

For example:

```text
42 / 190 × 100 = 22.11%
```

---

## Threat Status

The dashboard can display an alert status when attack records are present.

For example:

```text
ALERT
```

This means attack-classified records are present in the data being displayed.

It does not mean that a real-world cyberattack has been independently verified.

---

## ML Confidence

The dashboard displays the prediction confidence obtained from the Machine Learning classifier.

For example:

```text
94.92%
```

This represents the highest class probability returned by the Random Forest model for the corresponding prediction.

---

# 24. Monitoring Page

The Monitoring page provides more detailed traffic information.

It includes:

* Total Traffic
* Normal Traffic
* Attack Traffic
* Attack Percentage
* Latest Status
* Latest Timestamp
* Average Confidence
* Recent Alerts

The page is intended to provide a more detailed view of the system's current monitoring state.

---

# 25. IoT Devices Page

The IoT Devices page represents the simulated IoT environment.

The simulated gateway contains:

```text
ESP32 IoT Gateway
     |
     +-- Smart Light
     +-- Smart Thermostat
     +-- Smart Camera
     +-- Smart Lock
     +-- Smart Meter
```

The page provides information about device traffic and attack records.

---

# 26. Smart Light

The Smart Light is represented using an LED.

The ESP32 controls the LED through:

```text
GPIO 25
```

The LED demonstrates an IoT actuator.

---

# 27. Smart Thermostat

The Smart Thermostat uses a DHT22 sensor.

It provides:

```text
Temperature
Humidity
```

The DHT22 data line is connected to:

```text
GPIO 4
```

---

# 28. Smart Camera

The Smart Camera uses a PIR motion sensor.

It provides:

```text
Motion Detected
No Motion
```

The PIR output is connected to:

```text
GPIO 27
```

---

# 29. Smart Lock

The Smart Lock is simulated using a servo motor.

The servo is connected to:

```text
GPIO 26
```

The simulation moves the servo between locked and unlocked positions.

---

# 30. Smart Meter

The Smart Meter is simulated using a potentiometer.

It is connected to:

```text
GPIO 34
```

The analog value is read by the ESP32.

During the simulated attack condition, an anomalous high meter value is generated.

---

# 31. Intrusion Logs Page

The Intrusion Logs page provides detailed information about detected attacks.

A typical record contains:

| Field          | Description                     |
| -------------- | ------------------------------- |
| Timestamp      | Time of processing              |
| Device         | Source simulated device         |
| Packet Size    | Simulated packet size           |
| Packets/Second | Simulated traffic rate          |
| Connections    | Simulated number of connections |
| Duration       | Simulated duration              |
| Protocol       | Communication protocol          |
| Confidence     | Model probability               |
| Status         | Classification result           |

This page is useful for examining individual security events.

---

# 32. Analytics Page

The Analytics page summarizes the traffic statistically.

It displays:

* Total Traffic
* Normal Traffic
* Attack Traffic
* Attack Rate
* Device-level attack counts

This allows the user to analyze the overall traffic pattern rather than inspecting individual records.

---

# 33. Model Performance Page

The Model Performance page reads information directly from:

```text
intrusion_model.pkl
```

It displays information such as:

```text
Model:
RandomForestClassifier

Trees:
100

Features:
12

Status:
LOADED
```

It also displays the 12 features used by the model.

This ensures that the dashboard reports the configuration of the actual saved model rather than using hardcoded values.

---

# 34. Project File Structure

```text
Edge_AI_IDS/
│
├── app.py
│
├── traffic_generator.py
├── data_preprocessing.py
├── train_model.py
├── edge_gateway.py
├── mqtt_edge_gateway.py
│
├── mqtt_test.py
├── mqtt_publish_test.py
├── wokwi_mqtt_receiver.py
│
├── intrusion_model.pkl
│
├── dataset/
│   ├── iot_traffic.csv
│   └── processed_iot_traffic.csv
│
├── logs/
│   └── .gitkeep
│
├── static/
│   └── style.css
│
├── templates/
│   ├── dashboard.html
│   ├── monitoring.html
│   ├── devices.html
│   ├── logs.html
│   ├── analytics.html
│   └── model.html
│
├── Wokwi_IoT_Simulation/
│   ├── Wokwi_IoT_Simulation.ino
│   ├── diagram.json
│   ├── libraries.txt
│   ├── wokwi-project.txt
│   └── wokwi.toml
│
├── .gitignore
└── README.md
```

---

# 35. Description of Important Files

### `traffic_generator.py`

Generates the synthetic IoT network traffic dataset.

### `data_preprocessing.py`

Preprocesses and encodes the dataset for Machine Learning.

### `train_model.py`

Trains the Random Forest classifier and saves the trained model.

### `intrusion_model.pkl`

Saved Random Forest Machine Learning model.

### `edge_gateway.py`

Earlier Python-based simulated Edge Gateway that generates and analyzes traffic locally.

### `mqtt_edge_gateway.py`

Main MQTT-based Edge Gateway used for the Wokwi-to-ML pipeline.

### `app.py`

Flask web application that provides the security dashboard.

### `mqtt_test.py`

Used for testing MQTT message reception.

### `mqtt_publish_test.py`

Used for testing MQTT message publishing.

### `wokwi_mqtt_receiver.py`

MQTT-related receiver/testing utility.

### `Wokwi_IoT_Simulation.ino`

ESP32 firmware used by the Wokwi simulation.

### `diagram.json`

Defines the Wokwi circuit and component connections.

### `libraries.txt`

Lists the libraries required by the Wokwi Arduino project.

### `wokwi.toml`

Wokwi project configuration.

---

# 36. Software Requirements

The project uses:

```text
Python 3.13+
Git
Arduino CLI
Wokwi
Visual Studio Code
```

Python packages:

```text
pandas
numpy
scikit-learn
joblib
Flask
paho-mqtt
```

---

# 37. Installation

## Step 1: Clone the Repository

Clone the GitHub repository:

```powershell
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project:

```powershell
cd Edge_AI_IDS
```

---

# 38. Create Python Virtual Environment

Create the environment:

```powershell
python -m venv venv
```

Activate it:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

---

# 39. Install Dependencies

Install the required Python packages:

```powershell
pip install pandas numpy scikit-learn joblib flask paho-mqtt
```

---

# 40. Run the Complete System

The complete demonstration requires three components:

```text
1. Wokwi ESP32 Simulation
2. MQTT Edge Gateway
3. Flask Dashboard
```

---

## Terminal 1: MQTT Edge Gateway

Open a terminal in the project directory and activate the virtual environment.

Run:

```powershell
python mqtt_edge_gateway.py
```

Expected output includes:

```text
Random Forest model loaded
Starting Edge-AI MQTT Gateway...
Connecting to MQTT broker...
Connected to MQTT broker
Subscribed to: edge_ai_ids/abhi_esp32_iot_data
```

Keep this terminal running.

---

# 41. Terminal 2: Flask Dashboard

Open another terminal.

Navigate to the project:

```powershell
cd "C:\Users\Abhi Raksha\OneDrive\Desktop\Edge_AI_IDS"
```

Activate the environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Run:

```powershell
python app.py
```

The Flask application will run at:

```text
http://127.0.0.1:5000
```

---

# 42. Start Wokwi

Open:

```text
Wokwi_IoT_Simulation
```

Open:

```text
Wokwi_IoT_Simulation.ino
```

Start the simulation.

The ESP32 will:

```text
Connect to Wi-Fi
       |
Connect to MQTT
       |
Read simulated components
       |
Generate telemetry
       |
Publish MQTT data
```

---

# 43. Verify the Complete Pipeline

Once all three components are running:

```text
Wokwi
  |
  v
MQTT Broker
  |
  v
mqtt_edge_gateway.py
  |
  v
Random Forest
  |
  v
CSV Logs
  |
  v
Flask Dashboard
```

The MQTT Edge Gateway should display messages such as:

```text
Received Wokwi IoT data
```

followed by:

```text
AI Analysis:
Status: NORMAL
Confidence: ...
```

or:

```text
AI Analysis:
Status: ATTACK
Confidence: ...

ALERT: Intrusion detected!
```

---

# 44. Accessing the Dashboard

Open a browser and visit:

```text
http://127.0.0.1:5000
```

Available routes:

```text
/             Dashboard
/monitoring   Monitoring
/devices      IoT Devices
/logs         Intrusion Logs
/analytics    Analytics
/model        Model Performance
```

---

# 45. GitHub Repository

The project contains a `.gitignore` file to prevent unnecessary runtime files from being uploaded.

The following are excluded:

```text
venv/
__pycache__/
logs/*.csv
Wokwi_IoT_Simulation/build/
.vscode/
temporary files
```

The trained model is intentionally included:

```text
intrusion_model.pkl
```

The dataset is also included:

```text
dataset/iot_traffic.csv
dataset/processed_iot_traffic.csv
```

---

# 46. Limitations

This project is primarily an educational and simulation-based implementation.

## 46.1 Synthetic Dataset

The Machine Learning dataset is generated programmatically.

It is not a dataset collected from a real IoT deployment.

Therefore, the model's performance on this dataset should not be interpreted as real-world IDS performance.

---

## 46.2 Simulated Network Features

The Wokwi ESP32 generates IoT telemetry.

It does not capture actual network packets.

The Edge Gateway maps the telemetry to network-related features expected by the trained model.

Therefore, the project demonstrates the **architecture and workflow of an Edge-AI IDS**, rather than a production packet-level network intrusion detection system.

---

## 46.3 Synthetic Attack Conditions

The attack conditions are simulated.

They are not actual cyberattacks against the IoT system.

The system uses predefined abnormal feature conditions to demonstrate the classification pipeline.

---

## 46.4 Public MQTT Broker

The project currently uses:

```text
broker.hivemq.com
```

on port:

```text
1883
```

This is suitable for demonstration purposes.

A production system should use:

* MQTT authentication
* TLS encryption
* Access control
* Private MQTT infrastructure
* Secure credentials

---

# 47. Future Enhancements

The system can be extended in several ways.

## Real Network Traffic

Replace synthetic network features with real network-flow information.

For example:

```text
Packet Capture
      |
      v
Flow Extraction
      |
      v
Feature Engineering
      |
      v
ML Model
```

---

## Real IoT Dataset

The model can be retrained using publicly available IoT cybersecurity datasets or traffic collected from controlled environments.

---

## More Attack Types

The current model uses:

```text
NORMAL
ATTACK
```

Future versions could distinguish between different attack categories such as:

```text
DoS
DDoS
Port Scanning
Brute Force
Botnet Traffic
MQTT Abuse
```

---

## Improved Machine Learning

Future versions could compare:

```text
Random Forest
Decision Tree
SVM
KNN
Gradient Boosting
Neural Networks
```

---

## Real-Time Dashboard

The current Flask dashboard reads logged information.

A future version could use WebSockets or Server-Sent Events to provide real-time updates without refreshing the page.

---

## Secure MQTT

The MQTT communication can be improved using:

```text
MQTT over TLS
Authentication
Authorization
Certificate-based security
```

---

## Database Integration

Instead of CSV files, a future implementation could use:

```text
SQLite
MySQL
PostgreSQL
MongoDB
```

for persistent event storage.

---

# 48. Academic Significance

This project combines several important areas of Computer Science and Electronics:

```text
Internet of Things
        |
        v
Embedded Systems
        |
        v
MQTT Communication
        |
        v
Edge Computing
        |
        v
Machine Learning
        |
        v
Cybersecurity
        |
        v
Web Application
```

It demonstrates how these technologies can be integrated into a single security monitoring architecture.

---

# 49. Project Demonstration

During a demonstration, the recommended sequence is:

### Step 1

Start the MQTT Edge Gateway:

```powershell
python mqtt_edge_gateway.py
```

### Step 2

Start Flask:

```powershell
python app.py
```

### Step 3

Start the Wokwi ESP32 simulation.

### Step 4

Show the MQTT messages arriving at the Edge Gateway.

### Step 5

Show the Random Forest prediction:

```text
NORMAL
```

or:

```text
ATTACK
```

### Step 6

Open the Flask Dashboard.

### Step 7

Show:

```text
Dashboard
      |
Monitoring
      |
IoT Devices
      |
Intrusion Logs
      |
Analytics
      |
Model Performance
```

This demonstrates the complete system from IoT simulation to Edge-AI classification and visualization.

---

---

# 51. Important Technical Note

This project should be described as a **software simulation and proof-of-concept architecture**.

The current implementation does not perform:

```text
Real packet capture
Real network-flow extraction
Real-world attack execution
```

Instead, it demonstrates:

```text
IoT Simulation
      +
MQTT Communication
      +
Edge Processing
      +
Machine Learning Classification
      +
Security Logging
      +
Web Visualization
```

This distinction is important when interpreting the Machine Learning results.

---

# 52. Conclusion

The Edge-AI Based Intrusion Detection System demonstrates how Machine Learning can be incorporated into an IoT security architecture at the edge.

The system integrates:

* ESP32 simulation
* Wokwi
* MQTT
* Python
* Random Forest
* Edge processing
* CSV-based logging
* Flask
* Web-based monitoring

The resulting architecture provides a complete educational demonstration of an IoT security pipeline in which simulated IoT data is transmitted, processed at an edge gateway, classified using Machine Learning, logged, and visualized through a web dashboard.

---

## Author

**Abhi Raksha**

**Project:** Edge-AI Based Intrusion Detection System for IoT Networks

**Purpose:** Academic / Educational Project
