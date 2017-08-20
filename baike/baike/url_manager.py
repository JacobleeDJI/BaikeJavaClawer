'''
Created on 2017年8月19日

@author: jacob
'''


class UrlManager(object):   #URL管理器需要维护两个列表——带爬取的URL列表，爬取过的URL列表，在构造函数中分别初始化
    def __init__(self):
        self.new_urls = set()   #待爬去的URL
        self.old_urls = set()   #爬取过的URL
    
    def add_new_url(self, url):  #添加单个URL
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:   #说明是一个全新的URL,可以用来爬取
            self.new_urls.add(url)
    
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
    
    
    def has_new_url(self):
        return len(self.new_urls) != 0 #self.new_urls不为零说明有带爬取的URL

    
    def get_new_url(self):
        new_url = self.new_urls.pop()   #pop()方法会获取URL，并在URL列表中移除他
        self.old_urls.add(new_url)  #
        return new_url

    

    
    
    
    
    
    
    
    



