import os
import praw
from praw import Reddit


def connect_reddit() -> Reddit:
    """
    Establish connection to Reddit using environment variables for credentials.
    """
    try:
        reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent=os.getenv("REDDIT_USER_AGENT"),
            username=os.getenv("REDDIT_USERNAME"),
            password=os.getenv("REDDIT_PASSWORD")
        )
        print("✅ Successfully connected to Reddit!")
        return reddit

    except Exception as e:
        print(f"❌ Failed to connect to Reddit: {e}")
        return None


def extract_posts(reddit_instance: Reddit, subreddit: str, time_filter: str = 'day', limit: int = 100):
    """
    Extract top posts from a specified subreddit using the Reddit instance.

    Args:
        reddit_instance (Reddit): Authenticated Reddit instance.
        subreddit (str): Subreddit name to extract posts from.
        time_filter (str): Filter for top posts ('day', 'week', 'month', etc.).
        limit (int): Number of posts to retrieve.

    Returns:
        list: List of dictionaries containing post data.
    """
    try:
        subreddit_obj = reddit_instance.subreddit(subreddit)
        posts = subreddit_obj.top(time_filter=time_filter, limit=limit)

        post_list = []
        for post in posts:
            post_list.append({
                'title': post.title,
                'score': post.score,
                'url': post.url,
                'created_utc': post.created_utc
            })

        print(f"✅ Successfully extracted {len(post_list)} posts from r/{subreddit}")
        return post_list

    except Exception as e:
        print(f"❌ Failed to extract posts from r/{subreddit}: {e}")
        return []
