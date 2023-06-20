import requests

# API endpoint URL
url = 'https://api.the-odds-api.com/v4/sports/basketball_nba/scores/'

# Your API key from the-odds-api.com
api_key = '92a38521dcc275a6d061cca8f46c8b77'

# Query parameters
params = {
    'daysFrom': 1,
    'apiKey': api_key
}

# Make a GET request to the Odds API
response = requests.get(url, params=params)

# Check the response status code
print('Response Code:', response.status_code)

# Access the information from the response
data = response.json()

# Iterate over the data and print relevant information
for game in data:
    print('Game ID:', game['id'])
    print('Sport:', game['sport_title'])
    print('Home Team:', game['home_team'])
    print('Away Team:', game['away_team'])
    print('Scores:')
    for score in game['scores']:
        print(score['name'], ':', score['score'])
    print('Last Update:', game['last_update'])
    print('---------------------------')
