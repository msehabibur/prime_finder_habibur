from setuptools import setup, find_packages

setup(
    name="prime_finder",  # Package name
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple Python package to check if a number is prime.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/msehabibur/prime_finder_habibur",  # Replace with your GitHub repo URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
