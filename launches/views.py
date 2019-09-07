from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from bs4 import BeautifulSoup
import json
import datetime


def getSpaceX(req):
    response = requests.get("https://www.spacex.com/missions")
    soup = BeautifulSoup(response.content, "html.parser")

    cleantext = []

    for i in soup.select(".views-table")[1].select("tbody")[0].select("tr"):
        temp = []
        for l in i.select("td"):
            temp.append(BeautifulSoup(l.text.replace("\n", "").strip(), "lxml").text)
        cleantext.append(temp)
    return JsonResponse(cleantext, safe=False)


def getNASA(req):
    response = requests.get(
        "https://www.nasa.gov/api/2/calendar-event/_search?size=100&from=0&sort=event-date.value&q=(((calendar-name%3A6089)%20AND%20(event-date.value%3A%5B2019-09-07T06%3A44%3A10-04%3A00%20TO%202029-09-07T06%3A44%3A10-04%3A00%5D%20OR%20event-date.value2%3A%5B2019-09-07T06%3A44%3A10-04%3A00%20TO%202029-09-07T06%3A44%3A10-04%3A00%5D)%20AND%20event-date-count%3A1))"
    )
    y = json.loads(response.content)

    cleantext = []

    for i in y["hits"]["hits"]:
        temp = []
        temp.append(i["_source"]["title"])
        temp.append(i["_source"]["event-date"][0]["value"])
        temp.append(i["_source"]["name"])

        cleantext.append(temp)

    return JsonResponse(cleantext, safe=False)


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
