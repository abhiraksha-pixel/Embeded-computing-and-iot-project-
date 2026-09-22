import paho.mqtt.publish as publish

publish.single(
    "edge_ai_ids/iot_data",
    '{"device":"TEST_DEVICE","meter":0}',
    hostname="broker.hivemq.com",
    port=1883
)

print("Test message published")
