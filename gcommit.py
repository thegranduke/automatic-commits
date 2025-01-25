import asyncio
import subprocess
import google.generativeai as genai
import sys
import os
from dotenv import load_dotenv
load_dotenv()

def get_git_diff():
    """Fetch the output of 'git diff'."""
    try:
        result = subprocess.run(["git", "diff", "--cached"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running 'git diff': {e.stderr}")
        sys.exit(1)

async def get_commit_message_from_gemini(diff):
    """Send the git diff to the Gemini API and get a commit message."""
    prompt = f"Generate a concise commit message based on this git diff:\n{diff}"
    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = await model.generate_content_async(f"{prompt}\n")
        return response.text.strip()
    except Exception as e:
        print(f"Error communicating with Gemini API: {e}")
        sys.exit(1)

async def main():
    # Step 1: Get the git diff output
    diff = get_git_diff()
    if not diff.strip():
        print("No changes detected in the git diff.")
        sys.exit(0)

    # Step 2: Send the diff to Gemini API for a commit message
    commit_message = await get_commit_message_from_gemini(diff)

    # Step 3: Print the git commit command
    print(f'git commit -m "{commit_message}"')

if __name__ == "__main__":
    asyncio.run(main())