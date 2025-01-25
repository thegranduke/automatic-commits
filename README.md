# 🚀 gcommit: AI-Powered Git Commit Messages

## Overview

`gcommit` is an innovative Python tool that leverages Google's Gemini AI to automatically generate intelligent, context-aware commit messages. Say goodbye to writer's block and inconsistent commit descriptions!

## 🌟 Features

- **AI-Powered Commit Messages**: Uses Gemini AI to analyze git diffs
- **Seamless Integration**: Works directly with your existing Git workflow
- **Async Performance**: Lightweight and fast async implementation
- **Easy Setup**: Simple installation and configuration

## 📦 Prerequisites

- Python 3.8+
- Git
- Google Gemini API Key

## 🛠 Installation

1. Clone the repository:

```bash
git clone <https://github.com/yourusername/gcommit.git>
cd gcommit

```

1. Install dependencies:

```bash
pip install -r requirements.txt

```

1. Set up your Gemini API Key:
- Create a `.env` file
- Add `GEMINI_API_KEY=your_api_key_here`

## 🚀 Usage

```bash
# Stage your changes
git add .

# Generate commit message
gcommit

```

## 🔧 How It Works

1. Captures staged git changes
2. Sends diff to Gemini AI
3. Generates a concise, meaningful commit message
4. Provides git commit command

## 🤝 Contributing

Contributions welcome!

- Fork the repository
- Create your feature branch
- Commit your changes
- Push to the branch
- Create a Pull Request

## 🛡 Limitations

- Requires internet connection
- Quality of commit message depends on AI model
- API usage may incur costs

## 📄 License

[Your Chosen License - e.g., MIT]

## 🌈 Motivation

Developed to streamline developer workflow and improve commit message quality using cutting-edge AI technology.

## 📞 Support

Open an issue on GitHub for any questions or problems.

---

**Made with ❤️ by [Your Name]**