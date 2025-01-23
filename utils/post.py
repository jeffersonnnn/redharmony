import random
import logging
import time
import os
from dotenv import load_dotenv

from utils.helper import load_accounts, get_reddit_client, subreddit_valid, save_post, get_flairs
from utils.constant import generate_post_content, generate_post_title
from utils.vote import vote_post

load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

with open("accounts.json") as f:
    accounts = load_accounts()

def generate_posts():
    account = random.choice(accounts)
    username = os.getenv("REDDIT_USERNAME")
    logger.info(f"Select Account : {username}")
    
    reddit = get_reddit_client(account)
    
    if not reddit:
        logger.error(f"Skipping account {username} due to failed authentication.")
        return
    
    subreddit = random.choice(account["subreddits"])

    logger.info(f"Logged in as: Username:{reddit.user.me()}, Subreddit:{subreddit}")

    if not subreddit_valid(reddit, subreddit):
        logger.error(f"Skipping post: Subreddit '{subreddit}' is invalid or inaccessible.")
        return

    post_content = generate_post_content(account["prompt"], subreddit) 
    post_title = generate_post_title(post_content)

    try:
        create_post(reddit, username, subreddit, post_title, post_content)
        
    except Exception as e:
        logger.error(f"Error creating post: {e}")

def create_post(reddit, username, subreddit_name, title, content):
    try:
        subreddit = reddit.subreddit(subreddit_name)
        
        # Get available flairs
        flairs = get_flairs(reddit, subreddit_name)
        
        # If flairs exist, select the first one (most subreddits put Discussion/General first)
        flair_id = None
        if flairs:
            flair_id = flairs[0]["flair_id"]
            logger.info(f"Using flair: {flairs[0]['flair_text']}")
     
        # Submit post with flair if available
        post = subreddit.submit(title=title, selftext=content, flair_id=flair_id)
        save_post(post.id, username, subreddit_name, title)
        vote_post(post)
        time.sleep(random.randint(100, 200))

    except Exception as e:
        logger.error(f"Error posting to subreddit: {e}")