import redis
import json
import time
def consume_queue():
    r = redis.Redis(host="redis", port=6379, db=0)
    print("📡 Listening for threats in Redis queue...")
    while True:
        _, data = r.blpop("threat_queue")
        payload = json.loads(data)
        print(f"🛡️ Processed: {json.dumps(payload, indent=2)}")
        time.sleep(1)
if __name__ == "__main__":
    consume_queue()
