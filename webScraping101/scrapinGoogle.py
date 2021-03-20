import requests
import bs4
import lxml
import pdb

# res = requests.get('https://www.google.ca')
# # print(type(res))
# soup = bs4.BeautifulSoup(res.text, "lxml")
# # print(soup)
# img = soup.select('img')
# print(img)
imglink = requests.get('https://www.google.com/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png')
# print(imglink.content)
myFile = open('googleLogo.png', 'wb')
myFile.write(imglink.content)
myFile.close()
# pdb.set_trace()
# myFile = open('allAnchors.json', 'w', encoding='utf-8')
# for tag in soup.select('a'):
#     content = {
#         "textContent": str(tag.text),
#         "href": str(tag['href'])
#     }
#     content = str(content)+',\n'
#     myFile.write(content)
