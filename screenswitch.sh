#!/usr/bin/env bash

in_debug=`[ ${1:-''} == '--debug' ] && echo true || echo false`
internal_screen=`xrandr | grep -i 'LVDS' | cut -f 1 -d ' '`
previous_external_screen_count=0

while true; do
    external_screens=`xrandr | grep -iv "$internal_screen\|virtual" | grep -i ' connected '`
    current_external_screen_count=`[ -n "$external_screens" ] && echo "$external_screens" | wc -l || echo 0`

    if [ $current_external_screen_count != $previous_external_screen_count ]; then
        previous_external_screen_count=$current_external_screen_count

        if [ $current_external_screen_count == 0 ]; then
            cmd="xrandr --output $internal_screen --auto"
            echo "[INFO]: No external screens detected, switching back to internal screen."
        else
            external_screen=`echo "$external_screens" | cut -f 1 -d ' '`
            cmd="xrandr --output ${internal_screen} --off --output $external_screen --auto"
            echo "[INFO]: Connected external screen count is $current_external_screen_count."
            echo "[INFO]: Switching external screen $external_screen to PRIMARY, turning off internal screen."
        fi

        $in_debug && echo "[DEBUG]: $cmd"
        eval "$cmd"
    fi

    sleep 5
done
