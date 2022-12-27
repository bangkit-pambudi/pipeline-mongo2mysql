from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import date
from datetime import timedelta
import json

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 0
}

today = date.today()
tommorow = date.today() - timedelta(days=1)
today = "{date}T00:00:00Z".format(date=str(date.today()))
tommorow = "{date}T23:59:59Z".format(date=str(date.today() - timedelta(days=1)))
# tommorow = "2016-06-05T00:00:00Z"
# today = "2022-06-05T23:59:59Z"
query = { "updatedAt" :{"$gte":  {"$date": tommorow}, "$lte":  {"$date": today}}}
query_string =json.dumps(query)
bash_download = 'docker exec -u 0 7ef72c48fc0e mongoexport --db codex -c vaksin_covid -q \'{query}\' --out vaksin.json'.format(query=query_string)

dag = DAG(dag_id='CODEX', 
        default_args=default_args,
        schedule_interval='0 0 * * *')

start_daily = DummyOperator(
    task_id='start_daily',
    trigger_rule='none_failed',
    dag=dag)

download_mongo = BashOperator(
        task_id='download_mongo',
        bash_command = bash_download,
        #bash_command='docker exec -u 0 7ef72c48fc0e mongoexport --db codex -c vaksin_covid --out vaksin.json',
        trigger_rule = 'all_done',
        dag=dag
    )

copy_json = BashOperator(
        task_id='copy_json',
        bash_command="docker cp 7ef72c48fc0e:/vaksin.json '/mnt/c/diary ngoding/Test Telkom/pipeline mongo to mysql/JsonOutput'",
        trigger_rule = 'all_done',
        dag=dag
    )

run_tomysql = BashOperator(
        task_id='run_tomysql',
        bash_command="python3 '/mnt/c/diary ngoding/Test Telkom/pipeline mongo to mysql/run.py'",
        trigger_rule = 'all_success',
        dag=dag
    )


start_daily >> download_mongo >> copy_json >> run_tomysql