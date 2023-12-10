def send_data_to_backend(api_url, data):
    import requests
    response = requests.post(api_url, json=data)
    return response.json()

def fetch_data_from_url(url):
    import requests
    response = requests.get(url)
    return response.json()
