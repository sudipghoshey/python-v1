import requests
import json

# Fetch data from free API
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    with open("raw_data.json", "w") as f:
        json.dump(data, f)
    print("Data fetched successfully!" + f)
else:
    print(f"Error: {response.status_code}")
