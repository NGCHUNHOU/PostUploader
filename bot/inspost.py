import asyncio
from .base import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
class inspost(base):  
    def __init__(self, userdata):
        super().__init__(userdata)
    def initMobileBrowser(self):
        print("starting mobile browser")
        useragent="Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
        profile=webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", useragent)
        self.instadriver=webdriver.Firefox(profile)
        self.instadriver.set_window_size(360,640)
    def inputlogin(self, site, eles:list, eleval:list, enter:bool=True):
        print("navigating to website "+ site)
        self.instadriver.get(site)
        self.site = site
        time.sleep(self.userdata["sleepinterval"]/2)
        # if not (self.instadriver.find_element_by_css_selector(self.userdata["instaDisLoginBtnxpath"])):
        #     lgbtn=self.instadriver.find_element_by_xpath(self.userdata["instaMobileLoginBtnxpath"])
        #     lgbtn.click()
        landlogin=1
        try:
            self.instadriver.find_element_by_xpath(self.userdata["instaMobileLoginBtnxpath"])
        except:
            landlogin=0
        print("inputing logins...")
        time.sleep(self.userdata["sleepinterval"])
        if (landlogin):
            lgbtn=self.instadriver.find_element_by_xpath(self.userdata["instaMobileLoginBtnxpath"])
            lgbtn.click()
        for num in range(len(eles)):
            logineles=self.instadriver.find_element_by_css_selector(eles[num])
            logineles.send_keys(eleval[num])
        if (enter==True):
            time.sleep(self.userdata["sleepinterval"])
            action = ActionChains(self.instadriver)
            action.send_keys(Keys.ENTER)
            action.perform()
            # self.customactions((Keys.ENTER))
        time.sleep(self.userdata["sleepinterval"]/2)
    async def createpost(self, accid, postdata):
        print("get to user profile page")
        self.instadriver.get(self.site+"/"+accid)
        time.sleep(self.userdata["sleepinterval"]/2)
        currdtime=time.strftime(self.userdata["datetimeformat"], time.localtime())
        sortedpostdata=self.sortpostschedule(postdata["instapostdataset"])
        for post in sortedpostdata:
            while(currdtime<post["schedule"]):
                await asyncio.sleep(1)
                currdtime=time.strftime(self.userdata["datetimeformat"], time.localtime())

            time.sleep(self.userdata["sleepinterval"]*2)
            postbtn=self.instadriver.find_element_by_css_selector(postdata["instapostbtn"])
            postbtn.click()
            # os.system("xdotool key ctrl+l && xdotool type "+postdata["instapostdataset"][0]+" && xdotool key KP_Enter")
            if (post["mediapath"] == ""):
                raise Exception("image is required for uploading instagram post")
            os.system("xdotool key ctrl+l && xdotool type "+post["mediapath"]+" && xdotool key KP_Enter")
            # time.sleep(self.userdata["sleepinterval"]/2)
            # next=self.instadriver.find_element_by_xpath(postdata["instanextbtn"])
            # next.click()
            # time.sleep(self.userdata["sleepinterval"]/2)
            # caption=self.instadriver.find_element_by_xpath(postdata["instacaption"]) 
            # caption.send_keys(postdata["instapostdataset"][1])
            # time.sleep(self.userdata["sleepinterval"]/2)
            # sharebtn=self.instadriver.find_element_by_xpath(postdata["instasharebtn"]) 
            # sharebtn.click()
            markupbtns=postdata["instabtns"]
            isclickortype=postdata["instaisclicktype"]
            for btnnum in range(len(markupbtns)):
                time.sleep(self.userdata["sleepinterval"])
                targetbtn=self.instadriver.find_element_by_xpath(markupbtns[btnnum])
                if (isclickortype[btnnum]==True):
                    targetbtn.click()
                else:
                    targetbtn.send_keys(post["postcontent"])
        pass
    def closeMobileBrowser(self):
        self.instadriver.close()