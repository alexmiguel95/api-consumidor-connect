from http import HTTPStatus


def build_api_response(http_status) -> tuple:
    return build_response_message(http_status), http_status


def build_response_message(http_status):
    messages = {
        HTTPStatus.BAD_REQUEST: 'Bad request',
        HTTPStatus.CREATED: 'Created',
        HTTPStatus.NOT_FOUND: 'Not found',
        HTTPStatus.OK: 'Ok',
        HTTPStatus.UNAUTHORIZED: "Unauthorized - Invalid email or password",
        HTTPStatus.CONFLICT: "Conflict - Email already exists"
    }

    return {'status': messages[http_status]}
