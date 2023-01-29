import tweepy
import os
from io import StringIO
import pandas as pd
import json
from datetime import datetime
import boto3

# Create an output path name. Returns AIRFLOW_HOME env, otherwise store the second argument
AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")

def run_twitter_et():

    # Retrieves the credentials from .env files
    access_key = os.environ['tweepy_access_key']
    access_secret = os.environ['tweepy_access_secret']
    consumer_key = os.environ['tweepy_consumer_key']
    consumer_secret = os.environ['tweepy_consumer_secret']

    # Twitter authentication
    auth = tweepy.OAuthHandler(access_key, access_secret)
    auth.set_access_token(consumer_key, consumer_secret)

    # Creating an API object
    api = tweepy.API(auth) # Look up tweepy documentations for details

    # Retrieves all the tweets from elonmusk
    tweets = api.user_timeline(screen_name = '@elonmusk',
                                # count of posts
                                count=200,
                                # don't include retweets
                                include_rts=False,
                                # Need to keep full text
                                tweet_mode='extended'
                                )

    tweet_list = []

    for tweet in tweets:
        text = tweet._json["full_text"]

        # Creates a dictionary with desired columns
        refined_tweet = {"user": tweet.user.screen_name,
                        'text': text,
                        'favorite_count' : tweet.favorite_count,
                        'retweet_count' : tweet.retweet_count,
                        'created_at' : tweet.created_at
                        }
        tweet_list.append(refined_tweet)

    # Saves the resulted list into a DataFrame
    df = pd.DataFrame(tweet_list)
    # Save the DataFrame into csv and save in the Airflow path
    df.to_csv(AIRFLOW_HOME + '/twitter_log.csv')

def run_twitter_load_s3():

    # S3 bucket name
    BUCKET_NAME = "jinchoi-airflow-bucket"
    # Name of csv file object
    KEY = "elonmusk_tweets.csv"

    session = boto3.Session(
        aws_access_key_id=os.environ['aws_access_key_id'],
        aws_secret_access_key=os.environ['aws_secret_access_key']
    )

    # Creating S3 resource from Session
    s3 = session.resource('s3')
    csv_buffer = StringIO()

    # Read the csv and convert into a DataFrame
    df = pd.read_csv(AIRFLOW_HOME + '/twitter_log.csv')
    df.to_csv(csv_buffer)

    # Store the csv file into S3
    s3.Object(BUCKET_NAME, KEY).put(Body=csv_buffer.getvalue())


    # Unused code
    
    # Create an S3FileSystem object
    # s3 = s3fs.S3FileSystem()
    # csv_buffer = df.to_csv().encode()
    # s3.put('s3://{BUCKET_NAME}/data/{KEY}', csv_buffer)   
    # df.to_csv("s3://{BUCKET_NAME}/data/elonmusk_tweets.csv")   
    # Below if I don't get elevated access. This is very limited!
    # client = tweepy.Client(bearer_token=bearer_token)
    # username = 'elonmusk'
    # account = client.get_user(username=username)
    # tweets = client.get_users_tweets(id = account.data.id,  max_results = 100, exclude = "retweets,replies")