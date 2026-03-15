import requests

def fetch_data(url, params=None, timeout=10):
    """Fetches JSON from an endpoint and handles basic network failures."""
    try:
        res = requests.get(url, params=params, timeout=timeout)
        res.raise_for_status()
        return res.json()
        
    except requests.exceptions.RequestException as e:
        print(f"Request failed for {url}: {e}")
        return None

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/users"
    
    # Quick test
    data = fetch_data(api_url, params={"id": 1})
    
    if data:
        print(data[0].get("name"))
