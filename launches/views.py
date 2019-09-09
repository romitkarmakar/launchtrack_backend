from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from bs4 import BeautifulSoup
import json
import datetime
from launches.models import Launch, Spaceport, Company
from launches.jobs import runSpaceX, runNASA, runSpaceports

def getCompanies(req):
    companies = Company.objects.all()
    response = []
    for company in companies:
        response.append({
            "name": company.name,
            "image": company.image,
            "details": company.details
        })

    return JsonResponse({
        "data": response
    })

def getSpaceX(req):
    company = Company.objects.get(name='SpaceX')
    launches = Launch.objects.filter(company=company)

    arr = []
    for i in launches:
        arr.append({
            "name": i.name,
            "date": i.date,
            "details": i.details
        })

    return JsonResponse({
        "data": arr
    })


def getNASA(req):
    company = Company.objects.get(name='NASA')
    launches = Launch.objects.filter(company=company)

    arr = []
    for i in launches:
        arr.append({
            "name": i.name,
            "date": i.date,
            "details": i.details
        })

    return JsonResponse({
        "data": arr
    })


def getISRO(req):
    response = requests.get("http://www.antrix.co.in/business/upcoming-missions")
    soup = BeautifulSoup(response.content, "html.parser")

    cleantext = []
    cleantext.append(
        BeautifulSoup(
            soup.select(".md-object > a")[0].text.replace("\n", "").strip(), "lxml"
        ).text
    )

    return JsonResponse(cleantext, safe=False)


def getRoscosmos(req):
    now = datetime.datetime.now()

    response = requests.get("http://en.roscosmos.ru/launch/{}".format(now.year))
    soup = BeautifulSoup(response.content, "html.parser")

    cleantext = []

    for i in soup.select("table")[0].select("tr")[1:]:
        temp = []
        if i.select("td")[5].text[0] == "U":
            for l in i.select("td"):
                temp.append(
                    BeautifulSoup(l.text.replace("\n", "").strip(), "lxml").text
                )
            cleantext.append(temp)

    return JsonResponse(cleantext, safe=False)


def getESA(req):
    now = datetime.datetime.now()

    response = requests.get(
        "https://www.esa.int/Newsroom/Launch_schedule_{}".format(now.year)
    )
    soup = BeautifulSoup(response.content, "html.parser")

    cleantext = []

    for i in range(len(soup.select(".section")[0].select("p"))):
        if i % 4 == 0 and i > 0:
            cleantext.append(
                [
                    i.replace("\xa0", "")
                    for i in soup.select(".section")[0]
                    .select("p")[i]
                    .text.strip()
                    .split("\n")
                ]
            )

    return JsonResponse(cleantext, safe=False)

def getSpacePorts(req):
    spaceports = Spaceport.objects.all()
    arr = []
    for i in spaceports:
        arr.append({
            "name": i.name,
            "country": i.country
        })

    return JsonResponse({
        "data": arr
    })

def runJobs(req):
    runNASA()
    runSpaceX()
    runSpaceports()

    return HttpResponse("Successful")