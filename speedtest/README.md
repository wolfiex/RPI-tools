# Step 1
Install the requirements:
```
sudo apt-get install python-pip
sudo apt-get install speedtest-cli
sudo apt-get install -y nodejs

```

# Step 2
Start the updating program to update the csv
`crontab -e` 

and insert :
`*/5 * * * * python ~/speedtest.py`

to check every 5 minutes. You may edit this.


# Step 3 
Also update the path within this to the correct directory
Move / update the rc.local file in /etc. to configure autostart. Note code must go above the line stating exit!


# Step 4
Reboot, find your rpi ip address and view the graph using port 8000.
http://<your ip>:8000



