from django.contrib.syndication.views import Feed
from django.shortcuts import reverse
from .views import Article


class ArticleFeed(Feed):
    title = "RSS工具的初步使用"
    description = "定期发布自己的学习情况"
    link = "/"

    def items(self, num=3):
        return Article.objects.all().order_by("-create_time")[:num]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        url = reverse("blog_app:detail", args=(item.id,))
        return url
