from app.services.http import build_api_response


def test_status_200_OK():
    result = build_api_response(200)

    expected = ({'status': 'Ok'}, 200)

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


def test_status_401_OK():
    result = build_api_response(401)

    expected = ({'status': 'Unauthorized - Invalid email or password'}, 401)

    assert result == expected


def test_status_409_OK():
    result = build_api_response(409)

    expected = ({'status': 'Conflict - Email already exists'}, 409)

    assert result == expected
