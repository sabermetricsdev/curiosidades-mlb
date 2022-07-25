from bs4 import BeautifulSoup as bs
import requests

from itertools import product

league = ["AL", "NL"]
division = ["W", "C", "E"]
month = 8
day = 1
p = 0.5
debug = True

for year in range(1975, 2022):
  if debug:
    print(year)
  url="https://www.baseball-reference.com/boxes/?month={month}&day={day}&year={year}".format(
    year=year,
    month=month,
    day=day
  )
  soup = bs(requests.get(url).content, "html.parser")
  for l, d in product(league, division):
    for section in soup.findAll("div", {'id': 'div_standings-upto-{league}-{division}'.format(league=l, division=d)}):
      if all(map(lambda wlp: float(wlp.text) >= p, section.findAll("td", {"data-stat": "win_loss_perc"}))):
        print(year, l, d)
