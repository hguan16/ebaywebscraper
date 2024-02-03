import requests
from bs4 import BeautifulSoup

def get_recent_prices():
    ebay_url = "https://www.ebay.com/sch/i.html?_nkw=apple+vision+pro&LH_Complete=1&LH_Sold=1&_sop=12"
    
    # Send a GET request to the eBay website
    response = requests.get(ebay_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract information about the sold items
        sold_items = soup.find_all('div', class_='s-item__info')

        # Extract and print information about the most recently sold items
        for item in sold_items:
            title_elem = item.find('div', class_='s-item__title')
            price_elem = item.find('span', class_='s-item__price')

            # Check if both title and price elements are found
            if title_elem and price_elem:
                title = title_elem.find('span').text.strip()
                price = price_elem.text.strip()
                print(f"Title: {title}, Price: {price}")

    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

# Call the function to get recent prices
get_recent_prices()
