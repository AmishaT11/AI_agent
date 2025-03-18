def generate_comment(file_path, issues):
    """Generates a structured PR comment based on analysis."""
    if not issues:
        return f"✅ `{file_path}` follows all coding standards!"

    comment = f"🚨 Issues detected in `{file_path}`:\n"
    for issue in issues:
        comment += f"- {issue}\n"

    comment += "\n💡 Please update the test to follow the standards."
    return comment
