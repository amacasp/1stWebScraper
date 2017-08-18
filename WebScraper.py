import lxml
import requests
from bs4 import BeautifulSoup

class Link():

    def __init__(self):
        self.link = "No input"
        self.found_links = False
        self.connected_link = None
        self.all_connected_links = list()
        self.link_entered = False
        self.input_link()

    def input_link(self):
        if self.link_entered != True:
            self.running = True
            self.action = False
        else:
            self.action = True
        while self.running:
            self.link = input("Enter a link: ")
            self.link_entered = True
            self.running = False
            self.action = True
        while self.action:
            self.request_link()
            choice = input("What would you like to do with this link? ")
            if choice == "print_connected_list":
                action = False
                self.print_connected_list()
            if choice == "print_page":
                action = False
                self.print_page()
            if choice == "find_connected_links":
                action = False
                self.find_connected_links()

    def request_link(self):
        self.page = requests.get(self.link)
        self.soup = BeautifulSoup(self.page.text, 'lxml')

    def print_page(self):
        print (self.soup.prettify())
        self.input_link()

    def find_connected_links(self):
        if self.found_links == False:
            for self.connected_link in self.soup.find_all('a'):
                self.connected_link = self.connected_link.get('href')
                self.all_connected_links.append(self.connected_link)
                print self.connected_link
            self.found_links = True
            self.input_link()
        else:
            print "Already found all links"
            self.input_link()

    def print_connected_list(self):
        if len(self.all_connected_links) == 0:
            print "Try calling the find_connected_links command first"
            self.input_link()
        else:
            print self.all_connected_links
            self.input_link()

web_scraper = Link()

