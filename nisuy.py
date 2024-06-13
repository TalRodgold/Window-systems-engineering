import requests

url = 'http://localhost:5162/api/Foods'  # Using HTTP URL

response = requests.get(url, verify=False)

if response.status_code == 200:
    
    foods = response.json()
    print(foods)
else:
    print(f"Failed to retrieve foods: {response.status_code}")
