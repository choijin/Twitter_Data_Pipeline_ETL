# Twitter Data Pipeline Project

Click [HERE](https://github.com/choijin/Twitter_Data_Pipeline_ETL/tree/main/airflow-docker) to see the full and detailed script

## Project Overview
Data engineering project using Airflow to perform ETL process on Twitter data and executing tasks inside Docker containers

* Executed data extraction utilizing Twitter API calls (Tweepy)
* Transformed JSON data into CSV using Python scripts and libraries (Pandas, JSON)
* Loaded the processed data into AWS S3 buckets for storage using Python SDK (boto3)
* Orchestrated the ETL process by implementing Airflow and operated the tasks inside Docker to ensure a controlled and isolated environment, resulting in improved development and testing processes and faster time to market

![](/images/pipeline_img_new.png) 

## Objectives
* Develop a complete ETL process from Twitter data to perform exploratory data analysis and create a visual using Tableau

## Part I. Establishing Airflow inside Docker container

### First of all, what is a Docker?

* Docker is used to package, deploy, and run applications in a containerized environment. This allows for consistency and ease of deployment across different environments, as well as improved isolation and resource utilization.

* In essence, Docker allows my code infrastructure to runs the same way every time, no matter where I am running with it.

### And what is Docker-compose?

* Docker Compose is a tool for defining and running multi-container Docker applications. Instead of manually starting each individual container, you can define all the containers, their configuration, and their relationships in a single file called a *docker-compose.yml file*. Using this file, you can spin up all the containers with a single command, making it easier to manage the whole application as a single unit. 

* Additionally, Docker Compose allows for easy scaling of the application by allowing you to add or remove containers as needed. This simplifies the process of managing complex, multi-container applications.

### What is Airflow?

* Apache Airflow is an open-source platform to programmatically author, schedule, and monitor workflows. 

* Apache Airflow works by defining workflows as DAGs in Python, scheduling the workflows, executing the tasks on worker nodes, and monitoring the progress and results of the workflows through the Airflow web UI or API.

![](/images/dag.png) 

The above DAG demonstrates the pipeline for this project. Once the task of extracting and transforming is complete, it triggers the next task, which is the loading task, to store the file into AWS S3.

### Steps

* Create a **Dockerfile**: This is a script that specifies the base image and the necessary dependencies for running Airflow. An **image** is a pre-configured environment that includes all the necessary components, such as libraries, dependencies, and application code, to run a specific application. 
* Create a **docker-compose.yml** file: This file specifies the services, networks, and volumes to be used in the Docker Compose setup.
* Build the **Docker Images**: Run the docker-compose build command to build the Docker images from the Dockerfile.
* Start the **Containers**: Use the docker-compose up command to start the containers and bring up the services.

![](/images/docker-compose.png)

(A snippet of docker-compose.yml)

## Part II. Extraction and Transformation

* Twitter API Elevated Access is required to perform tasks in this project
* API credentials were securely stored inside .env file to prevent hard-coding and unauthorized access
* The tweet posts to extract was tweets from Elon Musk, one of the influential people in the world
* Extracted 200 tweet posts from Elon Musk, stored the 'text', 'favorite counts', 'retweet counts', and 'time stamp' per each tweet into CSV file

![](/images/elon.png)

## Part III. Loading Data

### Why use AWS S3 for storing files?
* S3 makes it easy to store and access your files from anywhere. It is cheap, reliable, and secure, making it a good option for storing important files and data. You can access your files from anywhere on the web and it integrates with other AWS services for more complex solutions.

### What is boto3?
* Boto3 is the Amazon Web Services (AWS) SDK for Python, which allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2. Boto3 makes it easy to integrate your Python application, library, or script with AWS services. 

### Steps
* Create S3 bucket in AWS

![](/images/bucket.png)

* Use boto3 to interact with S3 buckets and objects
* Apply **os.environ** command to access .env files (this way, you can keep sensitive information separate from your application code)
* Read the csv using Pandas library and store the data into S3 by calling **boto3.Session.resource.Object.put()**

![](/images/boto3.png)


