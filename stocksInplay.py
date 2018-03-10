from selenium import webdriver
import re

driver = webdriver.PhantomJS()
url = r"http://hosting.briefing.com/cschwab/InDepth/InPlay.htm"
# 打开本地文件，需要用firefox，chrom里面看到的网络路径
#url = r"file:///D:/pythonProgram/pCrawler/stocksInplay.htm"
driver.get(url)
driver.implicitly_wait(3)  # 等待网页加载完成

stocks_pattern = re.compile(r'^[A-Z]{1,5}\s')
stocks_elements = driver.find_elements_by_class_name("storyTitle")

stock_set = set()
for stock in stocks_elements:
    res = re.match(stocks_pattern, stock.text)
    if res:
        tt = res.group().strip()
        stock_set.add(tt)


stock_set_exclude = set(
    ['BONDX', 'FOREX', 'QQQ', 'SPY', 'SCANX', 'SUMRX', 'WIRES', 'WRAPX'])  # 不是真的股票
stocksInplay_set = stock_set - stock_set_exclude
print('stock inplay len:')
print(len(stocksInplay_set))
print(stocksInplay_set)


# 查找高开低开的股票
stocks_pattern = re.compile(r'^[A-Z]{1,5}$')
stocks_gaping_elements = driver.find_elements_by_tag_name('strong')

stocks_gaping_set = set()
for stock in stocks_gaping_elements:
    res = re.match(stocks_pattern, stock.text)
    if res:
        tt = res.group().strip()
        stocks_gaping_set.add(tt)

print('stock gapping (len):')
print(len(stocks_gaping_set))
print(stocks_gaping_set)

# 把inplay的股票写进 1.stk,超过200个就写到1.2.stk， 高开低开的写进去2.stk
with open(r'C:\Users\Administrator\Desktop\1.stk', 'wt') as f:
    for l in stocksInplay_set:
        f.writelines(l)
        f.write('\n')


with open(r'C:\Users\Administrator\Desktop\2.stk', 'wt') as f:
    for l in stocks_gaping_set:
        print(l, file=f)
