import string
import requests
import time
chars = list(string.ascii_lowercase) + list(map(str, range(0, 10)))
f = open("output.txt", "a")

for a in chars:
    for b in chars:
        url = f"https://github.com/{a}{b}"
        if requests.get(url).status_code == 404:
            print(f'{a}{b} available')
            f.write(url + '\n')
        else:
            print(f'{a}{b} taken')
        time.sleep(0.5)
f.close()
