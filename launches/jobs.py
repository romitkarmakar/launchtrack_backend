import requests
from bs4 import BeautifulSoup
import json
import datetime

from launches.models import Company, Launch, Spaceport
from django.utils import timezone

def runSpaceX():
    response = requests.get("https://www.spacex.com/missions")
    soup = BeautifulSoup(response.content, "html.parser")

    Launch.objects.filter(company='SpaceX').delete()

    for i in soup.select(".views-table")[1].select("tbody")[0].select("tr"):
        launch = Launch()
        launch.name = BeautifulSoup(i.select("td")[0].text.replace("\n", "").strip(), "lxml").text
        launch.location = BeautifulSoup(i.select("td")[1].text.replace("\n", "").strip(), "lxml").text
        launch.details = BeautifulSoup(i.select("td")[2].text.replace("\n", "").strip(), "lxml").text
        launch.date = timezone.now()
        launch.company = Company.objects.get(name='SpaceX')
        launch.save()

    return 1

def runNASA():
    response = requests.get(
        "https://www.nasa.gov/api/2/calendar-event/_search?size=100&from=0&sort=event-date.value&q=(((calendar-name%3A6089)%20AND%20(event-date.value%3A%5B2019-09-07T06%3A44%3A10-04%3A00%20TO%202029-09-07T06%3A44%3A10-04%3A00%5D%20OR%20event-date.value2%3A%5B2019-09-07T06%3A44%3A10-04%3A00%20TO%202029-09-07T06%3A44%3A10-04%3A00%5D)%20AND%20event-date-count%3A1))"
    )
    y = json.loads(response.content)

    company = Company.objects.get(name='NASA')
    Launch.objects.filter(company=company).delete()

    for i in y["hits"]["hits"]:
        launch = Launch()
        launch.name = i["_source"]["title"]
        launch.details = i["_source"]["description"]
        date = i["_source"]["event-date"][0]["value"]
        dateArr = date.split("T")
        launch.date = i["_source"]["event-date"][0]["value"]
        launch.company = Company.objects.get(name='NASA')
        launch.save()

    return 1

def runSpaceports():
    response = requests.get("https://en.wikipedia.org/wiki/Spaceport")
    soup = BeautifulSoup(response.content, 'html.parser')

    Spaceport.objects.all().delete()

    for i in soup.select("table.wikitable")[2].select("tbody")[0].select("tr")[1:]:
        spaceport = Spaceport()
        spaceport.name = BeautifulSoup(i.select("td")[0].text.split("[")[0].strip(), "lxml").text
        spaceport.country = BeautifulSoup(i.select("td")[1].text.split("[")[0].strip(), "lxml").text
        spaceport.save()

    return 1
