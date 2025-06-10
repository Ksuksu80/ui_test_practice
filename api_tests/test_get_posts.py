import requests

# to check that response gets: 200 code, the body is not empty, fields in json
def test_get_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200
    assert response.json() != []
    assert "userId" in response.json()[0]
    print(response.json())
    print("GET Posts API test passed!")

