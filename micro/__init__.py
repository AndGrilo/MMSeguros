from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY']= 'c4577e15a4497064eb90c3ab'
app.config['MAIL_HOST'] = 'smtp.gmail.com'
app.config['MAIL_HOST_USER'] = "mmseguros.microsite@gmail.com"
#app.config['UPLOAD_FOLDER'] = 'C:/Users/AndréMSGrilo/Desktop/Python stuff MAIN/11 MM Seguros/micro/images'
#app.config['MAX_CONTENT_PATH'] = '1024'

from micro import routes