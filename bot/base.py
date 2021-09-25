from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
class base:
    def __init__(self, txt):
        super(base, self).__init__()
        self.userdata = txt 
        self.driver = any
        pass
    def initBrowser(self):
        print("starting browser")
        driver = webdriver.Firefox() 
        self.driver = driver
    def navigate(self, website:str):
        self.driver.get(website)
        return self.driver
    def closeBrowser(self):
        self.driver.close()
    def customactions(self, inputlist:list):
        actiondict={}
        for inputnum in range(len(inputlist)):
            actiondict["action"+str(inputnum)]=ActionChains(self.driver)
            actiondict["action"+str(inputnum)].send_keys(inputlist[inputnum])
            actiondict["action"+str(inputnum)].perform()
    def sortpostschedule(self, postlist):
        for i in range(0, len(postlist)):
            for j in range(i+1, len(postlist)):
                if (postlist[i]["schedule"]>postlist[j]["schedule"]):
                    temp=postlist[i]
                    postlist[i]=postlist[j]
                    postlist[j]=temp
        return postlist       