import time
import random

from utils.database import initialize_db
from utils.post import generate_posts
from utils.comment import generate_comments
from datetime import datetime, timedelta

def main():
    print("Starting Reddit Bot...")

    initialize_db()
    if initialize_db():
        print("Database connection is working!")
    else:
        print("Database connection failed. Check your setup.")

    daily_post_limit = 20
    daily_comment_limit = 100
    hourly_post_limit = 2
    hourly_comment_limit = 5

    posts_created = 0
    comments_created = 0

    while posts_created < daily_post_limit or comments_created < daily_comment_limit:
        start_time = datetime.now()

        for _ in range(hourly_post_limit):
            if posts_created >= daily_post_limit:
                break
            generate_posts()
            posts_created += 1

        time.sleep(random.randint(10, 20))

        for _ in range(hourly_comment_limit):
            if comments_created >= daily_comment_limit:
                break
            generate_comments()
            comments_created += 1

        elapsed_time = datetime.now() - start_time
        if elapsed_time < timedelta(hours=1):
            time.sleep((timedelta(hours=1) - elapsed_time).seconds)    

    print("Daily task completed.")

if __name__ == "__main__":
    main()
