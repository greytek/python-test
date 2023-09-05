import datetime
import jwt
from django.contrib.auth import authenticate, login, logout
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users.models import User
from users.serializer import UserSerializer
from wiremi.permissions import IsAuthenticated, IsCustomer
from wiremi.utils import check_user


@swagger_auto_schema(
    tags=['User Modal'],
    method='post',
    operation_description="This endpoint requires the IsUser permission.",
    request_body=UserSerializer,
    responses={201: UserSerializer()}
)
@swagger_auto_schema(
    tags=['User Modal'],
    method='put',
    operation_description="This endpoint requires the IsUser permission.",
    request_body=UserSerializer,
    responses={201: UserSerializer()}
)
@api_view(['POST', 'PUT'])
@permission_classes([IsCustomer])
def user_registration(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user_type = serializer.validated_data['user_type']
            password = serializer.validated_data['password']
            name = serializer.validated_data['name']
            user = User.objects.create_user(email=email, name=name, user_type=user_type, password=password)

            response = Response({'user_id': user.user_id, 'message': 'User registered successfully.'},
                                status=status.HTTP_201_CREATED)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        print(request.COOKIES.get('jwt_token'))
        print(request.data)
        # payload = check_user(request)
        # email = payload['email']
        # try:
        #     user = User.objects.get(email=email)
        # except User.DoesNotExist:
        #     return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        # serializer = UserSerializer(user, data=request.data, partial=True)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    tags=['User Modal'],
    method='post',
    operation_description="This endpoint requires the IsUser permission.",
    request_body=UserSerializer,
    responses={201: UserSerializer()}
)
@api_view(['POST'])
@permission_classes([AllowAny])  # Remove AllowAny decorator
def user_login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()
    if user is None:
        raise AuthenticationFailed("User Not Found")
    if not user.check_password(password):
        raise AuthenticationFailed("Incorrect Credentials")
    payload = {
        'email': user.email,
        'uid': user.user_id,
        'user_type': user.user_type,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'message': 'User logged in successfully.',
            'status': status.HTTP_200_OK,
            'token': token
        }
        return response
    else:
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(
    tags=['User Modal'],
    method='post',
    operation_description="This endpoint requires the IsUser permission.",
    request_body=UserSerializer,
    responses={201: UserSerializer()}
)
@api_view(['POST'])
@permission_classes([AllowAny])
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)


@swagger_auto_schema(
    tags=['User Modal'],
    method='put',
    operation_description="This endpoint requires the IsUser permission.",
)
@api_view(['PUT'])
@permission_classes([AllowAny, IsAuthenticated])
def change_password(request):
    if request.method == 'PUT':
        old_password = request.data['old_password']
        new_password = request.data['new_password']
        payload = check_user(request)
        email = payload['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Old password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
