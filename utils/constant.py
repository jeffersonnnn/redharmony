import openai
from dotenv import load_dotenv
import os
import random
import re

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_post_content(prompt, subreddit, max_tokens=200):
    content_prompt = f"{prompt} Here's a tip for {subreddit} enthusiasts! Please ensure the post content feels natural and human-like with 4~5 sentences. Whenever I ask, please use different styles each time. I only need the post content"
    content = openAI_generate(content_prompt, max_tokens)
    content.replace('"', '')
    return content

def generate_post_title(post_content, max_tokens=200):
    title_prompt = f"Here's a {post_content}. Please ensure the post content feels natural and human-like. Whenever I ask, please use different styles each time. I only need the post title"
    title = openAI_generate(title_prompt, max_tokens)
    title.replace('"', '')
    return title

def generate_comment(prompt, post_context, max_tokens=150):
    combined_prompt = f"This is the prompt:\n\n{prompt}\n\n This is the post content:\n\n{post_context}\n\n Make the comment human-like."
    content = openAI_generate(combined_prompt, max_tokens)
    return content

def openAI_generate(prompt, max_tokens=150):
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-2024-11-20",  
            messages=[
                {"role": "system", "content": "You are an AI that helps with Reddit bot development."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,  
            max_tokens=max_tokens  
        )

        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating content: {e}")
        return None