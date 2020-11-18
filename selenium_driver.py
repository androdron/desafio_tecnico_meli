import time
import random
import csv
import unidecode
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
#Action keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import TimeoutException

import requests
from lxml.html import fromstring

def get_proxies():
    url = 'https://free-proxy-list.net/anonymous-proxy.html'#'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:20]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            #Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return list(proxies)
def get_socks():
    url = 'https://www.socks-proxy.net/'#'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:20]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            #Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return list(proxies)

user_agents = []
with open('./user_agents.txt','r') as ua_ls:
    for item in ua_ls.readlines():
        if len(item) > 2:
            user_agents.append(item)
            
def setProxy(user_agent_ls=user_agents,headless=False):
    #try:
    ##port_web = 10000
    #hproxy = get_proxies()[2000]
    ##prox = Proxy()
    ##prox.proxy_type = ProxyType.MANUAL
    ##prox.http_proxy = 'us.smartproxy.com:%d'%port_web
    #prox.socks_proxy = proxa+':'+por
    ##prox.ssl_proxy = 'us.smartproxy.com:%d'%port_web

    capabilities = webdriver.DesiredCapabilities.CHROME
    ##prox.add_to_capabilities(capabilities)
    #except:
    #    capabilities = webdriver.DesiredCapabilities.CHROME
    
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=es")
    if headless == True:
        options.add_argument("--headless")  
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1920,1080")
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US',
                                             "profile.managed_default_content_settings.images": 2,
                                              "disk-cache-size": 9192,})
    options.add_argument("user-agent=%s"%random.choice(user_agents))
    driver = webdriver.Chrome('./chromedriver.exe',desired_capabilities=capabilities,chrome_options=options)
    return driver


