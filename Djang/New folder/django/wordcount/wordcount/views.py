from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'text': 'This is Home.'})

def eggs(request):
    return HttpResponse('Hello Eggs.')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    wordDict = {}

    for word in wordlist:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'wordDict': wordDict.items})