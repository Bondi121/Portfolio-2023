
#python -m venv myenv
#myenv\Scripts\activate
#https://www.askpython.com/python/examples/connect-and-call-apis


import requests

# Make a GET request to the API URL
response_API = requests.get('https://www.askpython.com/')

print('Response Code:', response_API.status_code)




response = requests.get('https://www.askpython.com/')

# Check the response status code
print('Response Code:', response.status_code)

# Extract and print the response content
#print('Response Content:')
#print(response.text)



# Check the response status code
print('Response Code:', response.status_code)

# Print specific response headers
print('Response Headers:')
print('Content-Type:', response.headers.get('Content-Type'))
print('Server:', response.headers.get('Server'))


# API endpoint URL
url = 'https://www.askpython.com/search'

# Query parameters
params = {'q': 'python', 'page': 1}

# Make a GET request with query parameters
response = requests.get(url, params=params)

# Check the response status code
print('Response Code:', response.status_code)
