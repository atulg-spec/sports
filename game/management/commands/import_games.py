import csv
from django.core.management.base import BaseCommand
from game.models import Game
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Import games from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help="Path to the CSV file")

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        try:
            with open(csv_file, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    try:
                        image_src, iframe_url, title, description = row
                        slug = slugify(title)
                        Game.objects.update_or_create(
                            slug=slug,
                            defaults={
                                'name': title,
                                'thumbnail': image_src,
                                'iframe': iframe_url,
                                'description': description,
                                'instructions': 'Play Now',
                            }
                        )
                        self.stdout.write(self.style.SUCCESS(f"Game '{title}' imported successfully."))
                    except ValueError:
                        self.stdout.write(self.style.ERROR(f"Invalid row format: {row}"))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File '{csv_file}' not found."))
