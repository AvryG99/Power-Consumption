import torch
import numpy as np
from sklearn.preprocessing import MinMaxScaler

scaler_x = MinMaxScaler()
scaler_y = MinMaxScaler()

def preprocess(df, look_back=10):
    data = df[['Temperature', 'Humidity', 'WindSpeed', 'GeneralDiffuseFlows', 'DiffuseFlows', 'PowerConsumption']].values
    X, y = [], []
    for i in range(look_back, len(data)):
        X.append(data[i - look_back:i, :-1])
        y.append(data[i, -1])
    X = scaler_x.fit_transform(np.array(X).reshape(-1, 5)).reshape(-1, look_back, 5)
    y = scaler_y.fit_transform(np.array(y).reshape(-1, 1))
    return torch.tensor(X, dtype=torch.float32), torch.tensor(y, dtype=torch.float32)