from django.core.management.base import BaseCommand, CommandError
from haiku.models import Haiku

from haiku.RSS import TrackingChannel, RSSParser
import feedparser

class Command(BaseCommand):
    args = ''
    help = 'Grab some poems and throw them in the DB'

    haiku_url = 'http://tinywords.com/feed/'

    def handle(self, *args, **options):
        feed = feedparser.parse(self.haiku_url)
        for item in feed[ "items" ]:
            Haiku(
                name = item['author'],
                text = item['summary_detail']['value']
            ).save()
            print item['author']