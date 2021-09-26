# PostUploader
Automatically upload your posts to facebook, instagram and twitter. 

# Dependencies
1. python3 
2. python3-pip
3. DataList.json
4. python selenium
5. xdo
6. xdotool
7. Firefox driver (geckodriver)

# Install 
```
$ apt install python3 xdo xdotool python3-pip \
	pip install selenium \
```
# Run 
You need to write down your data into DataList.json. This includes your logins, post content, id, post image and video. Then, run python
```
$ python3 main.py 

```
# Docker Image 
```
$ docker run -p 6000:80 -dit chunhou5741/socbot
```

# Headless run
~~MOZ_HEADLESS=1 python3 main.py~~