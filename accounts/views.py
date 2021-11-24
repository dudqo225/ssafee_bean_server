from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, UserAvatarSerializer, UserUpdateSerializer, UserMileageUpdateSerializer
from django.contrib.auth import get_user_model

# 회원 아바타
@api_view(['GET'])
def users(request):
    users = get_list_or_404(get_user_model())
    serializer = UserAvatarSerializer(users, many=True)
    return Response(serializer.data)

# 회원가입
@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    # Client에서 받은 비밀번호/비밀번호 확인 변수 저장
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')

    # 비밀번호 일치 여부 확인 후, 다르면 Error 반환
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    # 데이터 직렬화
    serializer = UserSerializer(data=request.data)

    # 데이터 검증 후 Response 반환
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        # 비밀번호 해싱
        user.set_password(password)
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 프로필 페이지
@api_view(['GET', 'PUT'])
def user_detail(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserUpdateSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


# 마일리지 변경
@api_view(['PUT'])
def user_mileage(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    serializer = UserMileageUpdateSerializer(user, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
