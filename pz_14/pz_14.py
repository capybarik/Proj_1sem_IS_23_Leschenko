#В исходном текстовом файле(radio_stations.txt) найти все домены из URL-адресов
#(например, в URL-адресе http://stream.hoster.by:8081/pilotfm/audio/icecast.audio
#домен выделен полужирным).

import re

with open('radio_stations.txt', encoding='utf-8') as file:
    text = file.read()

regular = re.compile(r"//(.*):")
print(regular.findall(text))


