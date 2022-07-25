from bs4 import BeautifulSoup as bs
import requests

from itertools import product

league = ["AL", "NL"]
division = ["W", "C", "E"]

for year in range(1975, 2022):
  print(year)
  url="https://www.baseball-reference.com/boxes/?month=8&day=1&year={year}".format(year=year)
  soup = bs(requests.get(url).content, "html.parser")
  for l, d in product(league, division):
    for section in soup.findAll("div", {'id': 'div_standings-upto-{league}-{division}'.format(league=l, division=d)}):
      if all(map(lambda wlp: float(wlp.text) >= 0.5, section.findAll("td", {"data-stat": "win_loss_perc"}))):
        print(year, l, d)
