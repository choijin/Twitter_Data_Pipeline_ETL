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

## Part I. Establishing Docker Environment

### First of all, why use Docker?

Docker is used to package, deploy, and run applications in a containerized environment. This allows for consistency and ease of deployment across different environments, as well as improved isolation and resource utilization.

In essence, Docker allows my code infrastructure to runs the same way every time, no matter where I am running with it.

### Then why Docker-compose?

Docker Compose is a tool for defining and running multi-container Docker applications. Instead of manually starting each individual container, you can define all the containers, their configuration, and their relationships in a single file called a docker-compose.yml file. Using this file, you can spin up all the containers with a single command, making it easier to manage the whole application as a single unit. Additionally, Docker Compose allows for easy scaling of the application by allowing you to add or remove containers as needed. This simplifies the process of managing complex, multi-container applications.

## Part II. Extraction and Transformation

* Twitter API Elevated Access is required to perform tasks in this project
* API credentials were securely stored inside .env file to prevent hard-coding and unauthorized access
* The tweet posts to extract was tweets from Elon Musk, one of the influential people in the world
* Extracted 200 tweet posts from Elon Musk, stored the 'text', 'favorite counts', 'retweet counts', and 'time stamp' per each tweet into CSV file

## Part III. Loading Data




