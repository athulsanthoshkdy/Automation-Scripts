import requests

def check_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} is reachable.")
        else:
            print(f"{url} returned status code {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"Error checking {url}: {e}")

check_url("https://www.example.com")
