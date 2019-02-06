from django.db import models


class User(models.Model):
    roll = models.CharField('役職', max_length=255)
    name = models.CharField("ユーザ名", max_length=255, unique=True)
    display_name = models.CharField("表示名", max_length=255)
    created_at = models.DateTimeField("登録日時", auto_now_add=True)
    team_num = models.IntegerField("チーム数", max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, verbose_name="ユーザー", on_delete=models.CASCADE)
    emo = models.IntegerField("エモ度")
    day = models.DateField("日付", auto_now_add=True)

    def __str__(self):
        return self.date


class Team(models.Model):
    created_at = models.DateTimeField("チーム作成日", auto_now_add=True)
    users = models.ForeignKey(User, verbose_name="ユーザー", on_delete=models.CASCADE)
    posts = models.ForeignKey(Post, verbose_name="投稿", on_delete=models.CASCADE)

    def __str__(self):
        return self.created_at
