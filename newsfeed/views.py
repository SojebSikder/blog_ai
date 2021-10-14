import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def newsfeed(request):
    filepath_dict = {'yelp':   'data/sentiment_analysis/yelp_labelled.txt',
                    'amazon': 'data/sentiment_analysis/amazon_cells_labelled.txt',
                    'imdb':   'data/sentiment_analysis/imdb_labelled.txt'}

    df_list = []
    for source, filepath in filepath_dict.items():
        df = pd.read_csv(filepath, names=['sentence', 'label'], sep='\t')
        df['source'] = source  # Add another column filled with the source name
        df_list.append(df)

    df = pd.concat(df_list)
    print(df.iloc[0])

    return HttpResponse("Hello World")
