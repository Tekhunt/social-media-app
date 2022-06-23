from rest_framework import generics
from rest_framework.response import Response
import requests
from .models import Post, User, Like, DisLike
from .serializers import (
    PostSerializer,
    UserSerializer,
    UserDataSerializer,
    LikeSerializer,
    DisLikeSerializer,
)
from datetime import date
import os
from dotenv import load_dotenv

load_dotenv()

email_key = os.getenv("EMAIL_API_KEY")
geodata_key = os.getenv("GEODATA_API_KEY")
holiday_key = os.getenv("HOLIDAY_API_KEY")


class UserRegister(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        geo_data = requests.get(
            f"https://ipgeolocation.abstractapi.com/v1/?api_key={geodata_key}"
        )
        geo_data_response = geo_data.json()
        email = request.data.get("email")
        current_year = date.today().year
        current_month = date.today().month
        current_day = date.today().day

        response = requests.get(
            f"https://holidays.abstractapi.com/v1/?api_key={holiday_key}&country=NG&year={current_year}&month={current_month}&day={current_day}"
        )
        holiday_data_res_obj = response.json()

        response = requests.get(
            f"https://emailvalidation.abstractapi.com/v1/?api_key={email_key}&email={email}"
        )
        email_check_res = response.json()

        if email_check_res.get("quality_score"):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            return Response(
                {
                    "user": UserSerializer(
                        user, context=self.get_serializer_context()
                    ).data,
                    "message": "User Created Successfully",
                    "continent": geo_data_response["continent"],
                    "country": geo_data_response["country"],
                    "timezone": geo_data_response["timezone"],
                    "region": geo_data_response["region"],
                    "city": geo_data_response["city"],
                    "holiday": holiday_data_res_obj[0].get("name")
                    if holiday_data_res_obj
                    else "no holiday",
                }
            )
        else:
            return Response(
                {
                    "message": "Poor email quality and deliverability, please use a valid email"
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


class UpdatePost(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LikeList(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class LikeDetail(generics.RetrieveDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class DisLikeList(generics.ListCreateAPIView):
    queryset = DisLike.objects.all()
    serializer_class = DisLikeSerializer


class DisLikeDetail(generics.RetrieveDestroyAPIView):
    queryset = DisLike.objects.all()
    serializer_class = DisLikeSerializer
