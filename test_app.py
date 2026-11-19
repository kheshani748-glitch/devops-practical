from app import app

def test_home ():
    client = app.test_client()
    responce = client.get('/')
    assert responce.status_code ==200
    assert b"Hello, DevOps World! V1" in responce.data