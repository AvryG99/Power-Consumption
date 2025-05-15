from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kafka.consumer_trainer import train_on_kafka_stream

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 8),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'stream_lstm_train',
    default_args=default_args,
    schedule_interval='*/15 * * * *',
    catchup=False
)

stream_task = PythonOperator(
    task_id='stream_kafka_lstm_training',
    python_callable=train_on_kafka_stream,
    dag=dag
)