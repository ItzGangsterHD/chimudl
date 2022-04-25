import requests
import re
import os
from tqdm import tqdm

def get_filename_from_cd(cd):
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]

def main():
    mapid = input('Enter beatmap ID: ')
    url = 'https://chimu.moe/d/' + mapid

    r = requests.get(url, allow_redirects=True, stream=True)
    filename = str(get_filename_from_cd(r.headers.get('content-disposition')))
    block_size = 1024
    total = int(r.headers.get('content-length', 0))
    progress_bar = tqdm(total = total, unit='iB', unit_scale=True)
    with open(filename.strip('"'), 'wb') as file:
        for data in r.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    os.system(f'start "" {filename}')

print('''     _     _                        _  _ 
 __ | |_  (_) _ __   _  _        __| || |
/ _||   \ | || '  \ | || |      / _` || |
\__||_||_||_||_|_|_| \_._|      \__/_||_|
''')

while True:
    main()
    if input('Download another beatmap? (Y/N): ').strip().upper() != 'Y':
        break