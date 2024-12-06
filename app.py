from flask import Flask, render_template, request, send_file, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from main import process_tts

app = Flask(__name__)
app.secret_key = 'supersecretkey'
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text')
        # language = request.form.get('language', 'en')
        speaker_file = request.files.get('speaker')
        output_filename = 'output.wav'
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)

        speaker_path = None
        if speaker_file:
            speaker_filename = secure_filename(speaker_file.filename)
            speaker_path = os.path.join(app.config['UPLOAD_FOLDER'], speaker_filename)
            speaker_file.save(speaker_path)

        if not text:
            flash('Text is required!', 'danger')
            return redirect(url_for('index'))

        success = process_tts(text, output_path, speaker_path)
        if success:
            return redirect(url_for('download_file', filename=output_filename))
        else:
            flash('TTS conversion failed', 'danger')
            return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(app.config['OUTPUT_FOLDER'], filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)