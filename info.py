import pytz
from datetime import datetime

import socket

import urllib.request as urllib
from bs4 import BeautifulSoup

import platform

class Info:
    def get_url(self):
        url = None

        server1 = 'https://www.showmyip.com/'

        url_query = urllib.build_opener()
        url_query.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0')] 

        url_query = urllib.build_opener()
        url_query.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0')] 
        
        
        # Conectando al sevidor 1
        try:
            url = url_query.open(server1, timeout=17)
            url_fetch = url.read()
            
            try:
                url_fetch = url_fetch.decode('UTF-8')
            except UnicodeDecodeError:
                url_fetch = url_fetch.decode('ISO-8859-1')

            url.close()

            return url_fetch
        except:
            print('IP query to server1 failed')

    def get_publicIP(self):
        url = self.get_url()

        soup = BeautifulSoup(url, 'html.parser')    # Parsering string to HTML
        div_ipv4 = soup.find('h2', id = "ipv4")     # Finding the h2 with the id
        ipv4 = div_ipv4.string

        return ipv4

    def get_hostname(self):
        host = socket.gethostname()
        return host

    def get_local(self):
        hostname = self.get_hostname()
        ip = socket.gethostbyname(hostname)
        return ip

    def get_ipv4(self):
        try:
            if self.get_publicIP():
                ip = self.get_publicIP()
        except:
            print('No se encontro una ip publica')

            try:
                if self.get_local():
                    ip = self.get_local()
            except:
                print('No se encontro una ip local')
        
        return ip
                
    def get_localtime(self):
        ltime = datetime.now()
        return ltime

    def get_cancuntime(self):
        tz = pytz.timezone('America/Cancun')
        ctime = datetime.now(tz)
        return ctime

    def get_os(self):
        os = platform.system()
        return os
