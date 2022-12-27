# pipeline mongo to mysql
Requirement : Python 3.7, Airflow 2.2.3, and Ubuntu 20.04

## 1. Docker Compose

``` bash
docker compose -f docker-compose.yml up -d
```

## 2. Install Airflow

``` bash
AIRFLOW_VERSION=2.2.3
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip3 install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

## 3. How to use
``` bash
run dag in airflow
```
