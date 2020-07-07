
pkill -f np-applet
pkill -f mate-panel

dconf reset -f /org/mate/panel/objects/ > /dev/null &
dconf reset -f /org/mate/panel/toplevels/ > /dev/null &

mate-panel --layout ubuntu-mate --reset
mate-panel --replace > /dev/null &
nm-applet > /dev/null &



pkill -f np-applet
pkill -f mate-panel

dconf reset -f /org/mate/panel/objects/ > /dev/null &
dconf reset -f /org/mate/panel/toplevels/ > /dev/null &

mate-panel --layout ubuntu-mate --reset
mate-panel --replace > /dev/null &
nm-applet > /dev/null &
