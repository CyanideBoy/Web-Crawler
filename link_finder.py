

from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):
    
    def __init__(self,base_url,page_url):
        super().__init__()
        self.base_url= base_url
        self.page_url=page_url
        self.links=set()
        self.mails=set()
        self.Flag = False
        self.find='[AT]'
        
    def handle_starttag(self,tag,attrs):
        if tag == 'a':
            for (attribute,value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url,value)
                    self.links.add(url)
        
    def handle_data(self, data):
        arr = data.split(' ')
        for s in arr:
            if self.find in s: 
                email = s.replace(self.find,'@')
                self.mails.add(email)
                
    
    def page_links(self):
        return self.links

    def page_mails(self):
        return self.mails

    def error(self,message):
        pass
    














