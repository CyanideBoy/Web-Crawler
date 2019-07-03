
import threading
from queue import Queue
from spider import spider
from domain import *
from general import *
import sys

PROJECT_NAME = sys.argv[1]
HOMEPAGE = sys.argv[2]
DOMAIN_NAME = "https://www.ee.iitb.ac.in/web/people/faculty"

QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'

NUMBER_OF_THREADS = 4

queue = Queue()

spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)

#MAKING THREADS

def create_spiders():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target = work)
        t.daemon = True
        t.start()

def work():
    while True:
        url = queue.get()
        spider.crawl_page(threading.current_thread().name,url)
        queue.task_done()

def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0 :
        print(str(len(queued_links))+' many links in queue')
        create_jobs()        


create_spiders()
crawl()























