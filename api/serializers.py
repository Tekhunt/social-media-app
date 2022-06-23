from pyexpat import model
from tabnanny import verbose
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import User, Post, Like, DisLike


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "name"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        user = super.update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class DisLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisLike
        fields = "__all__"


class PostSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    likes = LikeSerializer(many=True, required=False)
    dis_likes = DisLikeSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = "__all__"
