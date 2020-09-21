import requests
from bs4 import BeautifulSoup as bs
import sys
from funcs import getAct, getMov

# Getting the arguments
seed_file = sys.argv[1]
depth = int(sys.argv[2])

# links is a list of every imdb movie url that is in the seed file
f = open(seed_file,'r')
links = [l.split('\n')[0] for l in f.readlines()]

# main lists
all_mov = [] # All gathered movies
all_act = [] # All gathered actors

# Iterating through the seed links list
for url in links:

    # Getting the seed movie webpage
    res = requests.get(url)
    soup = bs(res.content, 'html.parser')
    # Getting the seed movie title
    seed_title = soup.find('h1').text[:-8]

    # 
    actors = []
    a_i = 0

    movies = [{'title':seed_title, 'href':url}]
    m_i = 0

    # Getting the cast of the seed movie
    actors += getAct(url)

    # Scarping in the input depth
    while depth > 0:

        # Find movies from actors
        un_mov = movies # list of all gathered movies
        titles = [] # list of all the movies names
        s_mov = [] # list of all gathered movies, without duplicants

        # Adding scraped movies to the gathered movies list
        while a_i < len(actors):
            un_mov += getMov(actors[a_i]['href'])
            a_i += 1
        m_i += 1

        # Getting rid of duplicates
        for u in un_mov:
            if u['title'] not in titles:
                titles.append(u['title'])
                s_mov.append(u)
        movies = s_mov

        # Find actors from movies
        un_act = actors
        names = []
        s_act = []

        # Adding scraped actors to the gathred actors list
        while m_i < len(movies):
            un_act += getAct(movies[m_i]['href'])
            m_i +=1
        #a_i += 1

        # Getting rid of duplicates
        for u in un_act:
            if u['actor'] not in names:
                names.append(u['actor'])
                s_act.append(u)
        actors = s_act

        depth -= 1

    # Updating the main lists
    all_mov += [m['title'] for m in movies]
    all_act += [a['actor'] for a in actors]

# removing duplicates from the main lists
all_mov = list(dict.fromkeys(all_mov))
all_act = list(dict.fromkeys(all_act))

print('All Movies: ', all_mov)
print('All Actors: ', all_act)