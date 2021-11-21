from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY']= 'f4c05887b883e66cc981db21'
app.config['MAIL_HOST'] = 'smtp.gmail.com'
app.config['MAIL_HOST_USER'] = "mmseguros.microsite@gmail.com"
#app.config['UPLOAD_FOLDER'] = 'C:/Users/AndréMSGrilo/Desktop/Python stuff MAIN/11 MM Seguros/micro/images'
#app.config['MAX_CONTENT_PATH'] = '1024'

from micro import routes