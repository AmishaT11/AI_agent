import json
import re

with open("agent/rules.json", "r") as file:
    RULES = json.load(file)

def analyze_test_file(file_path):
    """Analyzes a Kotlin test file for standards compliance."""
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    issues = []

    for req in RULES["must_include"]:
        if req not in content:
            issues.append(f"❌ Missing required import: `{req}`.")

    # Check if assertions are present
    if not any(keyword in content for keyword in RULES["should_contain"]):
        issues.append("⚠️ No assertions found! Use `assert` or `verify` to validate behavior.")

    # Check for discouraged patterns
    for pattern in RULES["avoid_patterns"]:
        print(f"Checking pattern: {pattern}")
        if re.search(pattern, content):
            issues.append(f"⚠️ Avoid using `{pattern}` in test cases.")

    return issues if issues else ["✅ Test file follows standards!"]

if __name__ == "__main__":
    import sys
    file_path = sys.argv[1]
    print("\n".join(analyze_test_file(file_path)))
