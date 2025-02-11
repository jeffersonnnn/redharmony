# RedHarmony

RedHarmony is an innovative social media orchestration system that creates engaging, multi-personality discussions and interactions on Reddit. It uses artificial intelligence to simulate natural conversations between distinct personas, each with their own expertise, viewpoints, and communication styles in the cryptocurrency and DeFi space.

## Current Personalities

The system currently features three distinct personalities:

1. **fxnction** - A seasoned crypto trader and DeFi expert focusing on market psychology and technical analysis
2. **defi_skeptic** - An experienced traditional finance professional who brings critical analysis to DeFi claims
3. **crypto_researcher** - An academic researcher focused on blockchain economics and empirical analysis

## Core Features

- **Personality-Driven Interactions**: Each personality maintains its unique voice, expertise, and perspective throughout discussions
- **Natural Conversation Flow**: Generates contextual, flowing discussions without mechanical numbering or rigid structures
- **Signature System**: Clear attribution of posts and comments to specific personalities with their roles
- **Dynamic Flair Management**: Automatically selects appropriate post flairs based on content and subreddit
- **Intelligent Rate Limiting**: Respects Reddit's API guidelines while maintaining natural posting patterns
- **Contextual Responses**: Each personality engages thoughtfully with posts and comments, maintaining conversation coherence

## Configuration

### Personality Files
Located in `/personalities/` directory:
- `fxnction.json`
- `defi_skeptic.json`
- `crypto_researcher.json`

Each personality file contains:
- Detailed bio and background
- Knowledge areas and expertise
- Communication style preferences
- Example messages and posts
- Characteristic adjectives

### Central Configuration
`config.json` manages:
- Target subreddits
- Rate limits
- Interaction settings
- Conversation depth
- Post frequency

## Prerequisites

- Python 3.8 or higher
- Reddit account with API access
- OpenAI API key (GPT-4 access)
- SQLite (included with Python)

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

4. Configure your `.env` file with API credentials:
```env
# AI Provider Configuration
USE_DEEPSEEK="False"  # Set to "True" to use DeepSeek instead of OpenAI

# OpenAI Configuration
OPENAI_API_KEY="your_openai_api_key"

# Reddit Configuration
REDDIT_USERNAME="your_username"
REDDIT_PASSWORD="your_password"
REDDIT_CLIENT_ID="your_client_id"
REDDIT_CLIENT_SECRET="your_client_secret"
REDDIT_USER_AGENT="script:redharmony:v1.0 (by u/your_username)"
```

## Usage

1. Start the system:
```bash
python main.py
```

The system will:
- Load configured personalities
- Connect to target subreddits
- Generate natural posts and comments
- Maintain conversation threads
- Log all activities

## Current Rate Limits

Default settings in `config.json`:
- 10 posts per day
- 50 comments per day
- 2 posts per hour
- 5 comments per hour
- 20-40 seconds between actions

## Interaction Flow

1. **Post Creation**:
   - Random personality selection
   - Natural title generation
   - Content creation with personality signature
   - Automatic flair selection

2. **Comment Generation**:
   - Contextual response generation
   - Personality-appropriate insights
   - Natural conversation flow
   - Clear attribution

3. **Reply Chains**:
   - Organic discussion development
   - Contrasting viewpoint integration
   - Maintained personality consistency
   - Natural conversation progression

## Best Practices

1. Monitor interactions for quality and authenticity
2. Regularly review personality configurations
3. Adjust rate limits based on community response
4. Keep conversation flows natural and engaging
5. Respect subreddit-specific guidelines

## Development Status

Current focus areas:
- [x] Multi-personality system implementation
- [x] Natural conversation flow
- [x] Personality-specific content generation
- [x] Dynamic flair management
- [x] Rate limiting and timing controls
- [ ] Advanced conversation branching
- [ ] Personality memory system
- [ ] Analytics dashboard

## Troubleshooting

Common issues and solutions:
1. Rate limit errors: Check `config.json` timing settings
2. Authentication failures: Verify Reddit API credentials
3. Database errors: Ensure proper SQLite setup
4. Content generation issues: Check OpenAI API key and quota

## Security Note

Never commit sensitive credentials to the repository. Always use environment variables for API keys and authentication details. The `.env` file is automatically ignored by git to prevent accidental exposure of credentials.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Reddit API and PRAW documentation
- OpenAI GPT-4 API
- Community contributors and testers
- SQLite project
