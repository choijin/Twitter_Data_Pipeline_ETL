FROM apache/airflow:2.5.1
COPY requirements.txt .
# no cache means it doesn't save cache
RUN pip install -r requirements.txt

# ENV PYTHONPATH /opt/airflow/dags
# COPY scripts scripts
# RUN chmod +x scripts