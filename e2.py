import requests
from bs4 import BeautifulSoup as bs

for line in open("ELECTION-ID"):
    a = line.split()
    file_name = a[0] +".csv"
    addr = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/".format(a[1])
    resp = requests.get(addr)
    html = resp.content
    soup = bs(html, "html.parser")
    with open(file_name, "w") as out:
        out.write(resp.text)
