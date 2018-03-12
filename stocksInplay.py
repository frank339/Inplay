from selenium import webdriver
import re

driver = webdriver.PhantomJS()
#url = r"http://hosting.briefing.com/cschwab/InDepth/InPlay.htm"
# 打开本地文件，需要用firefox，chrom里面看到的网络路径
url = r"file:///D:/pythonProgram/pCrawler/Inplay/stocksInplay.htm"
driver.get(url)
driver.implicitly_wait(3)  # 等待网页加载完成

stocks_pattern = re.compile(r'^[A-Z]{1,5}\s')
#stocks = driver.find_elements_by_class_name("storyTitle")
inplay_tr = driver.find_elements_by_xpath(
    '//*[@id="Content"]/table/tbody/tr/td[2 and @class="storyTitle"]')

stock_set = set()
for inplay in inplay_tr:
    stocks = re.match(stocks_pattern, inplay.text)
    if stocks:
        stock_set.add(stocks.group().strip())

stock_set_exclude = set(
    ['BONDX', 'FOREX', 'QQQ', 'SPY', 'SCANX', 'SUMRX', 'WIRES', 'WRAPX'])  # 不是真的股票
stocksInplay_set = stock_set - stock_set_exclude
print('stock inplay len:{0:10d}'.format(len(stocksInplay_set)))
print(stocksInplay_set)


# 把inplay的股票写进 1.0.stk,超过200个就写到1.2.stk
def write_list2file(l, path):
    with open(path, 'wt') as f:
        for element in l:
            print(element, file=f)
        f.close()


stocksInplay_list = list(stocksInplay_set)
file_number = 0
stocks_number_all = len(stocksInplay_list)
stocks_in_a_file = 200

for index in range(0, stocks_number_all, stocks_in_a_file):
    if(index < stocks_number_all):
        file_number = index//stocks_in_a_file
        path = r"C:\Users\Administrator\Desktop\1." + \
            str(file_number) + r".stk"
        print("index %d\n file_number %d\n path %s" %
              (index, file_number, path))
        write_list2file(stocksInplay_list[index:index+stocks_in_a_file], path)


# 高开低开的写进去2gappingup.stk,3gappingdown.stk
gapping_up_tr = driver.find_elements_by_xpath(
    '//*[@id="Content"]/table/tbody/tr/td[p//*[contains(text(),"Gapping up")]]//strong[text()]')
with open(r'C:\Users\Administrator\Desktop\2gappingup.stk', 'wt') as f:
    for gapping_up in gapping_up_tr:
        print(gapping_up.text, file=f)

gapping_down_tr = driver.find_elements_by_xpath(
    '//*[@id="Content"]/table/tbody/tr/td[./p//*[contains(text(),"Gapping down")]]//strong[text()]')
with open(r'C:\Users\Administrator\Desktop\3gappingdown.stk', 'wt') as f:
    for gapping_down in gapping_down_tr:
        print(gapping_down.text, file=f)


# 在浏览器打开网页
import webbrowser
webbrowser.open_new_tab(url)
