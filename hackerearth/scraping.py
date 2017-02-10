# # # loading dependencies
# # import requests
# # from bs4 import BeautifulSoup as bs
# #
# #
# # url = "http://mahavat.gov.in/Tin_Search/Tinsearch.jsp"
# #
# # postdata = {
# #     'tin': '27540084138V'
# # }
# # r = requests.post(url, data=postdata)
# # # print(r.encoding)
# # # print(r.status_code)
# # # print(r.text)
# # # print(type(r.text))
# #
# # soup = bs(r.text, "html.parser")
# # soup.prettify(encoding='utf-8')
# # print((soup.text))
# # # soup.text.replace('\ufffd','ccc')
# # # open('maha.html', 'a').write(soup.text)
#
#
# from selenium import webdriver
# from selenium.webdriver.support import ui
# from selenium.webdriver.common.keys import Keys
#
# def page_is_loaded(driver):
#     return driver.find_element_by_tag_name("body")!= None
#
# driver = webdriver.Chrome('')
# driver.get("http://mahavat.gov.in/Tin_Search/Tinsearch.jsp")
#
# wait = ui.WebDriverWait(driver,10)
# wait.until(page_is_loaded)
#
