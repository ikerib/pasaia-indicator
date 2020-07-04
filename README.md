# Pasaia-indicator

IP helbidea ikustarazteko "Mate Panek Indicators" gaitu behar da, horretarako bi bide daude:
- Sistema => Hobespenak => Itxura eta izaera => Mate TWEAK bertan Interfaces atalean gaitu "Enable indicators"
- [Ez dabil] shell batean exekutatu gsettings set org.mate.panel default-layout ubuntu-mate-indicators


    git clone git@github.com:ikerib/pasaia-indicator.git
    cd pasaia-indicator
    python3 pasaia-indicator

Ordenagailua abiaraztean exekutatu dadin:

    chmod +x pasaia-indicator.py
    nohup python3 /path/to/pasaia-indicator.py &



Credits:

https://itectec.com/ubuntu/ubuntu-how-to-write-a-dynamically-updated-panel-app-indicator/