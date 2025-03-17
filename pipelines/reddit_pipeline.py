from etls.reddit_etl import connect_reddit
import os
import json

# ✅ Reading Reddit credentials from environment variables for security
CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
SECRET = os.getenv('REDDIT_CLIENT_SECRET')
USER_AGENT = os.getenv('REDDIT_USER_AGENT')
USERNAME = os.getenv('REDDIT_USERNAME')
PASSWORD = os.getenv('REDDIT_PASSWORD')


def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None):
    """
    Reddit ETL Pipeline:
    - Connect to Reddit API.
    - Extract top posts from a subreddit.
    - Save data into a JSON file.
    """

    # ✅ Connecting to Reddit instance using final connection function
    instance = connect_reddit(
        client_id=CLIENT_ID,
        client_secret=SECRET,
        user_agent=USER_AGENT,
        username=USERNAME,
        password=PASSWORD
    )

    print(f"Connected to Reddit API for subreddit: {subreddit}")

    # ✅ Extraction
    subreddit_obj = instance.subreddit(subreddit)
    posts = []

    for submission in subreddit_obj.top(time_filter=time_filter, limit=int(limit)):
        posts.append({
            'title': submission.title,
            'score': submission.score,
            'url': submission.url,
            'created_utc': submission.created_utc
        })

    print(f"Extracted {len(posts)} posts from r/{subreddit}")

    # ✅ Loading: Save posts to JSON file
    output_dir = '/opt/airflow/output'
    os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists

    output_path = f"{output_dir}/{file_name}.json"
    with open(output_path, 'w') as f:
        json.dump(posts, f, indent=4)

    print(f"Data saved successfully to {output_path}")


# ✅ Example call (Comment out when using in Airflow DAG)
# reddit_pipeline(file_name='reddit_data', subreddit='dataengineering', time_filter='day', limit=100)
