import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response=requests.get(self.url)
        return response.content

    def load_json(self):
        data=[]
        all_data=json.loads(self.get_response_body())
        for datum in all_data:
            data.append(datum)
        return data
    
get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
information=get_requester.load_json()
print(information)
