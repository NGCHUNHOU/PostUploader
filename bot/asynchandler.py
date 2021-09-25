import time
class asynchandler:
   def __init__(self, data): 
       self.userdata = data
   async def fbpack(self, fbobj):
       fbobj.initBrowser()
       fbobj.keyinlogin(self.userdata["markupdataset"][0], self.userdata["markupdataset"][1])
   async def fbpack1(self, fbobj):
       await self.fbpack(fbobj)
       await fbobj.keyinpost(self.userdata["accid"], self.userdata)
       time.sleep(10)
       fbobj.closeBrowser()
   async def inspack(self, instaobj):
       instaobj.initMobileBrowser()
       instaobj.inputlogin(self.userdata["instasite"], self.userdata["instaMarkupDataset"][0], self.userdata["instaMarkupDataset"][1])
   async def inspack1(self, instaobj):
       await self.inspack(instaobj)
       await instaobj.createpost(self.userdata["instaid"], self.userdata)
       time.sleep(10)
       instaobj.closeMobileBrowser()
   async def twtpack(self, twobj):
       twobj.initBrowser()
       twobj.keyinlogin(self.userdata["twtmail"], self.userdata["twtpass"])
   async def twtpack1(self, twobj):
       await self.twtpack(twobj)
       await twobj.createpost(self.userdata)
       time.sleep(10)
       twobj.closeBrowser()