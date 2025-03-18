import os
import requests
from agent.analyzer import analyze_test_file
from agent.comment_generator import generate_comment

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPOSITORY = os.getenv("GITHUB_REPOSITORY")
PR_NUMBER = os.getenv("PR_NUMBER")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_changed_test_files():
    """Fetch changed Kotlin test files in the PR."""
    api_url = f"https://api.github.com/repos/{GITHUB_REPOSITORY}/pulls/{PR_NUMBER}/files"
    response = requests.get(api_url, headers=headers)

    if response.status_code != 200:
        print(f"❌ Failed to fetch PR files: {response.json()}")
        return []

    files = response.json()
    return [f["filename"] for f in files if f["filename"].endswith(".kt")]

def post_review_comment(file_path):
    """Analyze test file with LLM and post a GitHub comment."""
    issues = analyze_test_file(file_path)
    comment = generate_comment(file_path, issues)

    api_url = f"https://api.github.com/repos/{GITHUB_REPOSITORY}/issues/{PR_NUMBER}/comments"
    response = requests.post(api_url, json={"body": comment}, headers=headers)

    if response.status_code == 201:
        print(f"✅ Successfully posted review comment for {file_path}")
    else:
        print(f"❌ Failed to post comment: {response.json()}")

if __name__ == "__main__":
    test_files = get_changed_test_files()
    if not test_files:
        print("⚠️ No Kotlin test files changed in this PR.")

    for file in test_files:
        post_review_comment(file)
