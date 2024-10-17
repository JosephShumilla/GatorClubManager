from django.db import models


class Club(models.Model):
    club_name = models.CharField(max_length=100, unique=True)  # Unique identifier for each club
    club_desc = models.TextField()

    def __str__(self):
        return self.club_name  # Use club_name for string representation

    class Meta:
        db_table = 'Club_Database'

def __str__(self):
    return self.name