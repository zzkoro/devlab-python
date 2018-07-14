import mechanize
def testProxy(url, proxy):
    browser = mechanize.Browser()
    browser.set_proxies(proxy)
    page = browser.open(url)
    source_code = page.read()
    print source_code
url = 'http://www.myipaddress.com/'
hideMeProxy = {'http': '43.249.141.114:8080'}
testProxy(url, hideMeProxy)