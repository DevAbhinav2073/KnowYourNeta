from rest_framework import serializers

from apps.authuser.models import PoliticianDetail
from apps.system.models import *


class PoliticianDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliticianDetail
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


class PartySerializer(serializers.ModelSerializer):
    total_votes = serializers.SerializerMethodField()

    def get_total_votes(self, obj):
        return obj.total_votes

    class Meta:
        model = Party
        fields = '__all__'


class ConstituencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Constituency
        fields = '__all__'


class AssemblySegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssemblySegment
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
