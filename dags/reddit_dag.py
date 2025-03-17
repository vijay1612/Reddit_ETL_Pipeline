from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import json
import praw

# ✅ STEP 1: Define the Reddit pipeline function
def reddit_pipeline(file_name, subreddit, time_filter, limit):
    # Read Reddit API credentials from environment variables
    reddit = praw.Reddit(
    reddit = praw.Reddit(
        client_id=os.getenv('REDDIT_CLIENT_ID'),
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
        user_agent=os.getenv('REDDIT_USER_AGENT'),
        username=os.getenv('REDDIT_USERNAME'),
        password=os.getenv('REDDIT_PASSWORD')
    )

    )

    subreddit_obj = reddit.subreddit(subreddit)
    posts = []

    for submission in subreddit_obj.top(time_filter=time_filter, limit=int(limit)):
        posts.append({
            'title': submission.title,
            'score': submission.score,
            'url': submission.url,
            'created_utc': submission.created_utc
        })

    # Make sure output directory exists
    output_dir = '/opt/airflow/output'
    os.makedirs(output_dir, exist_ok=True)

    # Save data to JSON file
    output_path = os.path.join(output_dir, f'{file_name}.json')
    with open(output_path, 'w') as f:
        json.dump(posts, f, indent=4)

    print(f"✅ Extracted {len(posts)} posts and saved to {output_path}")

# ✅ STEP 2: Define default_args and DAG
default_args = {
    'owner': 'vijay Mopuru',
    'start_date': datetime(2023, 10, 22),
    'retries': 1
}

dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'etl', 'pipeline']
)

# ✅ STEP 3: Define PythonOperator to call the pipeline
extract_task = PythonOperator(
    task_id='reddit_extraction',
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name': f'reddit_{datetime.now().strftime("%Y%m%d")}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': '100'
    },
    dag=dag
)

# ✅ Task pipeline
extract_task
