from bot.inspost import inspost
import bot
import json
import os
import time

def main():
    if (os.path.isfile("DataList.json")):
        with open("DataList.json") as data:
            customdata=json.load(data)
        autobot = bot.fbpost(customdata)
        autobot.initBrowser()
        autobot.keyinlogin(customdata["markupdataset"][0], customdata["markupdataset"][1])
        # autobot.keyinpost(customdata["accid"], customdata["fbpostelexpath"], customdata["fbpostbtnxpath"])
        autobot.keyinpost(customdata["accid"], customdata)
        time.sleep(10)
        autobot.closeBrowser()

        # instagram prevents uploading video
        insbot=bot.inspost(customdata)
        insbot.initMobileBrowser()
        insbot.inputlogin(customdata["instasite"], customdata["instaMarkupDataset"][0], customdata["instaMarkupDataset"][1])
        insbot.createpost(customdata["instaid"], customdata)
        time.sleep(10)
        insbot.closeMobileBrowser()

        twtbot=bot.twtpost(customdata)
        twtbot.initBrowser()
        twtbot.keyinlogin(customdata["twtmail"], customdata["twtpass"])
        twtbot.createpost(customdata["twtpostdataset"])
        time.sleep(10)
        twtbot.closeBrowser()

    else:
        print("DataList.json not found")

if __name__ == "__main__":
    main()