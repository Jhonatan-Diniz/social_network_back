import requests


def test_likes():
    post_id = 1
    url = f'http://127.0.0.1:8087/posts/{post_id}/like'
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2FvQGdtYWlsLmNvbSIsImV4cCI6MTczMzg3MjMzNH0.-eqVTBCa49E_lUx_GIubK8x5XhlJEZVMAfbJRVB-nG8'

    res = requests.post(url, headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    })

    print(res.json())


test_likes()
