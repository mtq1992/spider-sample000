#coding:utf-8
'''
Created on 2016-8-4

@author: u410
'''
import urllib2


class HtmlDownloader(object):
    
    
    def download(self,url):
        if url is None:
            return None
        headers = {'Accept':'text/html, application/xhtml+xml, */*',
                   'Accept-Language':'zh-CN',
                   'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0) QQBrowser/8.2.4257.400'
                   }
        requ = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(requ,timeout=10)
        
        if response.getcode()!= 200:
            return None
        
        return response.read()
        
    
    



