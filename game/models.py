from django.db import models
from django.utils.text import slugify

class Game(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    thumbnail = models.URLField(max_length=500)  # Changed to URLField
    iframe = models.URLField(max_length=500)
    description = models.TextField()
    instructions = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Game, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"
