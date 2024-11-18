# remote_carichello

Una semplice implementazione per creare una pagina web che permette l'upload di file .ogg, utilizzando un backend in Python con Flask. La pagina verifica che il file sia un .ogg e, se lo è, lo carica su un server FTP utilizzando Python.

project/
├── app.py
├── templates/
│   └── index.html
└── uploads/

app.py - Il backend con Flask.
templates/index.html - La pagina HTML per l'upload.
uploads/ - Cartella temporanea per salvare i file caricati.

# Installazione

Su un server Ubuntu 24.04

sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
sudo apt install python3-venv

mkdir ~/flask_app && cd ~/flask_app
python3 -m venv venv
source venv/bin/activate
pip install Flask

Crea il file app.py

sostituire your_ftp_username e your_ftp_password con le credenziali FTP.

python app.py

Verifica l'applicazione all'indirizzo http://<IP_della_VM>:5000


