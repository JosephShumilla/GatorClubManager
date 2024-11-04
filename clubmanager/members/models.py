from django.db import models


class Club(models.Model):
    club_name = models.CharField(max_length=100, unique=True)  # Unique identifier for each club
    club_desc = models.TextField()

    def __str__(self):
        return self.club_name  # Use club_name for string representation

    class Meta:
        db_table = 'Club_Database'


class Membership(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=[('member', 'Member'), ('manager', 'Manager')])

    def __str__(self):
        return f'{self.user.username} is a {self.role} of {self.club.club_name}'