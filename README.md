# 📊 Reddit Data Pipeline with Apache Airflow

This project is an **ETL (Extract, Transform, Load) data pipeline** built using **Apache Airflow** and the **Reddit API**. It extracts top posts from a specified subreddit, processes them, and saves them as a **CSV file**.

## 🚀 Features
- **Extract** 🔍: Fetches top Reddit posts using the Reddit API.
- **Transform** 🔄: Cleans and processes the extracted data.
- **Load** 💾: Saves the data as a CSV file.

## ⚙️ Tech Stack
- **Apache Airflow** 🛠️ (Task automation)
- **Python** 🐍 (Data processing)
- **Reddit API (PRAW)** 🔗 (Data extraction)
- **Docker** 🐳 (Containerized setup)
- **PostgreSQL** 🗄️ (Airflow metadata storage)
- **Redis**  (Task queue for CeleryExecutor)
- **AWS S3 (Future Enhancement)** ☁️ (For cloud storage)

# Reddit API Credentials
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=your_user_agent
REDDIT_USERNAME=your_username
REDDIT_PASSWORD=your_password

# Database Credentials
POSTGRES_USER=airflow
POSTGRES_PASSWORD=airflow

