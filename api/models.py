from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractBaseUser, BaseModel):
    # Remove unuse fields
    last_login = None
    is_staff = None
    is_superuser = None

    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email


class Post(BaseModel):
    title = models.CharField(max_length=1000)
    content = models.CharField(max_length=10000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return self.title


class Comment(BaseModel):
    content = models.CharField(max_length=10000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        db_table = 'comments'

    def __str__(self):
        return self.content


class Reaction(BaseModel):
    class ReactionType(models.TextChoices):
        LIKE = 'like'
        DISLIKE = 'dislike'
        SAD = 'sad'
        HAHA = 'haha'
        LOVE ='love'

    type = models.CharField(max_length=7, choices=ReactionType.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        db_table = 'reactions'

    def __str__(self):
        return self.type
