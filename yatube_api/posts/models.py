from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    '''Создания групп постов.'''
    title = models.CharField(
        max_length=200,
        help_text='Введите название группы'
    )
    slug = models.SlugField(
        unique=True,
        help_text='Укажите порядковый № группы'
    )
    description = models.TextField(
        help_text='Добавьте текст описания группы'
    )

    def __str__(self):
        return self.title


class Post(models.Model):
    '''Создания постов пользователей.'''
    text = models.TextField(help_text='Введите текст статьи')
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        help_text='Укажите дату публикации'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        help_text='Укажите автора статьи'
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        help_text='Добавьте картинку статьи'
    )
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE,
        related_name="posts", blank=True, null=True
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    '''Создания комментариев пользователей к постам.'''
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    '''Создания подписок пользователей.'''
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        help_text='Подписчик'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        help_text='Автор поста'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['following', 'user'],
                name='unique_following_user',
            )
        ]

    def __str__(self):
        return self.user
