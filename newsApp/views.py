from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.


def home(request):
    newsApi = NewsApiClient(api_key='17af1b67e52a44fa85a60b1f052df07d')
    headLines = newsApi.get_top_headlines(
        sources='ign, cnn, bbc-news, google-news')
    articles = headLines['articles']
    desc = []
    news = []
    img = []
    source = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        source.append(article['source']['name'])
    mylist = zip(news, desc, img, source)

    return render(request, "index.html", context={"mylist": mylist})
