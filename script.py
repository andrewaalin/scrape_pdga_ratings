import urllib.request 
import requests
from bs4 import BeautifulSoup
import re
import time

vgm_url = "https://www.discgolfscene.com/tournaments/2021_NOVA_Disc_Golf_Association_Membership_Drive_2021/registration?fbclid=IwAR37WqLoR5Al5Ac6bwOK9EGBnRgZ6OivctB9Fkiac0hSlVb2aWXjoRhh71A"

html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'html.parser')
matrix=[]
for link in soup.find_all('a'):
    linktext=link.get('href')
    match=re.findall("(www\.pdga\.com\/player\/\d+)",str(linktext))
    if len(match)>0:
        pdga_page=match[0]
        pdga_page = "http://"+pdga_page
        print(pdga_page)
        html_text = requests.get(pdga_page, verify=False).text
        soup = BeautifulSoup(html_text, 'html.parser')
        rating=re.findall("Current Rating:\S+ (\d+)",str(soup))
        person=re.findall("\"([^\"]+)\" property\=\"og:title\"",str(soup))
        if len(rating)>0 and len(person)>0:
            row=[int(rating[0]),person[0]]
            matrix.append(row)
            print(row)
matrix.sort(reverse=True)
top10=matrix[0:10]
for element in top10:
    print(str(element[0]) + " : " + element[1])
            
      
