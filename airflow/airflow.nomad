
# info on extending the docker image: https://airflow.apache.org/docs/apache-airflow/stable/production-deployment.html#production-container-images

# docker pull apache/airflow:v1-10-stable-python3.7-build



# steps:
# - deploy postgres
# - deploy redis
# - deploy celery (with redis as broker and storage)
# - deploy airflow and configure for CeleryExecutor (https://airflow.apache.org/docs/apache-airflow/stable/executor/celery.html)


