'''
Created on 2017年8月19日

@author: jacob
'''
import ssl
import urllib.request
ssl._create_default_https_context = ssl._create_unverified_context

class HtmlDownloader(object):
    
    
    def download(self, url):
        if url is None:
            return None
        
        
        head = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        resp = urllib.request.urlopen(url)
        if resp.getcode() != 200:
            return None
        resp.encoding = 'utf-8'
        return resp.read()
    



