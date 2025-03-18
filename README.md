# GitHub Action: Kotlin Test Reviewer 🚀

## What is this?
This GitHub Action **automatically reviews Kotlin test files** in pull requests and **comments on missing assertions**.

## How It Works
1. When a **pull request** is created or updated, this action:
    - Finds Kotlin test files (`*.Test.kt`).
    - Checks if they contain **assertions** (`assert`, `verify`).
    - **Posts a comment** if assertions are missing.

## Setup Instructions
1. **Fork & Clone this repository**.
2. **Enable GitHub Actions** in your repo settings.
3. **Add a GitHub Secret**:
    - `GITHUB_TOKEN` → **Your GitHub API token**.
4. **Create a Pull Request** with test files.

## Example Comment
If assertions are missing, this action will comment:
> ⚠️ Warning: `src/test/kotlin/SampleTest.kt` contains no assertions! Add assertions for proper testing.

## Run Locally
```bash
export GITHUB_TOKEN="your_token_here"
python cli/test_checker.py .
