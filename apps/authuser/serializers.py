from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from apps.utils import DynamicFieldsModelSerializer

User = get_user_model()


class UserSerializer(DynamicFieldsModelSerializer):
    token = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()
    party_name = serializers.SerializerMethodField()
    constituency_name = serializers.SerializerMethodField

    def get_party_name(self, obj):
        if obj.party is not None:
            return obj.party.name

    def get_constituency_name(self, obj):
        if obj.constituency is not None:
            return obj.constituency.name

    def get_token(self, obj):
        obj, created = Token.objects.get_or_create(user=obj)
        return obj.key

    def get_full_name(self, obj):
        return obj.get_full_name()

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
            , email=validated_data.get('email')
            , first_name=validated_data['first_name']
            , last_name=validated_data['last_name']
            , user_type=validated_data['user_type']
            , fathers_name=validated_data.get('fathers_name', None)
            , date_of_birth=validated_data.get('date_of_birth', None)
            , address=validated_data.get('address', None)
            , mobile_number=validated_data.get('mobile_number', None)
            , age=validated_data.get('age', None)
            , party=validated_data.get('party', None)
            , constituency=validated_data.get('constituency', None)
            , assembly_segment=validated_data.get('assembly_segment', None)
            , photo=validated_data.get('photo', None)
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        fields = (
            'id', 'username', 'password', 'email', 'mobile_number', 'first_name', 'last_name', 'full_name', 'token',
            'user_type', 'fathers_name', 'date_of_birth', 'address', 'age', 'party', 'constituency', 'party_name',
            'constituency_name', 'photo',
            'assembly_segment')
        model = User
