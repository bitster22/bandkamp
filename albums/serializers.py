from rest_framework import serializers
from .models import Album
from users.serializers import UserSerializer


class AlbumSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Album
        fields = "__all__"

    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=255)
    # year = serializers.IntegerField()
    # user = UserSerializer(read_only=True)

    def create(self, validated_data):
        return Album.objects.create(**validated_data)
