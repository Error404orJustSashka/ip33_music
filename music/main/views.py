from django.shortcuts import render

# Create your views here.
def index(reqest):
    return render(reqest, 'index.html')

# def zanr_musik(reqest):
#     return render(reqest, '')