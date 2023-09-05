import jwt
from rest_framework.exceptions import AuthenticationFailed


def check_user(request):
    secret_key = 'secret'
    token = request.COOKIES.get('jwt')
    token = token.strip("b'")
    if not token:
        raise AuthenticationFailed("User not Authenticated")
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Token has expired")
    except jwt.DecodeError:
        raise AuthenticationFailed("Invalid token")
