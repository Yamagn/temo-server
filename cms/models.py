from django.db import models

class User(models.Model):
    roll = models.CharField('役職', max_length=255)
    name = models.CharField("ユーザ名", max_length=255, unique=True)
    display_name = models.CharField("表示名", max_length=255)
    created_at = models.DateTimeField("登録日時", auto_now_add=True)
    team_num = models.IntegerField("チーム数", max_length=255)

    def __str__(self):
        return self.name

class Day(models.Model):
    date = models.DateField('日付', unique_for_date=True)
    emo = models.IntegerField('エモ度', max_length=6)

    def __str__(self):
        return self.date

class Team(models.Model):
    created_at = models.DateTimeField("チーム作成日", auto_now_add=True)
    users = models.ForeignKey(User, verbose_name="ユーザー", on_delete=models.CASCADE)
    calendar = models.ForeignKey(Day, verbose_name="日付", on_delete=models.CASCADE)

    def __str__(self):
        return self.created_at