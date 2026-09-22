#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>
#include <ESP32Servo.h>

// ============================================================
// PIN DEFINITIONS
// ============================================================

#define LED_PIN 25
#define DHT_PIN 4
#define PIR_PIN 27
#define SERVO_PIN 26
#define POT_PIN 34

#define DHT_TYPE DHT22

// ============================================================
// WIFI SETTINGS FOR WOKWI
// ============================================================

const char* WIFI_SSID = "Wokwi-GUEST";
const char* WIFI_PASSWORD = "";

// ============================================================
// MQTT SETTINGS
// ============================================================

const char* MQTT_BROKER = "broker.hivemq.com";
const int MQTT_PORT = 1883;

const char* MQTT_TOPIC = "edge_ai_ids/abhi_esp32_iot_data";

// ============================================================
// OBJECTS
// ============================================================

DHT dht(DHT_PIN, DHT_TYPE);
Servo lockServo;

WiFiClient espClient;
PubSubClient mqttClient(espClient);

// ============================================================
// SIMULATION VARIABLES
// ============================================================

int cycleCount = 0;

// ============================================================
// WIFI CONNECTION
// ============================================================

void connectWiFi()
{
    Serial.print("Connecting to WiFi");

    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }

    Serial.println();
    Serial.println("WiFi connected");

    Serial.print("ESP32 IP: ");
    Serial.println(WiFi.localIP());
}

// ============================================================
// MQTT CONNECTION
// ============================================================

void connectMQTT()
{
    while (!mqttClient.connected())
    {
        Serial.print("Connecting to MQTT broker...");

        String clientId = "ESP32-EdgeAI-" + String(random(0xffff), HEX);

        if (mqttClient.connect(clientId.c_str()))
        {
            Serial.println("connected");
        }
        else
        {
            Serial.print("failed, state=");
            Serial.println(mqttClient.state());

            delay(2000);
        }
    }
}

// ============================================================
// SETUP
// ============================================================

void setup()
{
    Serial.begin(115200);

    pinMode(LED_PIN, OUTPUT);
    pinMode(PIR_PIN, INPUT);

    dht.begin();

    lockServo.attach(SERVO_PIN);
    lockServo.write(0);

    Serial.println();
    Serial.println("================================");
    Serial.println("EDGE-AI IoT DEVICE SIMULATION");
    Serial.println("================================");

    Serial.println("ESP32 Gateway Started");

    Serial.println("Smart Light       : READY");
    Serial.println("Smart Thermostat  : READY");
    Serial.println("Smart Camera      : READY");
    Serial.println("Smart Lock        : READY");
    Serial.println("Smart Meter       : READY");

    // Connect to WiFi
    connectWiFi();

    // Configure MQTT
    mqttClient.setServer(MQTT_BROKER, MQTT_PORT);

    // Connect to MQTT broker
    connectMQTT();

    Serial.println("--------------------------------");
    Serial.println("MQTT connection ready");
    Serial.println();
}

// ============================================================
// SEND IOT DATA
// ============================================================

void sendIoTData()
{
    cycleCount++;

    // ========================================================
    // DETERMINE SIMULATED NETWORK CONDITION
    // ========================================================

    bool attackSimulation = (cycleCount % 5 == 0);

    Serial.println("================================");
    Serial.print("IoT Cycle: ");
    Serial.println(cycleCount);

    if (attackSimulation)
    {
        Serial.println("SIMULATED NETWORK CONDITION: ATTACK");
    }
    else
    {
        Serial.println("SIMULATED NETWORK CONDITION: NORMAL");
    }

    Serial.println("================================");

    // ========================================================
    // SMART LIGHT
    // ========================================================

    digitalWrite(LED_PIN, HIGH);

    Serial.println("Smart Light: ON");

    delay(500);

    digitalWrite(LED_PIN, LOW);

    Serial.println("Smart Light: OFF");

    // ========================================================
    // SMART THERMOSTAT
    // ========================================================

    float temperature = dht.readTemperature();
    float humidity = dht.readHumidity();

    if (isnan(temperature))
    {
        temperature = 24.0;
    }

    if (isnan(humidity))
    {
        humidity = 40.0;
    }

    Serial.print("Smart Thermostat: Temperature = ");
    Serial.print(temperature);
    Serial.print(" C, Humidity = ");
    Serial.print(humidity);
    Serial.println(" %");

    // ========================================================
    // SMART CAMERA
    // ========================================================

    int motion = digitalRead(PIR_PIN);

    Serial.print("Smart Camera: ");

    if (motion == HIGH)
    {
        Serial.println("MOTION DETECTED");
    }
    else
    {
        Serial.println("NO MOTION");
    }

    // ========================================================
    // SMART LOCK
    // ========================================================

    lockServo.write(90);

    Serial.println("Smart Lock: UNLOCKED");

    delay(500);

    lockServo.write(0);

    Serial.println("Smart Lock: LOCKED");

    // ========================================================
    // SMART METER
    // ========================================================

    int meterValue = analogRead(POT_PIN);

    // Every 5th cycle, simulate an anomalous condition
    if (attackSimulation)
    {
        meterValue = 4095;

        Serial.println("Smart Meter: ANOMALOUS");
        Serial.println("Network Traffic: HIGH");
    }
    else
    {
        Serial.print("Smart Meter: ");
        Serial.println(meterValue);

        Serial.println("Network Traffic: NORMAL");
    }

    // ========================================================
    // CREATE MQTT JSON MESSAGE
    // ========================================================

    String payload = "{";

    payload += "\"device\":\"ESP32_IoT_Gateway\",";
    payload += "\"temperature\":" + String(temperature, 2) + ",";
    payload += "\"humidity\":" + String(humidity, 2) + ",";
    payload += "\"motion\":" + String(motion) + ",";
    payload += "\"meter\":" + String(meterValue);

    payload += "}";

    // ========================================================
    // PUBLISH TO MQTT
    // ========================================================

    if (mqttClient.publish(MQTT_TOPIC, payload.c_str()))
    {
        Serial.println("--------------------------------");
        Serial.println("IoT data published to MQTT");
        Serial.println(payload);
        Serial.println("--------------------------------");
    }
    else
    {
        Serial.println("MQTT publish failed");
    }

    Serial.println("IoT device cycle completed");
    Serial.println();
}

// ============================================================
// MAIN LOOP
// ============================================================

void loop()
{
    // Check WiFi connection
    if (WiFi.status() != WL_CONNECTED)
    {
        connectWiFi();
    }

    // Check MQTT connection
    if (!mqttClient.connected())
    {
        connectMQTT();
    }

    // Maintain MQTT connection
    mqttClient.loop();

    // Send IoT data
    sendIoTData();

    // Wait 5 seconds
    delay(5000);
}