from kafka import KafkaConsumer
from io import StringIO
import pandas as pd
import torch
from bigdl.orca import init_orca_context, stop_orca_context
from bigdl.orca.learn.pytorch import Estimator
from model.lstm_model import LSTMModel
from model.preprocess import preprocess
import os

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
def train_on_kafka_stream():
    init_orca_context(cluster_mode="local")
    consumer = KafkaConsumer('power_data', bootstrap_servers=f'{HOST}:{PORT}', group_id='lstm-train')

    model = LSTMModel()
    estimator = Estimator.from_torch(model=model,
                                     optimizer=torch.optim.Adam(model.parameters(), lr=0.001),
                                     loss=torch.nn.MSELoss(),
                                     metrics=['mse'])

    for message in consumer:
        csv_data = StringIO(message.value.decode('utf-8'))
        df = pd.read_csv(csv_data)
        X, y = preprocess(df)
        dataset = torch.utils.data.TensorDataset(X, y)
        estimator.fit(data=dataset, epochs=3, batch_size=64)

    stop_orca_context()