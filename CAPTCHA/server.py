
#!/usr/bin/python
from http import server
from io import BytesIO
import time
from captcha.image import ImageCaptcha
from flask import Flask, url_for, render_template, request, redirect
from forms import CaptchaForm
from flask_wtf.csrf import CsrfProtect
from tcp_client import send_message

CAPTCHA_STRING = 'CS4404'
SERVER_IP = 'www.google.com'
image = ImageCaptcha()

data = image.generate(CAPTCHA_STRING)
image.write(CAPTCHA_STRING, 'static/out.png')
connections_dict = {}

app = Flask(__name__)
app.secret_key = 's3cr3t'

@app.route('/', methods=["GET", "POST"])
def hello_world(name=None):
    if request.remote_addr in connections_dict:
        connections_dict[request.remote_addr][0]+=1
    else:
        connections_dict[request.remote_addr]=[1,0]

    # if they've made more than 4 requests
    if connections_dict[request.remote_addr][0] >=4:
        send_message(request.remote_addr, False)
        return render_template('robot.html', name=name)


    cpt = CaptchaForm()
    if request.method == "POST":
        if cpt.captcha.data == CAPTCHA_STRING:
            connections_dict.pop(request.remote_addr)
            send_message(request.remote_addr, True)
            return redirect("http://" + SERVER_IP)

    return render_template('index.html', name=name, form=cpt)
