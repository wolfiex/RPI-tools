# Install
```
sudo pip install selenium
sudo pip install PyVirtualDisplay
sudo pip install xvfbwrapper

sudo apt-get update
sudo apt-get install iceweasel
sudo apt-get install xvfb --yes
sudo apt-get install chromium-browser --yes


```


# target.py
Auto setup the cronjob to run shoot.py 5 minutes before bid end. 

# shoot.py
runs a selinium browser to do all the nitty gritty clicking stuff. 
Aims to click 10 seconds before end. 
(lets hope its not at a time your internet fails)

# pass.word

A file consisting of two lines: 1 Username, 2 Password
