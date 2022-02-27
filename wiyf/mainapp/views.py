import json

from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd



def home(request):
    return render(request, 'home.html')

def add(request):
    return render(request,'add.html')
    # fridge_fill = request.body['fill']
    # return fridge_fill



# def cook(request):
#     df = pd.read_csv("../tops.csv")
#     df.drop(df["Category"])
#     cook_object = df.to_html()
#     return HttpResponse(cook_object)


def cook(request):
    df = pd.read_csv("../tops.csv")
    df.drop(['Category'], axis=1)
    json_records = df.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}

    return render(request, 'cook.html', context)

def recom(request):
    df = pd.read_csv("../rec.csv")
    json_records = df.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}

    return render(request, 'recom.html', context)