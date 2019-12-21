from django.shortcuts import render
from django.http import HttpResponse
import requests,json

# Create your views here.
def index(request):
    return render(request,'index.html')

def search(request):
    if request.method == "POST":
        try:
            q = request.POST['keyword'] 
            urlpart1 = "https://newsapi.org/v2/everything?q="
            urlpart2 = "&from=2019-12-8&sortBy=publishedAt&pageSize=10&apiKey="
            API_KEY = "09ea697cc4764ec0ab4987df2ad097fc"
            main_url = urlpart1+str(q)+urlpart2+API_KEY
             # fetching data in json format
            page = requests.get(main_url).json()
            # getting all articles in a string article
            articles = page["articles"]
            mydict = {
                "error":False,
                "result":True,
                "keyword":q,
                "articles":articles
            }
            print("search")
            print(articles[0])
            print(type(articles))
            print(type(articles[0]))
            return render(request,'index.html',context=mydict)
        except:
            mydict = {
                "error":True,
                "result":False
            }
            return render(request,'index.html',context=mydict)

