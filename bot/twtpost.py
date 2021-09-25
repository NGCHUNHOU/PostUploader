from os import sched_get_priority_max
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from .base import *
import asyncio

class twtpost(base):
    def __init__(self, userdata):
        super().__init__(userdata)
    def keyinlogin(self, mail, password):
        print("navigating to website "+ self.userdata["twtsite"])
        driver = self.navigate(self.userdata["twtsite"])
        driver.get(self.userdata["twtsite"]+"/"+self.userdata["twtloginPath"])
        time.sleep(self.userdata["sleepinterval"])
        passele=1
        try:
            self.driver.find_element_by_xpath(self.userdata["twtpassele"])
        except:
            passele=0
        # action = ActionChains(driver)
        # action.send_keys(mail+Keys.ENTER)
        # action.perform()
        self.customactions((mail+Keys.ENTER))
        time.sleep(self.userdata["sleepinterval"])
        if (passele):
            # action = ActionChains(driver)
            # action.send_keys(Keys.TAB)
            # action.perform()
            # action2 = ActionChains(driver)
            # action2.send_keys(password+Keys.ENTER)
            # action2.perform()
            self.customactions((Keys.TAB, password+Keys.ENTER))
            pass
        else:
            # action = ActionChains(driver)
            # action.send_keys(mail+Keys.ENTER)
            # action.perform()
            self.customactions((mail+Keys.ENTER))
            time.sleep(self.userdata["sleepinterval"])
            # action2 = ActionChains(driver)
            # action2.send_keys(password+Keys.ENTER)
            # action2.perform()
            self.customactions((password+Keys.ENTER))
    async def createpost(self, twtdataset):
        print("get to user profile page")
        time.sleep(self.userdata["sleepinterval"]/2)
        sortedpostdata=self.sortpostschedule(twtdataset["twtpostdataset"])
        for twtdata in sortedpostdata:
            time.sleep(self.userdata["sleepinterval"]/2)
            currdtime=time.strftime(self.userdata["datetimeformat"], time.localtime())
            while (currdtime<twtdata["schedule"]):
                await asyncio.sleep(1)
                currdtime=time.strftime(self.userdata["datetimeformat"], time.localtime())
            swt=1
            if (swt):
                if (twtdata["mediapath"] != ""):
                    # "fbimagebtn": "div[aria-label='Photo/Video']",
                    mediainput=self.driver.find_element_by_css_selector(self.userdata["twtmediainputele"])
                    mediainput.send_keys(twtdata["mediapath"])
                    pass
                else:
                    print("the post has not image")
                    pass
            time.sleep(self.userdata["sleepinterval"]/2)
            posttextblock=self.driver.find_element_by_css_selector("div[aria-label='Tweet text']")
            posttextblock.click()
            posttextblock.send_keys(twtdata["postcontent"])
            time.sleep(self.userdata["sleepinterval"]/2)
            postbtn=self.driver.find_element_by_css_selector("div[role='button'][data-testid='tweetButtonInline']")
            postbtn.click()