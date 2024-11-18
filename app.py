from flask import Flask, request, flash, redirect, url_for
import os
from werkzeug.utils import secure_filename
from ftplib import FTP

app = Flask(__name__)
app.secret_key = 'your_secret_key'
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'ogg'}
FTP_URL = 'upload.arkiwi.org'
FTP_PATH = '/2024/11'
FTP_USERNAME = 'your_ftp_username'
FTP_PASSWORD = 'your_ftp_password'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Nessun file selezionato.')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('Nessun file selezionato.')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            try:
                with FTP(FTP_URL) as ftp:
                    ftp.login(FTP_USERNAME, FTP_PASSWORD)
                    with open(file_path, 'rb') as f:
                        ftp.storbinary(f'STOR {FTP_PATH}/{filename}', f)
                flash('Upload completato con successo!')
            except Exception as e:
                flash(f'Errore durante l\'upload: {e}')
            finally:
                os.remove(file_path)
            return redirect(request.url)
        else:
            flash('Accettiamo solo file .ogg.')
            return redirect(request.url)
    return '''
    <!doctype html>
    <title>Carica un file .ogg</title>
    <h1>Carica un file .ogg</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file accept=".ogg">
      <input type=submit value=Carica>
    </form>
    '''
if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(host='0.0.0.0', port=5000)

