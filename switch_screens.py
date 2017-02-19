#!/usr/bin/env python3
import subprocess
import time
# --- set your internal screen below (the example is my primary screen)
# --- to see the internal display , from a CLI run xrandr
internal = "HDMI-1"
#---

# don't change anything below
scr_info1 = 0

while True:
    # time interval for each check
    time.sleep(4)
    # read the current screen setup from xrandr
    get_screens = subprocess.check_output("xrandr").decode("utf-8").splitlines()
    scr_data = [l for l in get_screens if " connected " in l]
    # count the number of connected screens
    scr_info2  = len(scr_data)
    print ("[INFO]: Connected screens %s" % scr_info2)
    # if the number of connected screens changes,
    # switch off the internal one if there are two screens
    if scr_info2 != scr_info1:
        if scr_info2 == 2:
            ext = [s.split()[0] for s in scr_data if not internal in s][0]
            print ("[INFO]: External display is: %s. Switching to external display as PRIMARY, turning internal screen" % ext)
            print("[DEBUG]: xrandr --output %s --off --output %s --auto" % (internal, ext))
            subprocess.Popen(["xrandr", "--output", internal, "--off", "--output", ext, "--auto"])
        # if external screen is disconnected, switch back to the internal one
        if scr_info2 == 1:
            print ("[INFO]: No external screens detected, switching back to internal screen")
            print("[DEBUG]: xrandr --output %s --auto" % internal)
            subprocess.Popen(["xrandr", "--output", internal, "--auto"])
    # assignment in order to prevent entering the if-loop uslessly
    scr_info1 = scr_info2

