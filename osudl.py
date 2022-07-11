import tkinter as tk
import base64
import os
import subprocess
import requests
import re

def get_filename_from_cd(cd):
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]

def main():
    mapid = text.get('1.0', 'end')[:-1]
    url = 'https://chimu.moe/d/' + mapid

    r = requests.get(url, allow_redirects=True, stream=True)
    filename = str(get_filename_from_cd(r.headers.get('content-disposition')))
    open(filename.strip('"'), 'wb').write(r.content)
    subprocess.call(f'start "" {filename}', shell=True)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

window = tk.Tk()
window.iconbitmap(resource_path('icon.ico'))
window.geometry('100x100')
window.resizable(False, False)
window.title('chimudl')
window.configure(bg='grey')

message = tk.Label(
    window,
    text='Enter beatmap ID:'
)
message.pack()

text = tk.Text(
    window,
    height=1,
    width=10
)
text.pack()

download = tk.Button(
    window,
    text='Download',
    command=main
)
download.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

window.mainloop()


