import requests

response = requests.get('https://reg.lectonic.skroy.ru/api/content/adbf2f39-a665-4cc6-ac06-3baae556fa6a')

# assert response.status_code == 404

def response_created_date():
    return response.json()['created_date']


def response_reading_time():
    return response.json()['data']['reading_time']


print(response.json())