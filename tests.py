from script import response_created_date, response_reading_time, response_status

def test_response_created_date():
    assert response_created_date() == '2025-12-05T10:21:01.037478+03:00'

def test_response_reading_time():
    assert response_reading_time() == 5

def test_invalid_reading_time():
    assert response_reading_time() == 5

def test_response_status():
    assert response_status() == 20