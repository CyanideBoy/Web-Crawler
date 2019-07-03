
from urllib.request import urlopen
from link_finder import LinkFinder
from general import *
import domain

class spider:
    
    #Static Variables
    
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    email_file = ''
    emails = set()
    queue = set()
    crawled = set()
    
    def __init__(self,project_name,base_url,domain_name):
        spider.project_name=project_name
        spider.base_url=base_url
        spider.domain_name=domain_name
        spider.queue_file=spider.project_name + '/queue.txt'
        spider.crawled_file=spider.project_name + '/crawled.txt'
        spider.email_file=spider.project_name + '/emails.txt'
        
        self.boot()
        self.crawl_page('First spider',spider.base_url)

    @staticmethod
    def boot():
        create_project_dir(spider.project_name)
        create_data_files(spider.project_name,spider.base_url)
        spider.queue = file_to_set(spider.queue_file)
        spider.crawled = file_to_set(spider.crawled_file)
        spider.emails = file_to_set(spider.email_file)
        
    
    @staticmethod
    def crawl_page(thread_name,page_url):
        if page_url not in spider.crawled:
            print(thread_name+" now crawling "+page_url)
            print("Queue "+str(len(spider.queue))+ " | Crawled "+str(len(spider.crawled)))
            links,emails = spider.gather_links(page_url)
            
            spider.add_links_to_queue(links)
            spider.add_emails_to_set(emails)
            
            spider.queue.remove(page_url)
            spider.crawled.add(page_url)
            
            spider.update_files()
            
    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type').find("text/html") != -1 :
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            else:
                print("BULLLSHIT")
                print(response.getheader('Content-Type'))
            
            finder = LinkFinder(spider.base_url,page_url)
            finder.feed(html_string)
            
        except:
            print("Error: can't crawl page")
            return set(),set()
        
        return finder.page_links(),finder.page_mails()
    
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in spider.queue:
                continue
            if url in spider.crawled:
                continue
            if spider.domain_name not in url:#########
                continue
            spider.queue.add(url)
            
    @staticmethod
    def add_emails_to_set(emails):
        for u in emails:
            if u in spider.emails:
                continue
            spider.emails.add(u)
            
    @staticmethod
    def update_files():
        set_to_file(spider.queue,spider.queue_file)            
        set_to_file(spider.crawled,spider.crawled_file) 
        set_to_file(spider.emails,spider.email_file)
                
            
            
            
        
        
        
        
    
    
    
        