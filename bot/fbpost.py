from os import sched_get_priority_max
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import asyncio
from .base import *

class fbpost(base):
    def __init__(self, userdata):
        super().__init__(userdata)
    def keyinlogin(self, eles:list, DataList:list, enter:bool=True):
        print("navigating to website "+ self.userdata["website"])
        driver = self.navigate(self.userdata["website"])
        print("inputing logins...")
        for num in range(len(eles)):
            solideles = driver.find_element_by_css_selector(eles[num])
            solideles.send_keys(DataList[num])
        if (enter==True):
            # action = ActionChains(driver)
            # action.send_keys(Keys.ENTER)
            # action.perform()
            self.customactions((Keys.ENTER))
        time.sleep(self.userdata["sleepinterval"])
    async def handlepostcontent(self, fblist:list):
        time.sleep(self.userdata["sleepinterval"])
        # for data in dataset["fbpostdataset"]:
        currdtime=time.strftime(self.userdata["datetimeformat"], time.localtime())
        while (currdtime<fblist["schedule"]):
            await asyncio.sleep(1)
            currdtime=time.strftime(self.userdata["datetimeformat"], time.localtime())
        dialog=1
        try:
            self.driver.find_element_by_css_selector("div[role='dialog']")
        except:
            dialog=0
        swt=1
        if (swt and dialog and fblist["mediapath"] != ""):
            # "fbimagebtn": "div[aria-label='Photo/Video']",
            imagebtn=self.driver.find_element_by_css_selector(self.userdata["fbimageinput"])
            imagebtn.send_keys(fblist["mediapath"])
            tabnum=self.userdata["steptopostbtn"]+1
            pass
        else:
            print("the post has not image")
            if "http" in fblist["postcontent"]:
                tabnum=self.userdata["steptopostbtn"]+1
                pass
            else: 
                tabnum=self.userdata["steptopostbtn"]
        if (swt and dialog):
            time.sleep(self.userdata["sleepinterval"])
            self.customactions((fblist["postcontent"]))
            time.sleep(self.userdata["sleepinterval"]/2)
            self.customactions((Keys.TAB*tabnum))
            time.sleep(self.userdata["sleepinterval"]/2)
            self.customactions((Keys.ENTER))
        else:
            ele=self.driver.find_element_by_xpath(self.userdata["fbpostelexpath"])
            ele.click()
            time.sleep(self.userdata["sleepinterval"])
            self.customactions((fblist["postcontent"]))
            time.sleep(self.userdata["sleepinterval"]/2)
            self.customactions((Keys.TAB*tabnum))
            time.sleep(self.userdata["sleepinterval"]/2)
            self.customactions((Keys.ENTER))

        # action2 = ActionChains(self.driver)
        # action2.send_keys(Keys.ENTER)
        # action2.perform()
        # blockui=self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div[2]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div/div[1]/div/span")
        # self.driver.execute_script("arguments[0].style.visibility = 'hidden'", blockui)
        # postbtn=self.driver.find_element_by_xpath(dataset["fbpostbtnxpath"])
        # postbtn.click()
        # action2 = ActionChains(self.driver)
        # action2.send_keys(Keys.ENTER)
        # action2.perform

    # def keyinpost(self, accid, fbpostele, fbpostbtn):
    async def keyinpost(self, accid, fbpostdata:dict):
        print("get to user profile page")
        self.driver.get(self.userdata["website"]+"/"+accid)
        time.sleep(self.userdata["sleepinterval"]/2)
        ele=self.driver.find_element_by_xpath(fbpostdata["fbpostelexpath"])
        ele.click()
        sortedpostlist=self.sortpostschedule(fbpostdata["fbpostdataset"])
        for data in sortedpostlist:
            print("pending to create post content")
            await self.handlepostcontent(data)
        # action = ActionChains(self.driver)
        # action.send_keys("testing")
        # action.perform()
        # postbtn=self.driver.find_element_by_xpath("//*[text()='Post']")
        # postbtn=self.driver.find_element_by_xpath(fbpostdata["fbpostbtnxpath"])
        # postbtn.click()
    
    # def wait_until(self, somepredicate):
    #     currdtime=time.strftime(self.userdata["datetimeformat"], time.localtime())
    #     while currdtime<somepredicate:
    #         if currdtime>somepredicate: return True
    #     return False