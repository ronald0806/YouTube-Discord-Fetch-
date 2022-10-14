from asyncore import read
from bs4 import BeautifulSoup 
import requests
# i think you have to use youtube's api to do any of this


def make_query(parameters) -> str:   
    link_starter = 'https://www.youtube.com/results?search_query='
    parameters = parameters.strip()
    parameters = parameters.replace('+', "2B%")
    parameters = parameters.replace(' ','+')
    return link_starter+parameters



#print(make_query('megadeth - tornado of souls'))

def download_page(url):
    response = requests.get(url,allow_redirects=False)
    print(f'encoding: {response.encoding}')
    print(f'status: {response.status_code}')
    print(f'length: {len(response.text)}')
    content = response.text
    f=open('search.html','a',encoding='utf-8')
    f.write(content)
    f.close()
    
    doc = BeautifulSoup(content, 'html.parser')
#    class_tags = 'yt-simple-endpoint style-scope ytd-video-renderer'
#    for link in doc.find_all('a'):
#        print(link.get('href'))
    print(doc.title)  
    
def make_link(page):
    '''
    target:
    <a id="video-title" class="yt-simple-endpoint style-scope ytd-video-renderer" title="Megadeth - Tornado of Souls (HD)" aria-label="Megadeth - Tornado of Souls (HD) by MegaHermansen 11 years ago 5 minutes, 20 seconds 18,723,840 views" href="/watch?v=Lcm9qqo_qB0">
            <yt-icon id="inline-title-icon" class="style-scope ytd-video-renderer" hidden=""><!--css-build:shady--></yt-icon>
            <yt-formatted-string class="style-scope ytd-video-renderer" aria-label="Megadeth - Tornado of Souls (HD) by MegaHermansen 11 years ago 5 minutes, 20 seconds 18,723,840 views">Megadeth - Tornado of Souls (HD)</yt-formatted-string>
          </a>
          
    '''

query ='https://www.youtube.com/results?search_query=megadeth'
#query='https://www.google.com'
download_page(query)