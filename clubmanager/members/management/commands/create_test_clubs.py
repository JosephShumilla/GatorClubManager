# clubmanager/management/commands/create_clubs.py
from django.core.management.base import BaseCommand
from members.models import Club

class Command(BaseCommand):
    help = 'Create test clubs programmatically'

    def handle(self, *args, **kwargs):
        # list of 25 fake club names
        club_names = [
            'Math Club', 'Science Club', 'Chess Club', 'Art Club', 'Music Club',
            'Dance Club', 'Gaming Club', 'Reading Club', 'Writing Club', 'Coding Club',
            'Robotics Club', 'Anime Club', 'Film Club', 'Photography Club', 'Cooking Club',
            'Gardening Club', 'Astronomy Club', 'Debate Club', 'Investment Club', 'Business Club',
            'Marketing Club', 'Entrepreneurship Club', 'Fashion Club', 'Fitness Club', 'Yoga Club'
        ]
        club_descs = [
            'For math lovers', 'For science enthusiasts', 'For chess players', 'For artists', 'For music lovers',
            'For dancers', 'For gamers', 'For readers', 'For writers', 'For coders',
            'For robotics enthusiasts', 'For anime lovers', 'For film lovers', 'For photographers', 'For cooks',
            'For gardeners', 'For astronomers', 'For debaters', 'For investors', 'For business enthusiasts',
            'For marketers', 'For entrepreneurs', 'For fashion lovers', 'For fitness enthusiasts', 'For yogis'
        ]
        for name, desc in zip(club_names, club_descs):
            Club.objects.create(club_name=name, club_desc=desc)
        self.stdout.write(self.style.SUCCESS('Successfully added clubs'))
