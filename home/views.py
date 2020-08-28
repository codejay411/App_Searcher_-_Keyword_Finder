from django.shortcuts import render, HttpResponse, render
import requests
from bs4 import BeautifulSoup
import html5lib
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Create your views here.
# admin username searcher  nad password searcher

def index(request):
    # return HttpResponse("this is home page")
    return render(request, "home.html")


def app_searcher(request):
    # return HttpResponse("this is searcher page")
    google={}
    try:
        if request.method=='POST':
            package=request.POST['package']
            # print(package)
            url="https://play.google.com/store/apps/details?id="+package
            # print(url)
        
            r=requests.get(url)
            htmlcontent=r.content

            soup =BeautifulSoup(htmlcontent, 'html.parser')
            # print(soup.prettify())

            # # app name
            appname = soup.find("h1", class_="AHFaub").get_text()
            # print(appname)

            # # app icon
            icon = soup.find("div", class_="xSyT2c").img['src']
            # print(icon)

            # # developer name
            sd = soup.find_all("span", class_="htlgb")[-1]
            dname=sd.find_all("div")[-1].get_text()
            # print(dname)

            # # description
            desc=soup.find("div", class_="JHTxhe IQ1z0d").meta.get('content')[:200]+"..."
            # print(desc)

            # # number of downloads
            download = soup.find_all("span", class_="htlgb")[5].get_text()
            # print(download)

            # # number of reviews
            review = soup.find_all("span", class_="")[-3].get_text()
            # print(review)

            # # rating
            rating = soup.find("div", class_="BHMmbe").get_text()
            # print(rating)
            google={'appname':appname, 'icon':icon, 'dname':dname, 'desc':desc, 'download':download, 'review':review, 'rating':rating }
            
            
    except:
        if request.method=='POST':
            name=request.POST['name']
            application=request.POST['application']
            # print(name, application)
            url="https://apps.apple.com/in/app/"+name+"/"+application
            # print(url)
            r=requests.get(url)
            htmlcontent=r.content
            # print(htmlcontent)

            soup =BeautifulSoup(htmlcontent, 'html.parser')
            # print(soup.prettify())

            # app name
            appname = soup.find("h1", class_="product-header__title app-header__title").get_text()[:-3]
            # print(appname)

            # app icon
            icon = soup.find("source", class_="we-artwork__source")['srcset'].split(',')[0][:-3]
            # print(icon)

            # developer name
            dname = soup.find("dd", class_="information-list__item__definition l-column medium-9 large-6").get_text()
            # print(dname)


            # description
            desc = soup.find("div", class_="we-truncate we-truncate--multi-line we-truncate--interactive ember-view l-column small-12 medium-9 large-8").p.get_text()[:200]+"..."
            # print(desc)


            # number of reviews
            review = soup.find("div", class_="we-customer-ratings__count small-hide medium-show").get_text()[:2]
            # print(review)
            
            download=""
            # print(download)

            # rating
            rating = soup.find("span", class_="we-customer-ratings__averages__display").get_text()
            # print(rating)

            google={'appname':appname, 'icon':icon, 'dname':dname, 'desc':desc, 'download':download, 'review':review, 'rating':rating }


    return render(request, "app_searcher.html", google)



def keyword_finder(request):
    # return HttpResponse("this is keyword page")
    if request.method=='POST':
        url=request.POST['url']
        print(url)  

        # getting the html    
        r=requests.get(url)
        htmlcontent=r.content

        # parse the content
        soup = BeautifulSoup(htmlcontent, 'html.parser')
        # print(soup.prettify())
        # getting all link
        anchor=soup.find_all('a')
        # print(anchor)
        all_link=set()
        for link in anchor:
            all_link.add(link.get('href'))
            # print(all_link, end=",")


    return render(request, "keyword_finder.html")

