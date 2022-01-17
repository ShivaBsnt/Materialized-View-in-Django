from django.db import models


class User(models.Model):
    name = models.CharField(max_length=10)
    age = models.PositiveSmallIntegerField()
    phone_num = models.CharField(max_length=10)


class UserMaterializedView(models.Model):
    name = models.CharField(max_length=10)
    age = models.PositiveSmallIntegerField()
    phone_num = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'polls_user_matt_view'


