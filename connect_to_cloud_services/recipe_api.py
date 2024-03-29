import requests
from functools import reduce
import json
import re

url = "https://edamam-recipe-search.p.rapidapi.com/api/recipes/v2"

querystring = {"type":"public","co2EmissionsClass":"A+","field[0]":"uri","q":"\"milk\", \"banana\"","beta":"true","random":"true"}

headers = {
	"Accept-Language": "en",
	"X-RapidAPI-Key": "e4cb194fedmsh8f5e57ba5fc557cp16248ajsn0d64d197f11a",
	"X-RapidAPI-Host": "edamam-recipe-search.p.rapidapi.com"
}

try:
    # Sending POST request to edamam-recipe-search API
    response = requests.get(url, headers=headers, params=querystring)

    # Checking if the request was successful
    if response.status_code == 200:
        j = json.loads(response.text)
        l = []
        for item in j['hits']:
            l.append(item['recipe']['url'])
        print([print(i) for i in l])
    else:
        print("Error:", response.status_code, response.text)
except Exception as e:
    print("Error occurred:", str(e))

def user_input(unparsed_str: str) -> str:

    try:
        split_list = re.split("[ ,]", unparsed_str)
    
        for string in split_list:
            if not string.isalpha():
                raise ValueError(f"String '{string}' contains non-letter characters.")
        return reduce(lambda x,y: x + ", " + y, split_list) 
    except ValueError as e:
        print(f"Error: {e}")

