from kafka import KafkaProducer
import pandas as pd
import time
import os

data_path = os.getenv("DATA_PAHT")
def produce_data():
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    df = pd.read_csv(data_path)

    for i in range(0, 50000, 10000):
        chunk = df.iloc[i:i+10000]
        csv_data = chunk.to_csv(index=False)
        producer.send('power_data', csv_data.encode('utf-8'))
        producer.flush()
        time.sleep(900)  # simulate 15-minute interval

if __name__ == '__main__':
    produce_data()