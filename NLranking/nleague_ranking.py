import urllib.request
from bs4 import BeautifulSoup
import time
import os

def get_bs_obj():
    url = "http://n-league.net/team_ranking"
    html = urllib.request.urlopen(url)
    bs_obj = BeautifulSoup(html, "html.parser")
    return bs_obj

def get_file_name_as_date():
    t = time.localtime()
    file = "%04d%02d%02d.txt" % (t.tm_year, t.tm_mon, t.tm_mday)
    if os.path.isfile(file):
        os.remove(file)
    return file

bs_obj = get_bs_obj()
result = bs_obj.find("table", {"class":"brd_list"})
tr_tag = result.findAll("tr")

f = open(get_file_name_as_date(), "a")
for i in range(1,9):
    td_tag = tr_tag[i].findAll("td")
    team_name = td_tag[1].text
    team_name = team_name[0:2]
    result = "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (team_name, td_tag[3].text, td_tag[4].text, td_tag[5].text, td_tag[6].text, td_tag[9].text, td_tag[7].text, td_tag[8].text)
    f.write(result)
    # print(result)
f.close()
