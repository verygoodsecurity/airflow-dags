from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_hello():
    return 'Hello world!'

dag = DAG('hello_world2', description='Simple tutorial DAG',
          schedule_interval='0/1 * * * *',
          start_date=datetime(2019, 1, 1), catchup=False)

dummy_operator = DummyOperator(task_id='dummy_task2', retries=3, dag=dag)

hello_operator = PythonOperator(task_id='hello_task2', python_callable=print_hello, dag=dag)

dummy_operator >> hello_operator
