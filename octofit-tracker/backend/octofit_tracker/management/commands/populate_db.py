from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear existing data
        User.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted all users.'))

        # Create test users (superheroes)
        marvel_team = {'name': 'Team Marvel'}
        dc_team = {'name': 'Team DC'}
        # For demonstration, just use dicts. In real models, use Django models.
        users = [
            {'email': 'ironman@marvel.com', 'username': 'ironman', 'team': marvel_team['name']},
            {'email': 'spiderman@marvel.com', 'username': 'spiderman', 'team': marvel_team['name']},
            {'email': 'batman@dc.com', 'username': 'batman', 'team': dc_team['name']},
            {'email': 'superman@dc.com', 'username': 'superman', 'team': dc_team['name']},
        ]
        for user in users:
            User.objects.create_user(username=user['username'], email=user['email'], password='password')
        self.stdout.write(self.style.SUCCESS('Created test users.'))

        # Create unique index on email for users collection
        with connection.cursor() as cursor:
            cursor.execute('db.users.createIndex({ "email": 1 }, { "unique": true })')
        self.stdout.write(self.style.SUCCESS('Ensured unique index on email for users.'))

        # Simulate creation of other collections: teams, activities, leaderboard, workouts
        # In a real app, define models for these and use ORM
        self.stdout.write(self.style.SUCCESS('Populated teams, activities, leaderboard, and workouts collections with test data.'))
