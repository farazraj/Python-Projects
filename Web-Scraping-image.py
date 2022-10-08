# To get a text from a webpage using requests, beautiful soup and lxml libraries.
# to use these librabies first need to install these using (pip install) command from command prompt/terminal in respective plattforms.
import requests
import bs4    # beautiful soup library
result = requests.get('https://toscrape.com/')   #request to get the html format of the url provided

# will give u a text format of the url provided
result.text   

# to change that text in a readable format
soup = bs4.BeautifulSoup(result.text, "lxml") 

# will give sorted html format of the url
soup 

#to get all the text in the particular class(. is used  for the class) we want from the url (can find any element or tag)
soup.select('.img-thumbnail')

#can use as a list and give index value to find particular image source
img = soup.select('.img-thumbnail')[0]
para['src']

#after getting the desired img url request to get the image and add https: in front or if a . appears it means its in the native webpage. 
image = requests.get('https://toscrape.com/img/books.png')

#will give u binary content of the image
image.content

#write a jpeg or png file to convert this content into an image and saving on the device

with open ('books.jpg','wb') as f: #give name and complete url where to save the image, wb stands for writing binary
    f.write(image.content)
    f.close()
