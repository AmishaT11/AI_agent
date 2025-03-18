from setuptools import setup, find_packages

setup(
    name="test-review-agent",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "requests",
        "openai",
        "PyGithub"
    ],
    entry_points={
        "console_scripts": [
            "test-checker=cli.test_checker:main"
        ]
    }
)
