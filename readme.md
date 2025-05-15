# StreamLSTM: Real-time Power Consumption Forecasting Pipeline

This project implements a real-time machine learning pipeline that streams power consumption data using Kafka and trains an LSTM model continuously using BigDL and PyTorch. The entire pipeline is orchestrated with Apache Airflow.

## 📦 Project Structure

```
project/
├── airflow_dag/               # Airflow DAG for orchestrating the pipeline
│   └── stream_lstm_dag.py     
├── kafka/                     # Kafka producer and consumer/trainer
│   ├── producer.py
│   └── consumer_trainer.py
├── model/                     # LSTM model definition and preprocessing utilities
│   ├── lstm_model.py
│   └── preprocess.py
├── data/                      # Input dataset (CSV format)
│   └── your_dataset.csv
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## 🚀 Overview

This pipeline continuously streams chunks of power consumption data from a CSV file to a Kafka topic every 15 minutes. A Kafka consumer picks it up, preprocesses it, and trains an LSTM model in real-time. Apache Airflow schedules this operation using a DAG that triggers every 15 minutes.

## 🔧 Technologies Used

- **Kafka** – Real-time data streaming  
- **PyTorch** – Deep learning framework  
- **BigDL Orca** – Distributed training using PyTorch  
- **Apache Airflow** – Workflow orchestration  
- **Pandas & Scikit-learn** – Data preprocessing

## 📊 Dataset Columns

- `Temperature`
- `Humidity`
- `WindSpeed`
- `GeneralDiffuseFlows`
- `DiffuseFlows`
- `PowerConsumption` (target)

## 🧠 Model Details

- **Architecture**: LSTM
- **Input**: 10 timesteps × 5 features
- **Output**: PowerConsumption
- **Loss Function**: MSE

## ⚙️ Workflow

1. **Kafka Producer (`producer.py`)**  
   Sends 10,000-row CSV chunks to topic `power_data` every 15 minutes.

2. **Kafka Consumer (`consumer_trainer.py`)**  
   Listens for data, preprocesses it, and trains an LSTM model.

3. **Airflow DAG (`stream_lstm_dag.py`)**  
   Triggers `train_on_kafka_stream()` every 15 minutes.

## 💻 Usage

### 1. Install Requirements

``
pip install -r requirements.txt
```
### 2. Start Kafka (ZooKeeper + Kafka)

Ensure local Kafka broker is running on `localhost:9092`.

### 3. Run Kafka Producer

```
python kafka/producer.py
```

### 4. Configure and Run Airflow

- Put `stream_lstm_dag.py` into your Airflow `dags/` folder.
- Run Airflow:

```
airflow db init
airflow webserver --port 8080
airflow scheduler
```

- Visit `localhost:8080` to trigger and monitor DAGs.

## 🧪 Local Test

Run model training directly:

```
python kafka/consumer_trainer.py
```


## 📄 License

Free to use for educational and non-commercial purposes.
