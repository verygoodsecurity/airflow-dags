from airflow.models import DAG, Variable
from airflow.utils import dates
from airflow.operators.bash_operator import BashOperator
from airflow.operators.latest_only_operator import LatestOnlyOperator
from airflow.operators import BashReader, SecretManager
import os


br = BashReader(__file__)
script_to_run = br.read_script()

args = {
    'owner': 'airflow',
    'start_date': dates.days_ago(1)
}

dag = DAG(
    dag_id='from_sftp_to_s3',
    default_args=args,
    schedule_interval='*/1 * * * *')

vgs_api = Variable.get("vgs_api")
vgs_user = Variable.get("vgs_user")
vgs_password = Variable.get("vgs_password")
sm = SecretManager(username=vgs_user, password=vgs_password, api_host=vgs_api)

aws_access_key_id=sm.decrypt("tok_dev_2AXxzhyPZh1Rm6KCYQPCrG")
aws_secret_access_key=sm.decrypt("tok_dev_eXYD1EQfoc56Nk5NoabgXR")
sftp_server_pass=sm.decrypt("tok_dev_qHUDREV3TvS691g1eUHwE3")

#test_key = os.environ['AIRFLOW_USER_PASS']
#var1 = Variable.get("TEST_KEY")


task = BashOperator(
    task_id='from_sftp_to_s3',
    bash_command=script_to_run,
    params={"sftp_server_pass": sftp_server_pass,"aws_access_key_id": aws_access_key_id, "aws_secret_access_key": aws_secret_access_key},
    dag=dag)
