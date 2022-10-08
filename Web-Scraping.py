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

#to get all the text in the particular tag we want from the url (can find any element or tag)
soup.select('p')

#can use as a list and give index value to find particular

para = soup.select('p')
para[0].getText


