from werkzeug.utils import secure_filename
from micro import app
from micro.forms import Aconselhamento, VidaForm, SaudeForm, HabitacaoForm, AcidentesForm
from flask import render_template, redirect, url_for, flash, request
import smtplib
from email import message
from email.mime.base import MIMEBase
from os import read, walk
import os
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
from os import read
import werkzeug
#from werkzeug import secure_filename

from_addr = 'mmseguros.microsite@gmail.com'
to_addr = 'andregrilo.cbs@gmail.com'
e=0
c=0
@app.route('/')
def nothing():
    if e != 1:
        pass
    if c == 1:
        os.getcwd()
        os.remove(final_final)
    return redirect(url_for('inicial'))
@app.route('/inicial', methods=["GET", "POST"])
def inicial():
    global c
    c = 0
    form = Aconselhamento()
    if form.validate_on_submit():
        if request.method == 'POST':
            email_checkbox = request.form.get('email_checkbox')
            tlm_checkbox = request.form.get('tlm_checkbox')
            if email_checkbox == 'on':
                em = 'Sim'
            else:
                em = 'Não'
            if tlm_checkbox == 'on':
                tl = 'Sim'
            else:
                tl = 'Não'
            nome = request.form.get('nome')
            tlm = request.form.get('tlm')
            email = request.form.get('email')
            info_formatada = (f'--> Informações recolhidas da: Página inicial:\n\t-> Nome Completo: {nome}\n\t-> Telemóvel: {tlm}\n\t-> Email: {email}\n\n--> O cliente prefere ser contactado por:\n\t-> Email: {em}\n\t-> Telemóvel: {tl}')

            # Envio das informações por email
            
            subject = f'Informações da Página Inicial de {nome}'
            body = info_formatada.encode('ascii', 'xmlcharrefreplace').decode()
            
            msg = message.Message()
            msg.add_header('from', from_addr)
            msg.add_header('to', to_addr)
            msg.add_header('subject', subject)
            msg.set_payload(body)

            server = smtplib.SMTP('smtp-relay.sendinblue.com', 587)
            server.login(from_addr, '6ZGHLrgKYhXd4Ctw')
            server.send_message(msg, from_addr=from_addr, to_addrs=[to_addr])
            flash('Formulário preenchido com sucesso!', category='success')
            return redirect(url_for('nothing'))


    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error {err_msg}', category='danger')
    return render_template('inicial.html', form=form)

@app.route('/condicoes')
def condicoes():
    return render_template('condicoes.html')

@app.route('/vida', methods=["GET", "POST"])
def vida():
    form = VidaForm()
    
            

    return render_template('vida.html', form=form)

@app.route('/uploader', methods=["GET", "POST"])
def uploader_file():
    form = VidaForm()
    if form.validate_on_submit():
        nome1 = ''
        data_nascimento1 = ''
        estado_civil1 = ''
        profissao1 = ''
        genero1 =''
        nome2 = ''
        data_nascimento2 = ''
        estado_civil2 = ''
        profissao2 = ''
        genero2 =''
        if request.method == 'POST':
            nome = request.form.get('nome')
            email = request.form.get('email')
            tlm = request.form.get('tlm')
            nif = request.form.get('nif')
            umaPessoa = request.form.get('UmaPessoa')
            #duasPessoa = request.form.get('DuasPessoas')
            if umaPessoa == 'on':
                nome1 = request.form.get('nome1')
                data_nascimento1 = request.form.get('data_nascimento1')
                genero1 = request.form.get('genero1')
                estado_civil1 = request.form.get('estado_civil1')
                profissao1 = request.form.get('profissao1')
            if umaPessoa == 'None':
                nome2 = request.form.get('nome1')
                data_nascimento2 = request.form.get('data_nascimento1')
                genero2 = request.form.get('genero1')
                estado_civil2 = request.form.get('estado_civil1')
                profissao2 = request.form.get('profissao1')
            seg = request.form.get('seg')
            mrt = request.form.get('mrt')
            iad = request.form.get('iad')
            itp = request.form.get('itp')
            subject = request.form.get('subject')
            file = request.files['file']
            global a
            global e
            global c
            if str(file) == "<FileStorage: '' ('application/octet-stream')>":
                c = 0
            else:
                c = 1
            if c == 1:
                
                a = []
                file.save(secure_filename(file.filename))
                for (dirpath, dirnames, filenames) in walk('C:/Users/AndréMSGrilo/Desktop/Python stuff MAIN'):
                    a.extend(filenames)
                    break
                new_file_list = str(file).replace("<FileStorage: '", "")
                final = []
                for ss in new_file_list:
                    if ss == " ":
                        ss = "_"
                    if ss == "'":
                        break
                    final.extend(ss)
                global final_final
                final_final = ''.join(final)




                file_name = final_final
                filename = file_name
                attachment = open(file_name, "rb")
                
                e = 1
            if mrt == 'on':
                mr = "Sim"
            else:
                mr = 'Não'
            if iad == 'on':
                ia = "Sim"
            else:
                ia = 'Não'
            if itp == 'on':
                it = "Sim"
            else:
                it = 'Não'
            frase_formatada = (f'Informações recolhidas da: Página de Seguros de Vida:\n\nOs seus dados:\n\n-> Nome completo: {nome}\n-> Telemóvel: {tlm}\n-> Email: {email}\n-> NIF: {nif}\n\n##################################\n\nDados da 1ª pessoa segura:\n\n-> Nome Completo: {nome1}\n-> Data de nascimento: {data_nascimento1}\n-> Género: {genero1}\n-> Estado Civil: {estado_civil1}\n-> Profissão: {profissao1}\n\n##################################\n\nDados da 2ª Pessoa segura:\n\n-> Nome completo: {nome2}\n-> Data de nascimento: {data_nascimento2}\n-> Género: {genero2}\n-> Estado Civil: {estado_civil2}\n-> Profissão: {profissao2}\n\n##################################\n\n Sobre o seu Seguro:\n\n-> Capital Seguro / Valor em dívida: {seg} €\n\nCoberturas:\n\n-> Morte:{mr}\n-> IAD Invalidez Absoluta Definitiva: {ia}\n-> ITP Invalidez Total Permanente: {it}\n\n##################################\n\nFracionamento:\n\n-> {subject}')

            #Email

            subject1 = f'Informações de Página Seguros de Vida {nome}'
            body = frase_formatada.encode('ascii', 'xmlcharrefreplace').decode()
            
            msg = MIMEMultipart()
            msg['From'] = from_addr
            msg['To'] = to_addr
            msg['Subject'] = subject1
            content = body

            body = MIMEText(content, 'plain')
            msg.attach(body)
            
            part = MIMEBase('application', 'octet-stream')
            if c == 1:
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename = %s" % filename)
            msg.attach(part)

            



            #msg = message.Message()
            #msg.add_header('from', from_addr)
            #msg.add_header('to', to_addr)
            #msg.add_header('subject', subject1)
            #msg.set_payload(body)

            server = smtplib.SMTP('smtp-relay.sendinblue.com', 587)
            server.login(from_addr, '6ZGHLrgKYhXd4Ctw')
            server.send_message(msg, from_addr=from_addr, to_addrs=[to_addr])
            flash('Formulário preenchido com sucesso!', category='success')
            return redirect(url_for('nothing'))


    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error {err_msg}', category='danger')
    return render_template('vida.html', form=form)

@app.route('/saude', methods=["GET", "POST"])
def saude():
    form = SaudeForm()
    if form.validate_on_submit():
        if request.method == 'POST':
            nome = request.form.get('nome')
            email = request.form.get('email')
            tlm = request.form.get('tlm')
            nif = request.form.get('nif')
            data_nascimento = request.form.get('data_nascimento')
            info_formatada = (f'Informações recolhidas da: Página de Seguros de Saúde:\n-> Nome Completo: {nome}\n-> Email: {email}\n-> Telemóvel: {tlm}\n-> NIF: {nif}\n-> Data de nascimento: {data_nascimento}')

            #Email

            subject = f'Informações de Página Seguros de Saúde de {nome}'
            body = info_formatada.encode('ascii', 'xmlcharrefreplace').decode()
            
            msg = message.Message()
            msg.add_header('from', from_addr)
            msg.add_header('to', to_addr)
            msg.add_header('subject', subject)
            msg.set_payload(body)

            server = smtplib.SMTP('smtp-relay.sendinblue.com', 587)
            server.login(from_addr, '6ZGHLrgKYhXd4Ctw')
            server.send_message(msg, from_addr=from_addr, to_addrs=[to_addr])
            flash('Formulário preenchido com sucesso!', category='success')
            return redirect(url_for('nothing'))


    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error {err_msg}', category='danger')

    return render_template('saude.html', form = form)

@app.route('/habitacao', methods=["GET", "POST"])
def habitacao():
    form = HabitacaoForm()
    if form.validate_on_submit():
        if request.method == 'POST':
            nome = request.form.get('nome')
            email = request.form.get('email')
            tlm = request.form.get('tlm')
            nif = request.form.get('nif')
            local = request.form.get('local')
            codigo_postal = request.form.get('codigo_postal')
            area_bruta = request.form.get('area_bruta')
            num_w_c = request.form.get('num_w_c')
            ano_de_construcao = request.form.get('ano_de_construcao')
            ef = request.form.get('ef')
            rc = request.form.get('rc')
            file = request.files['file']
            global a, e, c
            if str(file) == "<FileStorage: '' ('application/octet-stream')>":
                c = 0
            else:
                c = 1
            if c == 1:
                
                a = []
                file.save(secure_filename(file.filename))
                for (dirpath, dirnames, filenames) in walk('C:/Users/AndréMSGrilo/Desktop/Python stuff MAIN'):
                    a.extend(filenames)
                    break
                file_name = a[0]
                filename = file_name
                attachment = open(file_name, "rb")
                
                e = 1

            print("file uploaded")



            if ef == 'on':
                e_f = "Sim"
            else:
                e_f = 'Não'
            if rc == 'on':
                r_c = 'Sim'
            else:
                r_c = 'Não'

            info_formatada = (f'Informações recolhidas da Página de Seguros de Multirriscos\n\nOs seus dados:\n\n-> Nome completo: {nome}\n-> E-mail: {email}\n-> Telemóvel: {tlm}\n-> NIF: {nif}\n\n##################################\n\nSobre a sua habitação:\n\n-> Local de Risco: {local}\n-> Código-Postal: {codigo_postal}\n-> Área Bruta Privativa Total {area_bruta}\n-> Número de W.C.: {num_w_c}\n-> Ano de Construção: {ano_de_construcao}\n\n##################################\n\nCoberturas:\n\n-> Edifício/Fração: {e_f}\n-> Recheio/Conteúdo: {r_c}')

            #Email
            
            subject1 = f'Informações de Página Seguros de Habitação de {nome}'
            body = info_formatada.encode('ascii', 'xmlcharrefreplace').decode()

            

            msg = MIMEMultipart()
            msg['From'] = from_addr
            msg['To'] = to_addr
            msg['Subject'] = subject1
            content = body


            body = MIMEText(content, 'plain')
            msg.attach(body)
            
            part = MIMEBase('application', 'octet-stream')
            if c == 1:
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename = %s" % filename)
            msg.attach(part)








            server = smtplib.SMTP('smtp-relay.sendinblue.com', 587)
            server.login(from_addr, '6ZGHLrgKYhXd4Ctw')
            server.send_message(msg, from_addr=from_addr, to_addrs=[to_addr])
            flash('Formulário preenchido com sucesso!', category='success')
            return redirect(url_for('nothing'))


    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error {err_msg}', category='danger')

    return render_template('habitacao.html', form = form)

@app.route('/acidentes', methods=["GET", "POST"])
def acidentes():
    form = AcidentesForm()
    if form.validate_on_submit():
        if request.method == 'POST':
            nome = request.form.get('nome')
            email = request.form.get('email')
            tlm = request.form.get('tlm')
            nif = request.form.get('nif')
            data_nascimento = request.form.get('data_nascimento')
            profissao = request.form.get('profissao')
            capitais = request.form.get('capitais')
            sim = request.form.get('sim')
            nao = request.form.get('nao')
            obs = request.form.get('obs')
            if sim == 'on':
                sim = "Sim"
            else:
                sim = ""
            if nao == 'on':
                nao = "Não"
            else:
                nao = ""
            

            obs = request.form.get('obs')

            info_formatada = (f'Informações recolhidas da:\nPágina de Seguros de Acidentes Pessoais:\n\nOs seus dados:\n\n-> Nome completo: {nome}\n-> E-mail: {email}\n-> Telemóvel: {tlm}\n-> NIF: {nif}\n-> Data de Nascimento: {data_nascimento}\n-> Profissão: {profissao}\n\n##################################\n\nSobre o seu seguro:\n\n-> Capitais: {capitais} €\n->Utiliza viaturas de duas rodas: {sim}{nao}\n\n##################################\n\nObservações:\n{obs}')
            subject = f'Informações de Página Seguros de Acidentes Pessoais de {nome}'
            body = info_formatada.encode('ascii', 'xmlcharrefreplace').decode()
            
            msg = message.Message()
            msg.add_header('from', from_addr)
            msg.add_header('to', to_addr)
            msg.add_header('subject', subject)
            msg.set_payload(body)

            server = smtplib.SMTP('smtp-relay.sendinblue.com', 587)
            server.login(from_addr, '6ZGHLrgKYhXd4Ctw')
            server.send_message(msg, from_addr=from_addr, to_addrs=[to_addr])
            flash('Formulário preenchido com sucesso!', category='success')
            return redirect(url_for('nothing'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error {err_msg}', category='danger')
            



    return render_template('acidentes.html', form = form)