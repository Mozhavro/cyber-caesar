from django.shortcuts import render

def index(request):
    return render(request, "cesar_cypher/index.html")
