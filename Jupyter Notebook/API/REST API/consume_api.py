import requests
import json

#python -m venv myenv
#myenv\Scripts\activate
#pip install requests
#pip install flask
#pip install flask-sqlalchemy
#API>pip freeze > requirements.txt


response = requests.get(
    'https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

#rint(response)
#print(response.json()['items'])




for data in response.json()['items']:
    if data['answer_count'] == 0:
        print(data['title'])
        print(data['link'])
    else:
        print("skipped")
    print()