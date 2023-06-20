import requests

# API endpoint URL
url = 'https://api.the-odds-api.com/v4/sports/{sport}/odds/'

# Your API key from the-odds-api.com
api_key = '92a38521dcc275a6d061cca8f46c8b77'

# Query parameters
params = {
    'apiKey': api_key,
    'regions': 'us',
    'markets': 'h2h,spreads',
    'sport': 'americanfootball_nfl'
}

# Make a GET request to the Odds API
response = requests.get(url.format(sport=params['sport']), params=params)

# Check the response status code
print('Response Code:', response.status_code)

# Print the response content
print('Response Content:')
print(response.json())
