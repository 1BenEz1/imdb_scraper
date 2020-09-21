# imdb_scraper
The script pulls links to webpages of movies on IMDB and scrapes for the actors and movies connected to them.

The scripts run as so:

python3 <script.py> <seed file> <depth>

The script reads the seed file:
for each level in depth:
 for each movie - extract actors in cast
  for each actors extract movie

print the list of movies you gathered
print the list of actors you gathered
