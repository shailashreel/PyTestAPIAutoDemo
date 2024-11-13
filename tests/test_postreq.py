import requests

class ATestPostRequest:
    def test_post_request(self):
        #Req base URL
        base_url = "https://jsonplaceholder.typicode.com"
        #Req body
        request_body = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        
        #Send Req
        response = requests.post(f"{base_url}/posts", request_body)
        #Print Response
        print(response.json())

        #Asserting the response with expected values
        assert response.status_code == 201
        assert response.json()['userId'] == 1
        assert response.json()['id'] == 101
        assert response.json()['title'] == 'foo'
        assert response.json()['body'] == 'bar'
