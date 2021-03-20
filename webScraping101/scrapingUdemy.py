import requests
import bs4
import lxml

# name: Its just to give distinct temp names
name = 0
# Udemy.com
url = 'https://www.udemy.com'
res = requests.get(url)
# making soup object for fetching data
soup = bs4.BeautifulSoup(res.text, 'lxml')
# will select and return list of all <img> tags for that page
imgList = soup.find_all('img')
# parsing list elements
for img in imgList:
    # fetch value of "src" attribute
    imgUrl = img["src"]
    # type check
    if '.jpg' in imgUrl or '.png' in imgUrl:
        # fetching the actual image now. Ooyeah!!
        imgContent = requests.get(imgUrl)
        # make a new file in a local directory 'Udemy Images'
        # pay attention to the 'wb' Binary part !!!
        myFile = open(f'./UdemyImages/{str(name)}.jpeg', mode='wb')
        name+=1
        # writing content as binary
        myFile.write(imgContent.content)
        # close file
        myFile.close()
        '''
        are we done yet 
        > no
        wtf? 
        > go on for the next iteration
        :\
        '''
# Finally yay we're done now
# check your directory
