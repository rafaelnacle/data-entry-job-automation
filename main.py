import requests
from bs4 import BeautifulSoup

# Scrape the links, address and price of the properties
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# Use zillow clone from app brewery
response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

all_links_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [link["href"] for link in all_links_elements]
print(f"We found {len(all_links)} links of properties listings in total: \n")
print(all_links)

all_addresses_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_addresses_elements]
print(f"\nCleaned {len(all_addresses)} addresses: ")
print(all_addresses)

all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]
print(f"\nCleaned {len(all_prices)} prices: ")
print(all_prices)