'''
Created on 2017年8月19日

@author: jacob
'''
#coding:utf8
from baike import url_manager, html_downloader, html_parser, html_outputer
import urllib.parse

class SpiderMain(object):
    def __init__(self): #使用构造函数进行初始化
        self.urls = url_manager.UrlManager()    #初始化URL管理器对象
        self.downloader = html_downloader.HtmlDownloader()  #初始化下载器对象
        self.parser = html_parser.HtmlParser()  #初始化解析器对象
        self.outputer = html_outputer.HtmlOutputer()    #初始化输出器对象
        
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url) #将入口URL添加进URL管理器，这个时候URL管理器已经有了待爬取的URL
        while self.urls.has_new_url():  #启动爬虫的循环
             try:
                new_url = self.urls.get_new_url()   #获取到一个待爬去的URL
                print('craw %d : %s' % (count, urllib.parse.unquote(new_url)))    #打印当前爬取到第几条URL以及该URL的地址
                html_cont = self.downloader.download(new_url)   #利用下载器的方法来下载页面
                new_urls, new_data = self.parser.parse(new_url, html_cont)  #利用解析器来解析URL和下载好的页面
                self.urls.add_new_urls(new_urls)    #将解析的URL数据进行批量添加到URL管理器
                self.outputer.collect_data(new_data)    #利用输出器收集解析好的数据
                
                if count == 100:   #爬取1000个网页
                    break
                
                count = count + 1
             except Exception as e:  #异常处理
                 print("爬取失败:", e)
            
        self.outputer.output_html() #输出收集好的数据HTML


if __name__ == "__main__":  #主函数
    #root_url = "https://baike.baidu.com/item/Python"    #入口URL
    root_url = "https://baike.baidu.com/item/java/85979"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)