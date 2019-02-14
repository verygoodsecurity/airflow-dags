from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def create_file():
    f = open("created-file.txt","w+");
    f.write("13:55")
    return "file has been created";

dag = DAG('file_creator', description='File creation dag',
          schedule_interval='0/1 * * * * *',
          start_date=datetime(2019, 1, 1), catchup=False)
file_creator_operator = PythonOperator(task_id='create_file', python_callable=create_file, dag=dag)
