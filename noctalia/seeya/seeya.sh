#!/bin/bash
current_brightness=$(ddcutil getvcp 10 | awk '{print $9}' | tr -d ',')

paplay ~/.config/noctalia/seeya/seeya.mp3 &

for i in {1..20}; do
    noctalia msg brightness-down > /dev/null
    sleep 0.05
done

sleep 0.5

noctalia msg brightness-set $current_brightness > /dev/null
