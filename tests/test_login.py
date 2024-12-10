import requests


def test_login():
    url = 'http://127.0.0.1:8087/users/login'
    data = {
            'email': 'carlos@gmail.com',
            'password': '1234'
    }

    req = requests.post(url, json=data, headers={
        'Content-Type': 'application/json'
    })

    print(req.json())


test_login()
