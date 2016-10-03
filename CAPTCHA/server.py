
#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from io import BytesIO
from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha
from flask import Flask, url_for, render_template
 
# audio = AudioCaptcha(voicedir='/path/to/voices')
image = ImageCaptcha()

data = image.generate('1234')
image.write('1234', 'static/out.png')

app = Flask(__name__)

url_for('static')

@app.route('/')
def hello_world(name=None):
    return render_template('index.html', name=name)