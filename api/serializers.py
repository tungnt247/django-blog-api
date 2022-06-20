from rest_framework import serializers
from api.models import User, Post
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'created_at', 'updated_at']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        for field in validated_data:
            setattr(instance, field, validated_data[field])
        instance.save()
        return instance

    def validate_password(self, value):
        valid_password = len(value) > 6 and not value.isalnum()
        if not valid_password:
            raise serializers.ValidationError(
                'Password invalid! password has at least 6 characters and 1 special character')
        return value


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'user', 'created_at', 'updated_at']
