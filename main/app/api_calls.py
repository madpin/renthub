import requests

try:
    response = requests.get('http://daft:8000/search_result')
    response.raise_for_status()
    # Additional code will only run if the request is successful
except requests.exceptions.HTTPError as error:
    print(error)