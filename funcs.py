import requests
from bs4 import BeautifulSoup as bs

""" 
    The method gets a link to a movie webpage and returns a list of dicts.
    Keys: actor: the name of the actor
    href: the link to the actor's webpage
 """
def getAct(url):
    host = url.split('w')[0]  + url.split('/')[2] # the host url(and scheme)

    res = requests.get(url)
    soup = bs(res.content, 'html.parser')

    td = soup.find_all('td',attrs={'class':'primary_photo'}) # Scraping from the cast table
    actor_href = []

    # Appending the name of the actor and the link to the webpage
    for t in td:
        a = t.find('a')
        href = host + a.get('href')
        name = a.find('img').get('alt')
        actor_href.append({'actor':name, 'href':href})
    return actor_href # returning the list of dicts


""" 
    The method gets a link to an actor's webpage and returns a list of dicts.
    Keys: title: the name of the movie
    href: link to the webpage of the movie
 """
def getMov(url):
    host = url.split('w')[0]  + url.split('/')[2] # the host url(and scheme)

    res = requests.get(url)
    soup = bs(res.content, 'html.parser')

    knownFor = soup.find_all('div', attrs={'class':'knownfor-title-role'}) # scraping from the 'known for' table

    # appending the movies to the list
    for i in range(len(knownFor)):
        a = knownFor[i].find('a')
        knownFor[i] = {'title':a.text, 'href':host+a.get('href')}
    return knownFor #returning the list of dicts