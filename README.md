# SocialButterfly

This project was made in Collaboration with Juliana Unger in summer 2024 at Florida Atlantic University


Social Butterfly is a Python-based tool designed to empower users with the ability to collect, analyze, and derive insights from social media data, specifically from Twitter (X) and Reddit platforms. This project leverages the Tweepy and PRAW libraries for API interactions, providing advanced search capabilities, efficient data collection, sophisticated analysis tools, and customizable report generation.

Table of Contents
Overview
Installation
Usage
Testing
Contributing
License
Overview
Social Butterfly is intended to be a comprehensive tool for social media data analysis. The core functionalities include:

Data Retrieval: Fetch data from Twitter and Reddit using Tweepy and PRAW libraries.
Data Storage: Store the retrieved data in a structured format.
Data Analysis: Analyze the collected data to provide insights such as sentiment analysis and trend identification.
Reporting: Generate customizable reports in various formats (e.g., PDF, CSV).
User Interface: An intuitive interface for searching, analyzing, and reporting data.
Installation
Prerequisites
Python 3.7 or higher
Tweepy library
PRAW library
Additional libraries as listed in requirements.txt****************************************<-----------------------------



Usage
Running the Application
Start the application:

bash
Copy code
python main.py
Using the Interface:

Search Interface: Enter keywords, select options like date range and social media site, and click the search button.
Report Generation Interface: Choose the format and type of report, and click the generate button to create the report.
Example
To fetch Twitter data with specific parameters:

python
Copy code
from data_retrieval import fetch_twitter_data

tweets = fetch_twitter_data(query="Python", count=100, lang="en", result_type="recent", since_id=None, max_id=None)
for tweet in tweets:
    print(tweet)
Testing
Running Tests
To ensure the quality and functionality of Social Butterfly, we have provided a comprehensive test suite. To run the tests:

Install testing dependencies:

bash
Copy code
pip install -r requirements-test.txt
Execute the test cases:

bash
Copy code
pytest tests/
Test Plan
Refer to the Software Test Document for detailed information on our testing strategy, objectives, test cases, and more.

Contributing
We welcome contributions from the community. To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature-name).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/your-feature-name).
Create a new Pull Request.

