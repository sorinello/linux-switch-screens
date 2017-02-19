### Use Case

1. When connecting an external display (DVI, HDMI, DP) you want to turn off your laptop screen and automatically switch as PRIMARY display to the external screen
2. When disconnecting and external display (DVI, HDMI, DP) you want to switch back to your laptop lid as PRIMARY display

### How to setup

1. Copy the script below into an empty file, save it as switch_screens.py
2. In the head section of your script, set the name of your internal screen. To find out, open a terminal window and run the command xrandr (when no external screen connected). The line with `connected` in it shows the name of your screen in the first string, looking like: `VGA-1` or something like that.

3. Test- run it by opening a terminal window and typ the command:
   `python3 /path/to/switch_screens.py`
    While the script runs, connect your TV, wait for you internal screen to switch of and disconnect again.

4.  If all works fine, add the command below to Startup Applications: open Dash > Startup Applications > Add. Add the command:
    `/bin/bash -c "sleep 15 && python3 /path/to/switch_screens.py"`

Special thanks for **Jacob Vlijm** as the original author of the script.
Script is taken from [askubuntu.com](http://askubuntu.com/questions/740004/how-can-i-automatically-switch-off-internal-screen-when-an-external-screen-is-co) 
