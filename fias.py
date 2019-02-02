import urllib2
from bs4 import BeautifulSoup

baseURL = "https://www.fiasfreshmeals.com"
menuURL = baseURL + "/this-weeks-menu-2"
response = urllib2.urlopen(menuURL)
html = response.read()

soup = BeautifulSoup(html, features="html.parser")

itemURLs = []

for itemDivs in soup.findAll("div", {"class": "card-image"}):
    for link in itemDivs.findAll("a"):
        #print (link.get("href"))
        itemURLs.append(link.get("href"))

for itemURL in itemURLs:
    itemResponse = urllib2.urlopen(baseURL + itemURL)
    itemHtml = itemResponse.read()
    itemSoup = BeautifulSoup(itemHtml, features="html.parser")
    foodName = itemSoup.find("meta",  property="og:title")
    print "Food Name: " + foodName["content"]
    print "Calories: " + itemSoup.find(text="Calories").findNext('td').contents[0]
    print "Fat: " + itemSoup.find(text="Total Fat").findNext('td').span.contents[0]
    print "Sodium: " + itemSoup.find(text="Sodium").findNext('td').span.contents[0]
    print "Carbohydrate: " + itemSoup.find(text="Total").findNext('td').span.contents[0]
    print "Protein: " + itemSoup.find(text="Protein").findNext('td').span.contents[0]
    print ""
    #exit(1)
    



