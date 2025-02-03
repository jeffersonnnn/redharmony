# RedHarmony

RedHarmony is an innovative social media orchestration system that creates engaging, multi-personality discussions and interactions on Reddit. It uses artificial intelligence to simulate natural conversations between multiple personas, each with their own unique characteristics, viewpoints, and communication styles.

## Core Features

- **Multi-Personality System**: Create and manage multiple AI personas, each with distinct traits, backgrounds, and communication patterns
- **Natural Interaction Flow**: Generates contextually appropriate posts and comments that maintain conversation coherence
- **Flexible LLM Integration**: Supports both OpenAI and DeepSeek with seamless provider switching
- **Subreddit Targeting**: Deploy personas across chosen subreddits or create dedicated discussion spaces
- **Smart Rate Limiting**: Complies with Reddit's API guidelines through intelligent timing controls
- **Conversation Threading**: Maintains coherent discussion threads between different personas
- **Automated Engagement**: Handles post creation, commenting, and voting with natural timing
- **Detailed Activity Tracking**: Logs all interactions in a local database for analysis

## Prerequisites

- Python 3.8 or higher
- Reddit account with API access
- OpenAI API key (GPT-4 access) or DeepSeek API key
- SQLite (included with Python)

## LLM Provider Configuration

RedHarmony supports two AI providers:

### OpenAI (Default)
- Uses GPT-4 for state-of-the-art language understanding
- Requires OpenAI API key with GPT-4 access
- Set `OPENAI_API_KEY` in your `.env` file

### DeepSeek (Alternative)
- Cost-effective alternative with similar performance
- Requires DeepSeek API key
- Set `DEEPSEEK_API_KEY` and `USE_DEEPSEEK=True` in your `.env` file

You can easily switch between providers by updating your environment variables.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/redharmony.git
cd redharmony
```

2. Create and activate Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy `.env.example` to `.env` and configure your credentials:
```bash
cp .env.example .env
```
Then edit `.env` with your API credentials:
```env
# Choose your AI provider
USE_DEEPSEEK="False"  # Set to "True" to use DeepSeek instead of OpenAI

# OpenAI Configuration (Default)
OPENAI_API_KEY="your_openai_api_key"

# DeepSeek Configuration (Optional)
DEEPSEEK_API_KEY="your_deepseek_api_key"

# Reddit Configuration
REDDIT_USERNAME="your_username"
REDDIT_PASSWORD="your_password"
REDDIT_CLIENT_ID="your_client_id"
REDDIT_CLIENT_SECRET="your_client_secret"
REDDIT_USER_AGENT="script:redharmony:v1.0 (by u/your_username)"
```

5. Configure your personas in `accounts.json`:
```json
[
    {
        "subreddits": ["subreddit1", "subreddit2"],
        "prompt": "You are [personality description]..."
    }
]
```

## Usage

1. Start the system:
```bash
python main.py
```

2. Monitor the console for activity logs and interaction details.

3. View your Reddit profile to see the interactions:
```
https://www.reddit.com/user/your_username
```

## Rate Limits

RedHarmony respects Reddit's API guidelines with the following default limits:
- 20 posts per day
- 100 comments per day
- 2 posts per hour
- 5 comments per hour

These limits can be adjusted in `main.py`.

## Personality Configuration

Each persona can be configured with:
- Target subreddits
- Personality traits and background
- Communication style
- Knowledge areas and interests
- Response patterns

Example persona configurations:

1. Aviation Expert:
```json
{
    "subreddits": ["aviation", "flying"],
    "prompt": "You are a veteran commercial pilot with 30 years of experience. You enjoy sharing technical knowledge about aircraft systems and flight procedures, while maintaining a professional yet approachable tone. You often reference your real-world flying experiences..."
}
```

2. TV Show Fan:
```json
{
    "subreddits": ["brooklynninenine", "television"],
    "prompt": "You are an enthusiastic fan of Brooklyn Nine-Nine and similar shows. You have watched every episode multiple times and love discussing character development, plot details, and behind-the-scenes facts. Your tone is casual and friendly, often incorporating relevant quotes from the show..."
}
```

3. Tech Professional:
```json
{
    "subreddits": ["programming", "python", "coding"],
    "prompt": "You are a senior software engineer with expertise in Python and web development. You provide detailed, helpful responses to technical questions, share best practices, and occasionally mentor newcomers. Your communication style is clear and structured..."
}
```

## Development Roadmap

- [ ] Advanced personality memory system
- [ ] Dynamic conversation branching
- [ ] Sentiment analysis integration
- [ ] Web dashboard for monitoring
- [ ] Automated personality generation
- [ ] Cross-platform support
- [ ] Multi-account support
- [ ] Conversation analytics
- [ ] Custom personality templates

## Best Practices

1. Always follow Reddit's terms of service and API guidelines
2. Create meaningful, value-adding interactions
3. Be transparent about automated content when required
4. Respect community guidelines of target subreddits
5. Monitor interactions for quality and appropriateness
6. Regularly review and update persona configurations
7. Keep interaction frequencies natural and varied
8. Maintain backup of your database

## Troubleshooting

Common issues and solutions:
1. Rate limit errors: Adjust timing in `main.py`
2. Authentication failures: Check Reddit API credentials
3. Database errors: Ensure write permissions in directory
4. OpenAI API errors: Verify API key and quota

## Support

For support:
1. Check existing issues in the repository
2. Create a detailed new issue
3. Join our community Discord
4. Check the troubleshooting guide

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Reddit API and PRAW documentation
- OpenAI GPT-4 API
- Community contributors and testers
- SQLite project

## Security Note

Never commit sensitive credentials to the repository. Always use environment variables for API keys and authentication details. The `.env` file is automatically ignored by git to prevent accidental exposure of credentials.
