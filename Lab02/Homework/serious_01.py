from urllib.request import urlopen
from bs4 import  BeautifulSoup
import pyexcel

url = 'https://www.apple.com/itunes/charts/songs/'
html_content = urlopen(url).read().decode('utf-8')

soup = BeautifulSoup(html_content, 'html.parser')

sec = soup.find('section', 'section chart-grid')

li_list = sec.find_all('li')

data = []

for li in li_list :
    post = {}

    post['Name'] = li.h3.string
    post['Artist'] = li.h4.string
    data.append(post)

pyexcel.save_as(records=data, dest_file_name="Top100songs.xlsx")    