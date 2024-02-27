import requests

def get_cn_facts():
    api_url = 'https://api.api-ninjas.com/v1/chucknorris'
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
    if response.status_code == requests.codes.ok:
        print(response.text)
        return response.text
    else:
        print("Error:", response.status_code, response.text)