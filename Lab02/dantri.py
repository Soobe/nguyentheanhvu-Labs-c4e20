from urllib.request import urlopen
from bs4 import  BeautifulSoup
import pyexcel
# 1.Download web page

url = 'http://dantri.com.vn'
html_content = urlopen(url).read().decode('utf-8')
# # 1.1 Create a collection
# conn = urlopen(url)

# # 1.2 Read
# data = conn.read()
# print(data)

# # 1.3 Decode
# html_content = data.decode('utf-8')

# print(html_content)

# save html to file
# f = open('dantri.html','wb',)
# f. write(html_content)
# f.close()


# 2.Extract ROI ( Region of interest)
soup = BeautifulSoup(html_content, 'html.parser')
# find by class
ul = soup.find('ul', 'ul1 ulnew')

# print(ul.prettify())

# 3.Extract data
li_list = ul.find_all('li')

data = []
for li in li_list:
    post = {}
    a = li.h4.a
    post['tittle']= a.string
    post['url']= url + a['href']

    data.append(post)
    # li = li_list[0]
    # # Viết gọn : a = li.h4.a
    # h4 = li.find('h4')
    # a = h4.find('a')
    # print(a.string)
    # print(url + a['href'])
    # print("*" * 30)

pyexcel.save_as(records=data, dest_file_name="dantripy.xlsx")





