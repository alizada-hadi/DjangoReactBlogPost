from .serializers import ArticleSerializer
from articles.models import Article


from rest_framework import generics, serializers


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer