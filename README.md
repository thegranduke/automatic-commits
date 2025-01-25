# 🚀 gcommit: AI-Powered Git Commit Messages

## Overview

`gcommit` is a Python script that leverages Google's Gemini AI to automatically generate intelligent, context-aware commit messages. No more mental tax when trying to create commit messages.

## 🌟 Features

- **AI generated Commit Messages**: Uses Gemini AI to analyze git diffs
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
python gcommit.py

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


## 🌈 Motivation

Developed to make developer workflow easier and improve commit message quality by ensuring its context-aware.

**Made with ❤️ by thegranduke**