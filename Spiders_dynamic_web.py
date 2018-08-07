# -*- coding: cp936 -*-
from selenium import webdriver
import urllib2

def down_img(http, dirname):
    end = http.find('?')
    if end == -1:
        end = len(http)
    filepath = dirname + http[http.rfind('/'):end]
    print "保存图片:", filepath
    req = urllib2.Request(http)
    res = urllib2.urlopen(req)
    with open(filepath, 'wb') as f:
        f.write(res.read())
    res.close()
    
def get_chrome_browser():
    return webdriver.Chrome()

def main():
    dirname = "./img"
    http = "http://www.xiazaizhijia.com/rjjc/107058.html"
    chrome = webdriver.Chrome()
    chrome.get(http)
    
    img_list = chrome.find_elements_by_tag_name("img")
    for img in img_list:
        if img.get_attribute("alt") != u"宋民国表情包":
            continue
        http = img.get_attribute("src")
        print "下载图片:", http
        try:
            down_img(http, dirname)
        except Exception,e:
            print "下载失败: ", e
        
    chrome.close()
    chrome.quit()

if __name__ == '__main__':
    main()
