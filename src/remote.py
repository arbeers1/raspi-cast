#File: Remote.py
#Description: Interfaces webbrowser to navigate youtube/netflix
#Author: Alex Beers

from selenium import webdriver
import time

class Remote:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/lib/chromium-browser/chromedriver')
    
    def youtube(self):
        self.driver.get('https://www.youtube.com')

    def netflix(self):
        self.driver.get('https://www.netflix.com')


