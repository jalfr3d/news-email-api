import requests
from send_email import send_email


topic = "cryptocurrencies"
date = "2023-04-22"
api_key = "API_KEY"
# More parameters in de newsapi documentation
url = "https://newsapi.org/v2/everything?"\
      f"q={topic}&" \
      f"from={date}&sortBy=publishedAt&apiKey=" \
      "ee26a25870b74596acec352dab18a49d&language=en"

# Make request
request = requests.get(url)
# get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" \
               + article["description"] \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
# "Subject: Today's News" + "\n" +
