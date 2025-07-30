from airflow import DAG
from airflow.providers.amazon.aws.operators.glue import AwsGlueJobOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
    'owner': 'suresh',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='sales_glue_job_dag',
    default_args=default_args,
    description='Trigger AWS Glue job to clean sales data',
    schedule_interval='@hourly',
    start_date=days_ago(1),
    catchup=False,
    tags=['aws', 'glue', 's3'],
) as dag:

    run_glue_job = AwsGlueJobOperator(
        task_id='run_sales_data_glue_job',
        job_name='sales_data_cleaning_job',  # Same as in AWS Glue
        aws_conn_id='aws_default',
        region_name='us-east-1'
    )

    run_glue_job
