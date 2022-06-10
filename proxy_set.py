import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

make_database()
web = webdriver.Chrome()
web.get("https://google.com")
# login webpage
web.get("https://truthsocial.com/login")
# enter username
username_text_box = web.find_element_by_xpath(
    "/html/body/div/div[1]/main/div/div/div/div/div/div/div[2]/form/div[1]/div/div/input"
)
user_email = "ilijevskan@gmail.com"
username_text_box.send_keys(user_email)
time.sleep(3)
# enter password
userpass_text_box = web.find_element_by_xpath(
    "/html/body/div/div[1]/main/div/div/div/div/div/div/div[2]/form/div[2]/div/div/input"
)
user_pass = "Natal1jatruth"
userpass_text_box.send_keys(user_pass)
time.sleep(3)
# click login
button = web.find_element_by_xpath(
    "/html/body/div/div[1]/main/div/div/div/div/div/div/div[2]/form/div[3]/button"
)
button.send_keys(Keys.ENTER)
time.sleep(3)
for i in range(1, 3):

    # script to follow th users
    count = 1
    user = web.find_element_by_xpath(
        "/html/body/div/div[1]/div/div[2]/div[1]/div/main/div/div/div[2]/div/div[3]/div[2]/div[1]/div/div[2]/div["
        + str(count)
        + "]/div/div/div[1]/div/span/a/div/p"
    )
    user.click()
    time.sleep(3)
    status = web.find_element_by_css_selector(
        "#soapbox > div:nth-child(1) > div > div.z-10.flex.flex-col > div.sm\:pt-4.relative > div > main > div > div > div > div > div.mt-6.min-w-0.flex-1.sm\:px-2 > div > div.flex.items-center.space-x-3 > a:nth-child(1) > div > p.text-sm.text-primary-600.dark\:text-primary-400.font-bold.tracking-normal.font-sans.normal-case > span"
    ).text
    print("status", status)

    if "K" in status:
        if float(status.split("K")[0]) >= 100:
            print("user is in follow status")
            web.find_element_by_xpath(
                "/html/body/div/div[1]/div/div[2]/div[1]/div/main/div/div/div/div/div[1]/div[2]/div/div[2]/div/button[2]"
            ).click()
            time.sleep(3)
            following_name = web.find_element_by_css_selector(
                "#soapbox > div:nth-child(1) > div > div.z-10.flex.flex-col > div.sm\:pt-4.relative > div > main > div > div > div > div > div.mt-6.min-w-0.flex-1.sm\:px-2 > div > div:nth-child(1) > div.flex.items-center.space-x-0\.5 > p"
            ).text
            add_followed_user_to_file(following_name)
            print("following", following_name)
    else:
        count = count + 1

    web.get("https://truthsocial.com/search")
    time.sleep(3)


def add_followed_user_to_file(a):
    # Open a file with access mode 'a'
    file_object = open("follow_list.txt", "a")
    # Append 'hello' at the end of file
    file_object.write(str(a) + "\n")
    # Close the file
    file_object.close()


def make_database():
    # Open a file with access mode 'a'
    file_object = open("follow_list.txt", "w+")
    # Append 'hello' at the end of file
    file_object.write("followers list" + "\n")
    # Close the file
    file_object.close()
