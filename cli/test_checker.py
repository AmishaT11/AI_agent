import sys
import os

# Ensure the script can find the 'agent' module
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

from agent.analyzer import analyze_test_file  # Import after adjusting sys.path

if len(sys.argv) < 2:
    print("Usage: python cli/test_checker.py <test_file1> <test_file2> ...")
    sys.exit(1)

for file_path in sys.argv[1:]:
    issues = analyze_test_file(file_path)
    print(f"🔍 Review for {file_path}:")
    print("\n".join(issues))
    print("-" * 50)  # Separator for readability
