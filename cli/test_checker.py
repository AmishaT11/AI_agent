import sys
from agent.analyzer import analyze_test_file

if len(sys.argv) < 2:
    print("Usage: python cli/test_checker.py <test_file1> <test_file2> ...")
    sys.exit(1)

for file_path in sys.argv[1:]:
    issues = analyze_test_file(file_path)
    print(f"🔍 Review for {file_path}:")
    print("\n".join(issues))
    print("-" * 50)  # Separator for readability
