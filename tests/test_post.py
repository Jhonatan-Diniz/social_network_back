import requests


def test_post_message():
    url = 'http://127.0.0.1:8087/posts/create_post'
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjYXJsb3NAZ21haWwuY29tIiwiZXhwIjoxNzMzNzkyMTcxfQ.ZrniDkn7rvotaqkpUSmMjWqt0m2RMaiyICebDJLdmnA'

    message = 'Mensagem test user 2'

    body = {
            'message': message
            }

    resp = requests.post(url, json=body, headers={
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
        })

    print(resp)


test_post_message()
