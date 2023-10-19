# News Email API Caller

## Overview

This Python script retrieves the latest news about a specific topic using the News API and sends an email containing the news articles to a specified email address. It provides a convenient way to stay updated on the latest developments in a particular field or area of interest.

## Features

- **News Retrieval**: Fetches the latest news articles from the News API based on a specified topic and date.

- **Email Notification**: Sends an email containing the news article titles, descriptions, and links to a specified email address.

## How It Works

1. Run the script `main.py`.

2. The script makes an API request to the News API, specifying the topic, date, and API key. It retrieves a list of articles.

3. It extracts the titles, descriptions, and URLs of the news articles.

4. The script compiles the information into an email message.

5. The email is sent to the specified recipient using the SMTP protocol via Gmail.

## Prerequisites

Before using this script, ensure you have the following:

- A News API key: You can obtain one from [News API](https://newsapi.org/).

- A Gmail account: To send emails using the Gmail SMTP server.

- Python 3.x installed on your system.

## Configuration

1. Obtain a News API key from [News API](https://newsapi.org/) and replace `"API_KEY"` with your actual API key in the `main.py` file.

2. Set the topic you want to fetch news about and the date (in the "YYYY-MM-DD" format) in the `main.py` file.

3. Configure your Gmail account by setting the `"SENDER_MAIL"` and providing your Gmail password as an environment variable named `"PASSWORD"` for security. Make sure to allow less secure apps to access your Gmail account.

4. Customize the email subject and content as needed in the `send_email` function in the `send_email.py` file.

## Notes

- This script retrieves the latest news articles from the News API, but you can further customize the API request by adjusting the parameters based on the [News API documentation](https://newsapi.org/docs).

- Ensure that you run the script with a working internet connection to access the News API.

- The email sender and recipient email addresses should be valid Gmail accounts.

- Be cautious when handling email credentials and API keys, and consider more secure methods for storing sensitive information in a production environment.

That's it! Use this script to receive email updates on the latest news in your chosen topic of interest.
