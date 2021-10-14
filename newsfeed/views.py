import json
import os
from django.conf import settings
from django.http.response import JsonResponse
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls.static import static


def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def public(url):
    url = url.replace('/', '\\')
    path = os.path.join(settings.STATIC_ROOT, url)
    path = path.replace("\\", '/')
    return path


def newsfeed(request):
    filepath_dict = {
        'yelp':  public('data/sentiment_analysis/yelp_labelled.txt'),
        'amazon': public('data/sentiment_analysis/amazon_cells_labelled.txt'),
        'imdb':   public('data/sentiment_analysis/imdb_labelled.txt'),
    }

    df_list = []
    for source, filepath in filepath_dict.items():
        df = pd.read_csv(filepath, names=['sentence', 'label'], sep='\t')
        df['source'] = source  # Add another column filled with the source name
        df_list.append(df)

    df = pd.concat(df_list)
    # print(df.iloc[0])

    return JsonResponse(json.loads(df.iloc[0].to_json()),safe= False)
