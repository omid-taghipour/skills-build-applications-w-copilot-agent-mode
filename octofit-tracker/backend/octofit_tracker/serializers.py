from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)
    def to_internal_value(self, data):
        return ObjectId(data)

class UserSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'team']

class TeamSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    class Meta:
        model = Team
        fields = ['id', 'name']

class ActivitySerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Activity
        fields = ['id', 'user', 'type', 'duration', 'date']

class LeaderboardSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'score']

class WorkoutSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'difficulty']
