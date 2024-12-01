import requests


def test_post_message():
    url = 'http://127.0.0.1:8080/posts/create_post'
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2FvQGdtYWlsLmNvbSIsImV4cCI6MTczMzA4NzY5MH0.tNJk86M3GG1MAN-ZuY1us_wCcboZY9S7Y_8OJ66fNtI'
    message = 'ola mundo'

    body = {
            'message': message
            }

    resp = requests.post(url, json=body, headers={
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
        })

    print(resp)


test_post_message()
