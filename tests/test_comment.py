import requests


def test_comments():
    post_id = 1
    url = f'http://127.0.0.1:8087/posts/{post_id}/comment'
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2FvQGdtYWlsLmNvbSIsImV4cCI6MTczMzg4MDE3OH0.c33AhUC_r-1m6LRnmI9WfSnQrqyfPXJuhzHGjA8FhF4'

    data = {
        'message': 'comentario teste 1'
    }

    res = requests.post(url, json=data, headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    })

    print(res.json())


test_comments()
