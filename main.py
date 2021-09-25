from bot.inspost import inspost
import bot
import json
import os
import asyncio
# async def repack(instaobj, data):
#     instaobj.initMobileBrowser()
#     instaobj.inputlogin(data["instasite"], data["instaMarkupDataset"][0], data["instaMarkupDataset"][1])
# async def repack1(instaobj, data):
#     await repack(instaobj, data)
#     await instaobj.createpost(data["instaid"], data)
#     time.sleep(10)
#     instaobj.closeMobileBrowser()
# async def twpack(twobj, data):
#     twobj.initBrowser()
#     twobj.keyinlogin(data["twtmail"], data["twtpass"])
# async def twpack1(twobj, data):
#     await twpack(twobj, data)
#     await twobj.createpost(data["twtpostdataset"])
#     time.sleep(10)
#     twobj.closeBrowser()

async def main():
    if (os.path.isfile("DataList.json")):
        with open("DataList.json") as data:
            customdata=json.load(data)
        # autobot = bot.fbpost(customdata)
        # autobot.initBrowser()
        # autobot.keyinlogin(customdata["markupdataset"][0], customdata["markupdataset"][1])
        # # autobot.keyinpost(customdata["accid"], customdata["fbpostelexpath"], customdata["fbpostbtnxpath"])
        # autobot.keyinpost(customdata["accid"], customdata)
        # time.sleep(10)
        # autobot.closeBrowser()

        # instagram prevents uploading video
        # insbot=bot.inspost(customdata)
        # insbot.initMobileBrowser()
        # insbot.inputlogin(customdata["instasite"], customdata["instaMarkupDataset"][0], customdata["instaMarkupDataset"][1])
        # time.sleep(10)
        # insbot.closeMobileBrowser()
        asyncman=bot.asynchandler(customdata)
        fbobj=bot.fbpost(customdata)
        instaobj=bot.inspost(customdata)
        twtbot=bot.twtpost(customdata)
        task1=asyncman.fbpack1(fbobj)
        task2=asyncman.inspack1(instaobj)
        task3=asyncman.twtpack1(twtbot)
        t1=loop.create_task(task1)
        t2=loop.create_task(task2)
        t3=loop.create_task(task3)
        await asyncio.wait([t1,t2, t3])

        # twtbot=bot.twtpost(customdata)
        # twtbot.initBrowser()
        # twtbot.keyinlogin(customdata["twtmail"], customdata["twtpass"])
        # twtbot.createpost(customdata["twtpostdataset"])
        # time.sleep(10)
        # twtbot.closeBrowser()
        # target=customdata["fbpostdataset"]
        # for num in range(0, len(target)):
        #     for nu in range(num+1, len(target)):
        #         if (target[num]["schedule"]>target[nu]["schedule"]):
        #             temp=target[num]
        #             target[num]=target[nu]
        #             target[nu]=temp
        # print(target)
    else:
        print("DataList.json not found")

if __name__ == "__main__":
    loop=asyncio.get_event_loop()
    loop.run_until_complete(main())