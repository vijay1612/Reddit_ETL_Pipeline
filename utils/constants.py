import configparser
import os

# Load the config file
parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf'))

# Reddit API Keys
REDDIT_SECRET_KEY = parser.get('api_keys', 'reddit_secret_key')
REDDIT_CLIENT_ID = parser.get('api_keys', 'reddit_client_id')

# Database (Postgres) Config
DATABASE_HOST = parser.get('database', 'database_host')
DATABASE_NAME = parser.get('database', 'database_name')
DATABASE_PORT = parser.get('database', 'database_port')
DATABASE_USERNAME = parser.get('database', 'database_username')
DATABASE_PASSWORD = parser.get('database', 'database_password')

# AWS Credentials
AWS_ACCESS_KEY_ID = parser.get('aws', 'aws_access_key_id')
AWS_SECRET_ACCESS_KEY = parser.get('aws', 'aws_secret_access_key')
AWS_SESSION_TOKEN = parser.get('aws', 'aws_session_token')
AWS_REGION = parser.get('aws', 'aws_region')
AWS_BUCKET_NAME = parser.get('aws', 'aws_bucket_name')

# File Paths
INPUT_PATH = parser.get('file_paths', 'input_path')
OUTPUT_PATH = parser.get('file_paths', 'output_path')

# ETL Settings
BATCH_SIZE = parser.getint('etl_settings', 'batch_size')
ERROR_HANDLING = parser.get('etl_settings', 'error_handling')
LOG_LEVEL = parser.get('etl_settings', 'log_level')