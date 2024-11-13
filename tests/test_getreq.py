import requests

class TestGetRequest:
    def test_get_req(self):
        base_url = "https://jsonplaceholder.typicode.com"
        
        #Sending the request and saving the response
        response = requests.get(f"{base_url}/posts/1")
        #Print Response
        print(response.json())

        #Asserting the response data with expected values
        assert response.status_code == 200
        assert response.json()['userId'] == 1
        assert response.json()['id'] == 1


