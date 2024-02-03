import requests

def get_access_token(client_id, client_secret):
    url = 'https://api.ebay.com/identity/v1/oauth2/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json().get('access_token')

def search_ebay_items(search_query, access_token):
    url = f'https://api.ebay.com/buy/browse/v1/item_summary/search?q={search_query}'
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    response = requests.get(url, headers=headers)
    return response

def print_response(response):
    if response.status_code == 200:
        # Print the response content
        print(response.json())
    else:
        print(f'Error: {response.status_code}, {response.text}')

def main():
    # Replace 'YOUR_CLIENT_ID' and 'YOUR_CLIENT_SECRET' with your actual eBay API credentials
    client_id = 'HG-MyKeyset-SBX-ee5696659-a5219965'
    client_secret = 'SBX-e5696659da36-8ec0-4d90-91af-a8d3'
    search_query = 'shoes'

    # Get access token
    access_token = get_access_token(client_id, client_secret)

    # Search eBay items
    search_response = search_ebay_items(search_query, access_token)

    # Print the response
    print_response(search_response)

if __name__ == "__main__":
    main()