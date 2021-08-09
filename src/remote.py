#File: Remote.py
#Description: Interfaces webbrowser to navigate youtube/netflix
#Author: Alex Beers

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Remote:

    def __init__(self):
        options = Options()
        options.add_argument('user-agent=Mozilla/5.0 (Linux; Tizen 2.3 ) AppleWebKit/538.1 (KHTML, like Gecko) Version/2.3 TV Safari/538.1')
        options.add_argument('--start-maximized')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.driver = webdriver.Chrome(executable_path='/lib/chromium-browser/chromedriver', options=options)
    
    def youtube(self):
        self.driver.get('https://www.youtube.com/tv')

    def netflix(self):
        self.driver.get('https://www.netflix.com')


