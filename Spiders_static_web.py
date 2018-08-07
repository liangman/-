# -*- coding: cp936 -*-
import urllib2
import re

def get_html(http):
    req = urllib2.Request(http)
    res = urllib2.urlopen(req)
    buf = res.read()
    res.close()
    return buf

def get_img_list(html):
    img_re = re.compile('<img[ ]+src[ ]*=[ ]*"([^"]+)"')
    return img_re.findall(html)

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

def main():
    dirname = "./img"
    http = 'http://www.xiazaizhijia.com/rjjc/107058.html'
    html = get_html(http)
    img_list = get_img_list(html)
    for img in img_list:
        print "下载图片:", img
        try:
            down_img(img, dirname)
        except Exception,e:
            print "下载失败: ", e
    
if __name__ == '__main__':
    main()
