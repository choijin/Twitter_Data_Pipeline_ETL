from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from twitter_etl import run_twitter_et, run_twitter_load_s3

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 25),
    'email': ['jinchoi595@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'catchup': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=10)
}

dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='Our first DAG with ETL process!',
    schedule_interval=timedelta(days=1),
)

# This task involves extracting the data and transforming from JSON into csv
run_extract_transform = PythonOperator(
    task_id='extract_and_transform',
    python_callable=run_twitter_et,
    dag=dag, 
)

# This task involves loading the data into s3
run_load = PythonOperator(
    task_id='load_to_s3',
    python_callable=run_twitter_load_s3,
    dag=dag, 
)

run_extract_transform >> run_load