from django.contrib.syndication.views import Feed
from django.shortcuts import reverse
from .models import Article


class ArticleFeed(Feed):
    title = "优美文章精选"
    description = "定期更新优美的文章"
    link = "/"

    def items(self):
        return Article.objects.all().order_by("-create_time")[:3]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.author

    def item_link(self, item):
        url = reverse("blogapp:detail", args=(item.id,))
        return url
