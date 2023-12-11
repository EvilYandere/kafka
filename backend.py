import json

from kafka import KafkaProducer

ORDER_KAFKA_TOPIC = "order_details"
ORDER_LIMIT = 50000

producer = KafkaProducer(bootstrap_servers="localhost:29092")

print("start producing")

for i in range(1, ORDER_LIMIT):
    data = {
        "order_id": i,
        "user_id": f"user_{i}",
        "total_cost": i * 5,
        "items": "food1,food2",
    }

    producer.send(ORDER_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))
    print(f"Done Sending..{i}")