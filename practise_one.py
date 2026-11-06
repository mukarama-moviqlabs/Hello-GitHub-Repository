import requests

url = "https://jsonplaceholder.typicode.com/users/1"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()

        print("Name:", data["name"])
        print("Email:", data["email"])
        print("City:", data["address"]["city"])

    else:
        print("Request failed:", response.status_code)

except requests.exceptions.RequestException as error:
    print("An error occurred:", error)