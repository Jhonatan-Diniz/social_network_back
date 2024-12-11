import requests


def test_post_message():
    url = 'http://127.0.0.1:8087/posts/create_post'
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2FvQGdtYWlsLmNvbSIsImV4cCI6MTczMzg4MDE3OH0.c33AhUC_r-1m6LRnmI9WfSnQrqyfPXJuhzHGjA8FhF4'

    message = 'first message test user id 1'

    body = {
            'message': message
            }

    resp = requests.post(url, json=body, headers={
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
        })

    print(resp)


test_post_message()
