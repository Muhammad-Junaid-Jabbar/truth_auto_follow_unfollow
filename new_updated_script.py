import time 
import csv
import subprocess
try:
    import pandas
except (ImportError, NameError, RuntimeError, ModuleNotFoundError):
    subprocess.run(["pip", "install", "pandas"])


try:
    import openpyxl
except (ImportError, NameError, RuntimeError, ModuleNotFoundError):
    subprocess.run(["pip", "install", "openpyxl"])

try:
    from selenium import webdriver
except (ImportError, NameError, RuntimeError, ModuleNotFoundError):
    subprocess.run(["pip", "install", "selenium"])
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


try:
    import requests
except (ImportError, NameError, RuntimeError, ModuleNotFoundError):
    subprocess.run(["pip", "install", "requests"])


web = webdriver.Chrome()

web.get("https://instantusername.com/#/")

time.sleep(3)

f = open('selected.csv','w',newline='')
header = ['firstname','lastname']
writer =csv.DictWriter(f,fieldnames=header)

excel_data = pandas.read_excel('data.xlsx')
count = 0
text_enter = web.find_element_by_xpath('//*[@id="jumbotron"]/div/span/input')
for column in excel_data["firstname"].tolist():
    text = str(excel_data["firstname"][count])  +  str(excel_data["lastname"][count])
    print(text)
    text_enter.send_keys(text)
    # text_enter.send_keys(Keys.ENTER)
    time.sleep(3)
    web.execute_script("window.scrollTo(0,100)")
    time.sleep(3)
    web.execute_script("window.scrollTo(0,500)")
    time.sleep(3)
    web.execute_script("window.scrollTo(0,1500)")
    time.sleep(3)
    web.execute_script("window.scrollTo(0,3000)")
    time.sleep(3)
    web.execute_script("window.scrollTo(0,6000)")
    time.sleep(3)
    # submit = web.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div/div[1]/div/div/div/div/div/div/button')
    # submit.click()
    time.sleep(1)
    web.execute_script("window.scrollTo(10000,0)")
    instagram_status = web.find_element_by_css_selector("#content > div > a:nth-child(1) > div > div.description > span").text
    print("instagram",instagram_status)
    tiktok_status = web.find_element_by_css_selector("#content > div > a:nth-child(2) > div > div.description > span").text
    print("tiktok",tiktok_status)
    twitter_status = web.find_element_by_css_selector("#content > div > a:nth-child(3) > div > div.description > span").text
    print("twitter",twitter_status)
    facebook_status = web.find_element_by_css_selector("#content > div > a:nth-child(4) > div > div.description > span").text
    print("facebook",facebook_status)
    youtube_status = web.find_element_by_css_selector("#content > div > a:nth-child(5) > div > div.description > span").text
    print("youtube",youtube_status)
    pinterest_status = web.find_element_by_css_selector("#content > div > a:nth-child(93) > div > div.description > span").text
    print("pinterest",pinterest_status)
    reddit_status = web.find_element_by_css_selector("#content > div > a:nth-child(7) > div > div.description > span").text
    print("reddit",reddit_status)


    def snapchat_username_checker(username1):

        url = "https://accounts.snapchat.com:443/accounts/get_username_suggestions"
        # DONT CHANGE
        headers = {"Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\"", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                "Accept": "*/*", "Origin": "https://accounts.snapchat.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "same-origin", "Sec-Fetch-Dest": "empty", "Referer": "https://accounts.snapchat.com/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
        xsrf_token = "JxVkpuY3VbHfOFagfT0csQ"
        cookies = {"xsrf_token": xsrf_token}


        def single_request(username):
            data = {"requested_username": username,
                    "xsrf_token": xsrf_token}
            res = requests.post(url, headers=headers,
                                cookies=cookies, data=data)
            if "TAKEN" in res.text:
                return "Taken"
            elif "OK" in res.text:
                return "Available"  
            else:
                return "Taken"
        return str(single_request(username1))
    snapchat_status = snapchat_username_checker(str(text))
    print("snapchat",snapchat_status)
    if (twitter_status == "Available") & (instagram_status == "Available") & (snapchat_status == "Available") & (tiktok_status == "Available") & (facebook_status == "Available") & (pinterest_status == "Available") & (reddit_status == "Available") & (youtube_status == "Available"):
        writer.writerow({'firstname':str(excel_data["firstname"][count]),'lastname':str(excel_data["lastname"][count])})
    count = count + 1
    text_enter.clear()
web.close()
f.close()
