#File: Remote.py
#Description: Interfaces webbrowser to navigate youtube/netflix
#Author: Alex Beers

import os
import subprocess
import config
import requests
from pynput.keyboard import Key, Controller

class Remote:

    def __init__(self):
        self.k = Controller()
        subprocess.Popen(['unclutter', '-idle', '0'])
    
    def youtube(self):
        """
        Opens youtube tv app in the current window.
        """
        self.kill()
        args = []
        args.append('chromium-browser')
        args.append('--kiosk')
        args.append('--user-agent="Mozilla/5.0 (Linux; U; Tizen 2.3 ) AppleWebKit/538.1 (KHTML, like Gecko) Version/2.3 TV Safari/538.1"')
        args.append('https://youtube.com/tv')
        subprocess.Popen(args)

    def netflix(self, epid):
        """
        Opens a netflix video given its watch_code obtained through (method)
        
        Paramaters
            epid - the netflix episode id as provided by calling episodes()
        """
        self.kill()
        args = []
        args.append('chromium-browser')
        args.append('--kiosk')
        args.append('https://netflix.com/watch/' + str(epid))
        subprocess.Popen(args)

    def search_show(self, search):
        """
        Search for a show based off of its name.

        Paramaters
            search - a string to search

        Returns
            A json containing json array 'results' where each array element is a single show.
        """
        head = {'x-rapidapi-key': os.environ['API_KEY'], 'x-rapidapi-host': 'unogsng.p.rapidapi.com'}
        result = requests.get(url='https://unogsng.p.rapidapi.com/search', params={'query': search, 'limit': 5, 'countrylist': 78}, headers=head)
        return result.json()

    def episodes(self, nfid):
        """
        Search for episodes given a shows netflix id

        Paramaters
            nfid - A netflix id tied to a show

        Returns a json of an array of seasons where each season is an array of episodes
        """
        head = {'x-rapidapi-key': os.environ['API_KEY'], 'x-rapidapi-host': 'unogsng.p.rapidapi.com'}
        result = requests.get(url='https://unogsng.p.rapidapi.com/episodes', params={'netflixid': nfid}, headers=head)
        return result.json()

    def kill(self):
        """
        Kills the chromium browser
        """
        subprocess.call(['pkill', '-o', 'chromium'])

    def play_pause(self):
        """
        Simulates pressing the space key
        """
        self.k.press(Key.space)
        self.k.release(Key.space)
