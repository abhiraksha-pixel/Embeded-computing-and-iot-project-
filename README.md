# Edge-AI Based Intrusion Detection System for IoT Networks

An AI-Powered IoT Network Security System Using Machine Learning, ESP32 Simulation, and MQTT Communication.

## Overview

Edge-AI Based Intrusion Detection System for IoT Networks is a Python-based security project designed to demonstrate how Machine Learning can identify suspicious activities in IoT environments.

The project integrates Wokwi ESP32 simulation, MQTT communication through HiveMQ, a Python-based Edge Gateway, and a Random Forest Classifier to analyze incoming IoT telemetry and detect simulated cyberattacks.

The system simulates five IoT components: Smart Light, Smart Thermostat, Smart Camera, Smart Lock, and Smart Meter. The ESP32 simulation transmits device telemetry through MQTT to the Python Edge Gateway, where incoming data is converted into model features and classified as normal or suspicious activity.

A Flask-based interactive dashboard provides visual representations of network traffic, intrusion alerts, device information, analytics, and Machine Learning model details.

The primary goal is to demonstrate an Edge-AI-based approach to IoT security through software simulation, Machine Learning, and centralized monitoring.

## Features

- **IoT Device Simulation:** Simulates five IoT components using ESP32 in Wokwi.
- **MQTT Communication:** Transmits IoT telemetry using the HiveMQ public MQTT broker.
- **Edge Gateway:** Receives MQTT messages and processes incoming IoT data using Python.
- **Machine Learning Detection:** Uses a Random Forest Classifier to identify normal and suspicious activity.
- **Random Forest Model:** Implements 100 decision trees for classification.
- **Traffic Monitoring:** Records simulated network traffic and classification results.
- **Intrusion Detection:** Identifies simulated attack conditions and generates alerts.
- **Automated Logging:** Stores traffic records and detected intrusions in CSV files.
- **Interactive Dashboard:** Displays system status, traffic statistics, and security information.
- **Device Monitoring:** Provides information about simulated IoT devices and their activity.
- **Analytics:** Displays traffic distribution, attack statistics, and intrusion rates.
- **Model Information:** Displays trained model configuration and input features.

## System Architecture

The project follows a structured IoT security monitoring pipeline.

```text
          WOKWI ESP32 SIMULATION
                    |
                    v
              IoT TELEMETRY
                    |
                    v
             MQTT COMMUNICATION
                    |
                    v
              HIVEMQ BROKER
                    |
                    v
           PYTHON EDGE GATEWAY
                    |
                    v
          DATA FEATURE CONVERSION
                    |
                    v
           RANDOM FOREST MODEL
                    |
             +------+------+
             |             |
             v             v
           NORMAL        ATTACK
             |             |
             v             v
        TRAFFIC LOG    INTRUSION LOG
             |             |
             +------+------+
                    |
                    v
             FLASK DASHBOARD
                    |
                    v
          MONITORING AND ANALYTICS
```

## Simulated IoT Components

The project uses an ESP32 DevKit simulation with the following components:

| Component | Function | GPIO Pin |
|---|---|---|
| LED | Smart Light simulation | GPIO 25 |
| DHT22 | Temperature and humidity monitoring | GPIO 4 |
| PIR Sensor | Motion detection | GPIO 27 |
| Servo Motor | Smart Lock simulation | GPIO 26 |
| Potentiometer | Smart Meter simulation | GPIO 34 |

### Wokwi Simulation

The ESP32 firmware performs the following operations:

1. Connects to the Wokwi guest Wi-Fi network.
2. Establishes an MQTT connection with HiveMQ.
3. Reads temperature and humidity from the DHT22 sensor.
4. Detects motion using the PIR sensor.
5. Controls the LED and servo motor.
6. Reads the potentiometer value.
7. Generates normal and simulated attack conditions.
8. Publishes IoT telemetry in JSON format through MQTT.

**Wokwi Project:**

https://wokwi.com/projects/474662184638796801

## System Modules

### 1. IoT Device Simulation

The Wokwi environment simulates an ESP32-based IoT gateway containing five virtual components:

- Smart Light
- Smart Thermostat
- Smart Camera
- Smart Lock
- Smart Meter

The simulation generates device telemetry, including temperature, humidity, motion, and meter readings.

### 2. MQTT Communication

MQTT is used to transmit IoT telemetry from the Wokwi ESP32 simulation to the Python Edge Gateway.

**MQTT Configuration:**

| Parameter | Configuration |
|---|---|
| Broker | broker.hivemq.com |
| Port | 1883 |
| Protocol | MQTT |
| Topic | edge_ai_ids/abhi_esp32_iot_data |

### 3. Python Edge Gateway

The Edge Gateway receives MQTT messages, extracts incoming telemetry, converts the data into features expected by the trained Machine Learning model, and performs intrusion classification.

### 4. Data Processing

The incoming telemetry is converted into numerical network-related features such as:

- Packet Size
- Packets Per Second
- Number of Connections
- Connection Duration
- Device Type
- Communication Protocol

These features are passed to the trained Random Forest model.

### 5. Machine Learning Detection

The project uses a Random Forest Classifier containing 100 decision trees.

The model analyzes the extracted features and classifies incoming traffic into two categories:

- NORMAL
- ATTACK

The classification result and prediction confidence are displayed in the Edge Gateway terminal.

### 6. Traffic Logging

The system automatically records processed traffic information, including timestamps, device details, network-related features, confidence values, and classification status.

Traffic records are stored in CSV format.

### 7. Intrusion Logging

Whenever the model classifies incoming traffic as an attack, the system generates an intrusion alert and stores the corresponding record in the intrusion log.

### 8. Flask Dashboard

The Flask dashboard provides a centralized interface for monitoring IoT security activity and visualizing system information.

## Machine Learning Model

The project implements the **Random Forest Classification Algorithm**.

| Parameter | Configuration |
|---|---|
| Algorithm | Random Forest Classifier |
| Number of Decision Trees | 100 |
| Input Features | 12 |
| Training Dataset | Synthetic IoT Traffic Dataset |
| Classification | NORMAL / ATTACK |
| Model Storage | Joblib (.pkl) |

The Random Forest algorithm combines predictions from multiple decision trees to produce the final classification.

## Dashboard Modules

The Flask dashboard contains the following sections:

| Module | Functionality |
|---|---|
| Dashboard | Displays overall traffic and security status. |
| Monitoring | Shows traffic statistics and recent intrusion alerts. |
| IoT Devices | Displays simulated IoT gateway and component information. |
| Intrusion Logs | Displays detected attack records. |
| Analytics | Presents traffic distribution and attack statistics. |
| Model Performance | Displays Random Forest configuration and input features. |

## Technology Stack

**Programming Languages**
- Python
- C++ (ESP32 Firmware)

**Machine Learning**
- Scikit-learn
- Random Forest Classifier
- Pandas
- NumPy
- Joblib

**Backend**
- Flask
- Paho-MQTT

**IoT Simulation and Communication**
- Wokwi
- ESP32
- MQTT
- HiveMQ

**Sensors and Components**
- DHT22
- PIR Motion Sensor
- LED
- Servo Motor
- Potentiometer

**Frontend and Visualization**
- HTML
- CSS
- Flask Templates

**Data Storage**
- CSV Files

## Project Structure

```text
Edge_AI_IDS/
│
├── dataset/
│   ├── iot_traffic.csv
│   └── processed_iot_traffic.csv
│
├── logs/
│   └── .gitkeep
│
├── templates/
│   ├── dashboard.html
│   ├── monitoring.html
│   ├── devices.html
│   ├── logs.html
│   ├── analytics.html
│   └── model.html
│
├── static/
│   └── style.css
│
├── Wokwi_IoT_Simulation/
│   ├── Wokwi_IoT_Simulation.ino
│   ├── diagram.json
│   ├── libraries.txt
│   ├── wokwi.toml
│   └── wokwi-project.txt
│
├── app.py
├── traffic_generator.py
├── data_preprocessing.py
├── train_model.py
├── edge_gateway.py
├── mqtt_edge_gateway.py
├── mqtt_test.py
├── intrusion_model.pkl
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Install Prerequisites

Install the following software:

- Python 3.13 or compatible version
- Visual Studio Code
- Git
- Wokwi VS Code extension

### 2. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 3. Navigate to the Project Directory

```bash
cd Edge_AI_IDS
```

### 4. Create a Virtual Environment

```bash
python -m venv venv
```

### 5. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If script execution is blocked:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Activate the environment again:

```powershell
.\venv\Scripts\Activate.ps1
```

### 6. Upgrade pip

```bash
python -m pip install --upgrade pip
```

### 7. Install Dependencies

```bash
pip install -r requirements.txt
```

## Wokwi Setup

### 1. Open the Wokwi Project

Open the project folder:

```text
Edge_AI_IDS/Wokwi_IoT_Simulation
```

### 2. Open in Visual Studio Code

Open the `Wokwi_IoT_Simulation.ino` file.

### 3. Verify Project Files

Make sure the following files are available:

- Wokwi_IoT_Simulation.ino
- diagram.json
- libraries.txt
- wokwi.toml

### 4. Start the Simulation

Start the Wokwi simulation and open the Serial Monitor.

Verify that the ESP32 connects to Wi-Fi and the MQTT broker.

**Required Arduino Libraries:**

- DHT sensor library
- PubSubClient
- ESP32Servo

The ESP32 board uses its built-in Wi-Fi support.

## How to Run the Project

The project requires three components to run simultaneously.

### Step 1: Start the MQTT Edge Gateway

Open the first terminal inside the project directory:

```bash
python mqtt_edge_gateway.py
```

The Python gateway connects to HiveMQ, subscribes to the MQTT topic, and waits for incoming IoT telemetry.

### Step 2: Start the Flask Dashboard

Open a second terminal inside the project directory.

Activate the virtual environment and run:

```bash
python app.py
```

The Flask application starts the monitoring dashboard.

### Step 3: Open the Dashboard

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

### Step 4: Start the Wokwi Simulation

1. Open the `Wokwi_IoT_Simulation` folder in VS Code.
2. Open `Wokwi_IoT_Simulation.ino`.
3. Start the Wokwi ESP32 simulation.
4. Open the Serial Monitor.
5. Verify the Wi-Fi and MQTT connections.
6. Observe the generated IoT telemetry.

The Python Edge Gateway receives the telemetry and performs Machine Learning-based classification.

## Simulated Attack Detection

The ESP32 firmware generates a simulated attack condition every fifth IoT cycle.

During normal operation, the system publishes regular telemetry.

During the simulated attack cycle, the Smart Meter generates an anomalous reading of 4095, which the Python gateway maps to high simulated network activity.

**Normal Traffic Example:**

```text
AI Analysis:
Status: NORMAL
Confidence: 100.0 %

Traffic log updated
```

**Simulated Attack Example:**

```text
AI Analysis:
Status: ATTACK
Confidence: 90.0 %

Traffic log updated
Intrusion log updated
ALERT: Intrusion detected!
```

## Project Objective

The objective of this project is to demonstrate how Edge AI and Machine Learning can be integrated into IoT security systems to identify suspicious device activity and generate intrusion alerts.

By combining IoT simulation, MQTT communication, Python-based processing, and Random Forest classification, the project demonstrates an end-to-end intrusion detection workflow with a centralized monitoring dashboard.

## Future Enhancements

- Integration of real-time network packet capture.
- Advanced anomaly detection algorithms.
- Support for additional Machine Learning models.
- Improved feature extraction from network traffic.
- Automated threat response mechanisms.
- Enhanced dashboard visualizations.
- Integration with additional IoT communication protocols.

## Important Note

This project is a software-only academic simulation. IoT telemetry and network-related features are simulated or derived through a demonstration adapter.

The system does not perform real-world network packet inspection or production-grade cybersecurity monitoring.

The Random Forest model is trained using a synthetic dataset. Its reported performance should not be interpreted as guaranteed real-world detection accuracy.

## Author

**Abhi Raksha**  
B.Tech – Electronics and Computer Science (AIML Specialization)  
Christ University

Contributed to the development of AquaSentinel, an AI-powered groundwater intelligence platform focused on monitoring groundwater depletion, predicting future water levels, and identifying contamination risks.

Interested in Artificial Intelligence, Machine Learning, Full-Stack Development, and sustainable technology solutions.

**Connect with me:**
- LinkedIn: www.linkedin.com/in/abhi-raksha-9b3b80369/
- Email: abhiraksha06@gmail.com
