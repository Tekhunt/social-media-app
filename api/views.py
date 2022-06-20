from rest_framework import generics
from rest_framework.response import Response

from .models import Post, User
from .serializers import PostSerializer, UserSerializer, UserDataSerializer

# import pygeoip
class UserRegister(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "message": "User Created Successfully.  Now perform Login to get your token",
            }
        )

class UserData(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDataSerializer

class GetUser(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDataSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
