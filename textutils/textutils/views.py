#I have created this file (shivam )
from django.http import HttpResponse
from django.shortcuts import render


def  index(request):
    return render(request,'index.html')
    #return HttpResponse("Home")

def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    charcount = request.POST.get('charcount','off')

    if removepunc == "on":
         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
         analyzed=""
         for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
         params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
         # analyze the text
         return render(request, 'analyze.html', params)

    elif(fullcaps=="on"):
         analyzed=""
         for char in djtext:
             analyzed=analyzed+char.upper()

         params = {'purpose': 'Upper Case', 'analyzed_text': analyzed}
        # analyze the text
         return render(request, 'analyze.html', params)

    elif(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
             if char != "\n" and char !="\r":
                analyzed = analyzed + char
             else:
                 print("no")
             print("pre",analyzed)

        params = {'purpose': 'Removed newLine', 'analyzed_text': analyzed}
        # analyze the text
        return render(request, 'analyze.html', params)

    elif (spaceremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != " ":
                analyzed = analyzed + char

        params = {'purpose': 'Space Removed', 'analyzed_text': analyzed}
        # analyze the text
        return render(request, 'analyze.html', params)

    elif (charcount == "on"):
        analyzed = 0
        for char in djtext:
             if char != " ":
                analyzed = analyzed + 1

        params = {'purpose': 'Space Removed', 'analyzed_text': analyzed}
        # analyze the text
        return render(request, 'analyze.html', params)

    else:
        analyzed=djtext

    params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
    #analyze the text
    return render(request, 'analyze.html', params)














'''def capfirst(request):
    return HttpResponse("Captilize first")


def newlineremove(request):
    return HttpResponse("newline remove")

def spaceremove(request):
    return HttpResponse("space remover <a href='/'>Back</a>")

def charcount(request):
    return HttpResponse("charcount")

'''