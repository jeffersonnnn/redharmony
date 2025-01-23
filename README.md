# Reddit AI Bot

A powerful Reddit bot that uses artificial intelligence to interact with posts and comments on Reddit. This bot can analyze sentiment, generate responses, and perform automated actions based on configured triggers.

## Features

- Automated comment responses using AI
- Sentiment analysis of posts and comments
- Customizable trigger keywords
- Rate limiting to comply with Reddit's API rules
- Detailed logging system
- Multiple subreddit support
- Command handling system

## Prerequisites

- Python 3.8 or higher
- Reddit account
- Reddit API credentials
- OpenAI API credentials

## Installation

1. Clone the repository:
```bash
git clone https://github.com/amfuming/reddit-ai-social-simulacra.git
```
2. Navigate to the project directory:
```bash
cd reddit-ai-social-simulacra
```
3. Create Python virtual environment and activate:
```bash
python -m venv venv
```
Linux/MacOS:
```bash:linux/macos
source venv/bin/activate
```
Windows:
```command:windows
venv\Script\activate
```
4. Install required dependencies:
```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the root directory with your OpenAI API credentials:

```python:.env
OPENAI_API_KEY="<your_openai_api_key>"
```

6. Create a `accounts.json` file in the root directory with your Reddit accounts:
```json:accounts.json
[
    {
        "username": "reddit_username",
        "password": "reddit_password",
        "client_id": "client_id",
        "client_secret": "client_secret",
        "user_agent": "script:your-bot:v1.0 (by u/reddit_username)",
        "subreddits": ["lofimusic", "skateboarding", "latteart"],
        "prompt": "You are Aberra Truder, a 24-year-old barista who dreams of ... your prompt"
    },
    ...
]
```

## Usage
1. Start the bot:
```bash
python main.py
```
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Reddit API Documentation
- PRAW (Python Reddit API Wrapper)
- OpenAI GPT for response generation
- Contributors and community members

## Support

For support, please:
1. Check existing issues
2. Create a new issue with detailed description
3. Join our Discord community


## Development Roadmap

- [ ] Multi-language support
- [ ] Advanced AI model integration
- [ ] Web dashboard
- [ ] Custom plugin system
- [ ] Analytics dashboard

Remember to check Reddit's API Terms of Service and bot guidelines before deployment.
