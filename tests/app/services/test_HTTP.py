from app.services.HTTP import build_api_response

def test_status_200_OK():
    result = build_api_response(200)

    expected = ({'status': 'ok'}, 200)

    assert result == expected

def test_status_400_OK():
    result = build_api_response(400)

    expected = ({'status': 'Bad request'}, 400)

    assert result == expected

def test_status_404_OK():
    result = build_api_response(404)

    expected = ({'status': 'Not found'}, 404)

    assert result == expected

def test_status_201_OK():
    result = build_api_response(201)

    expected = ({'status': 'Created'}, 201)

    assert result == expected
