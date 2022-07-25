from pyperclip import paste
from waiting import wait
from re import findall
import subprocess
import requests

s = paste()

def get_filename_from_cd(cd):
    if not cd:
        return None
    fname = findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    name = fname[0].maketrans('"/\:*?<>|', '         ')
    return fname[0].translate(name)

def main(mapid):
    url = 'https://chimu.moe/d/' + mapid
    r = requests.get(url, allow_redirects=True, stream=True)
    filename = str(get_filename_from_cd(r.headers.get('content-disposition')))
    open(filename, 'wb').write(r.content)
    subprocess.call(f'start "" "{filename}"', shell=True)

def getid(url):
    mapid = ''
    for i in url[31:]:
        if i.isdigit(): mapid += i
        else: return mapid

def check():
    global s
    if s != paste():
        s = paste()
        if s.startswith('https://osu.ppy.sh/beatmapset'):
            main(getid(s))
        if s.startswith('https://osu.ppy.sh/b/') or s.startswith('https://osu.ppy.sh/beatmaps'):
            resp = requests.Session().head(s, allow_redirects=True)
            main(getid(resp.url))

wait(check)
