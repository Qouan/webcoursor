import requests
import re
from lxml import etree
import json

new_urls=set()
old_urls=[]
'''将网页的所有汉字保存到一个字符串中'''
def html_get_chi(page_url):
    '''
    :param url: 传入网站
    :return: 中文字符串
    '''

    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'}
    r=requests.get(page_url,headers=headers)
    r.encoding='utf-8'
    html=etree.HTML(r.text)
    '''获取文本'''
    pattern = re.compile(u"[\u4e00-\u9fa5]+")
    result = re.findall(pattern, r.text)
    a=''.join(result)

    '''获取本网页的其他网址,获取50个'''
    urls=html.xpath('//a/@href')
    for url in urls[:50]:
        if len(url)<20 :
            continue
        #print(url)
        new_urls.add(url)
    return a

if __name__=='__main__':
    initial_url='http://culture.ifeng.com/'
    new_urls.add(initial_url)
    index_text={}
    i=1
    while(len(new_urls)>0 and len(old_urls)<100):
        page_url=new_urls.pop()
        '''对于无效网址，会抛出异常，continue'''
        try:
            text=html_get_chi(page_url)
        except:
            continue
        '''判断新获取的url是否访问过'''
        if page_url in old_urls:
            continue
        old_urls.append(page_url)
        print('new_urls:%d' %len(new_urls))
        print(len(old_urls))
        index_text[str(i)]=text

        i+=1
    with open('page_data.json', 'w') as f:
        json.dump(index_text, f)


