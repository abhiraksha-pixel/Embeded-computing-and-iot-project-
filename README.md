# Edge-AI Based Intrusion Detection System for IoT Networks

## Overview

The **Edge-AI Based Intrusion Detection System for IoT Networks** is a software-based cybersecurity project designed to demonstrate how Edge AI and Machine Learning can be used to detect suspicious network behavior in an IoT environment.

The project simulates IoT devices using **ESP32 in Wokwi**. The simulated IoT data is transmitted using **MQTT** to a Python-based Edge Gateway. The Edge Gateway converts the received telemetry into network-related features and uses a trained **Random Forest Machine Learning model** to classify the traffic as either:

- NORMAL
- ATTACK

The detected results are stored in CSV log files and displayed through a **Flask-based web dashboard**.

---

## Project Architecture

```text
                    WOKWI SIMULATION
                         |
                         |
                    ESP32 IoT Device
                         |
        ---------------------------------------
        |          |          |        |       |
     Smart      Smart      Smart    Smart   Smart
     Light    Thermostat   Camera    Lock   Meter
                         |
                         |
                       MQTT
                         |
                         v
              HiveMQ MQTT Broker
                         |
                         |
                         v
              Python Edge Gateway
                         |
                 Data Processing
                         |
                         v
              Random Forest Model
                         |
              ---------------------
              |                   |
           NORMAL                ATTACK
              |                   |
              |            Intrusion Log
              |                   |
              -----------+--------
                         |
                         v
                    CSV Logs
                         |
                         v
                  Flask Web App
                         |
                         v
                  Web Dashboard
