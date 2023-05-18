from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.http import HttpResponse
# Create your views here.
def display_topics(request):
    LOT=Topic.objects.all()
    #LOT-Topic.objects.filter(topic_name='cricket')
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topics.html',d)

def display_webpage(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.order_by(Length('name'))
    LOW=Webpage.objects.order_by(Length('name').desc())
    LOW=Webpage.objects.order_by('url')
    LOW=Webpage.objects.order_by('-url')
    LOW=Webpage.objects.exclude(name='virat')
    LOW=Webpage.objects.filter(name__gt='dhoni')
    LOW=Webpage.objects.filter(name__startswith='j')
    LOW=Webpage.objects.filter(name__endswith='t')
    LOW=Webpage.objects.filter(name__in=('dhoni'))
    LOW=Webpage.objects.filter(name__contains='dhoni')
    LOW=Webpage.objects.filter(name__contains='a')
    LOW=Webpage.objects.order_by('name')
    LOW=Webpage.objects.exclude(name='Jaya Chandra')
    LOW=Webpage.objects.all()
    d={'web':LOW}
    return render(request,'display_webpage.html',d)
def display_access(request):
    LOA=AccessRecords.objects.all()
    d={'access':LOA}
    return render(request,'display_access.html',d)

def update_webpage(request):
    d={'web':Webpage.objects.all()}
    LOW=Webpage.objects.filter(name='dhoni').update(url='https://msd.com')
    LOW=Webpage.objects.filter(name='virat').update(url='http://virat.in')
    LOW=Webpage.objects.filter(url='https://msd.com').update(name='MSD')
    LOW=Webpage.objects.all()
    TO=Topic.objects.get_or_create(topic_name='cricket')[0]
    TO.save()
    LOW=Webpage.objects.update_or_create(name='dhoni',defaults={'topic_name':TO,'url':'https://dhoni.in'})
    #LOW=Webpage.objects.filter(name='virat').update(url='http://virat.com')
    #LOW=Webpage.objects.filter(name='jaya').update(url='https://jaya.com')
    LOW=Webpage.objects.all()
    return render(request,'display_webpage.html',d)
def update_access(request):
    d={'access':AccessRecords.objects.all()}
    #LOA=AccessRecords.objects.filter(author='abc').update(date='1997-10-17')
    #LOA=AccessRecords.objects.all()
    #LOA=AccessRecords.objects.filter(author='xyz').update(date='1997-10-13')
    LOA=AccessRecords.objects.filter(author='ABC').update(date='2000-09-11')
    WO=Webpage.objects.get_or_create(name='jaya')[0]
    WO.save()
    LOA=AccessRecords.objects.update_or_create(author='Jaya',defaults={'date':'2000-10-13','name':WO})
    return render(request,'display_access.html',d)
def delete_webpage(request):
    d={'web':Webpage.objects.all()}
    return render(request,'delete_webpage.html',d)