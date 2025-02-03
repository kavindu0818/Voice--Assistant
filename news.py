from ss import *

api_address ="https://newsapi.org/v2/top-headlines?country=us&apiKey=" + key
json_data = requests.get(api_address).json()

def news():
    for i in range(3):
        