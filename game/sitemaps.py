from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Game  # Replace with your actual model name

class GameSitemap(Sitemap):
    changefreq = "daily"  # Frequency of changes
    priority = 1.0  # Priority for search engines

    def items(self):
        # Return all objects that should be in the sitemap
        return Game.objects.all()

    def lastmod(self, obj):
        # Return the last modified date of the object
        return obj.updated_at  # Replace with the correct field name from your model

    def location(self, obj):
        # Return the URL of the object
        return reverse('game_detail', args=[obj.slug])  # Adjust for your app's URL pattern
