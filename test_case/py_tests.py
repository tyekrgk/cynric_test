from requests_html import HTMLSession

session = HTMLSession()

r = session.get('https://news.cnblogs.com/n/recommend')

#获取页面上的所有连接
news = r.html.find('h2.news_entry > a')

for i in news:
    print(i.text)
    print(i.absolute_links)
# #获取页面上的所有链接,以绝对路劲的方式
# all_absolute_links = r.html.absolute_links
#
# print(all_absolute_links)