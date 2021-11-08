from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, FileField
from wtforms.validators import Length, DataRequired, Email

class Aconselhamento(FlaskForm):
    nome= StringField(label="Nome Completo", validators=[Length(min=3, max=60), DataRequired()])
    tlm = IntegerField(label="Telemóvel", validators=[DataRequired()])
    email = StringField(label="E-mail", validators=[Length(min=7, max=60), DataRequired(), Email()])
    submit = SubmitField(label="Submeter")

class VidaForm(FlaskForm):
    nome = StringField(label="Nome Completo", validators=[Length(min=3, max=60), DataRequired()])
    email = StringField(label="E-mail", validators=[Length(min=7, max=60), DataRequired(), Email()])
    tlm = IntegerField(label="Telemóvel", validators=[DataRequired()])
    nif = IntegerField(label="NIF", validators=[DataRequired()])

    nome1 = StringField(label="Nome Completo", validators=[Length(min=0, max=60)])
    data_nascimento1 = StringField(label="Data de Nascimento", validators=[Length(min=0, max=12)])
    genero1 = StringField(label="Género", validators=[Length(min=0, max=12)])
    estado_civil1 = StringField(label="Estado Civil", validators=[Length(min=0, max=12)])
    profissao1 = StringField(label="Nome Completo", validators=[Length(min=0, max=60)])

    nome2 = StringField(label="Nome Completo", validators=[Length(min=0, max=60)])
    data_nascimento2 = StringField(label="Data de Nascimento", validators=[Length(min=0, max=12)])
    genero2 = StringField(label="Género", validators=[Length(min=0, max=12)])
    estado_civil2 = StringField(label="Estado Civil", validators=[Length(min=0, max=12)])
    profissao2 = StringField(label="Nome Completo", validators=[Length(min=0, max=60)])

    file = FileField(label="File")

    seg = StringField(label="Capital Seguro/Valor em dívida")

    submit = SubmitField(label="Submeter")

class SaudeForm(FlaskForm):
    nome = StringField(label="Nome Completo", validators=[Length(min=3, max=60), DataRequired()])
    email = StringField(label="E-mail", validators=[Length(min=7, max=60), DataRequired(), Email()])
    tlm = IntegerField(label="Telemóvel", validators=[DataRequired()])
    nif = IntegerField(label="NIF", validators=[DataRequired()])
    data_nascimento = StringField(label="Data de Nascimento", validators=[Length(min=8, max=12), DataRequired()])

    submit = SubmitField(label="Submeter")

class HabitacaoForm(FlaskForm):
    nome = StringField(label="Nome Completo", validators=[Length(min=3, max=60), DataRequired()])
    email = StringField(label="E-mail", validators=[Length(min=7, max=60), DataRequired(), Email()])
    tlm = IntegerField(label="Telemóvel", validators=[DataRequired()])
    nif = IntegerField(label="NIF", validators=[DataRequired()])

    local = StringField(label="Local de Risco", validators=[Length(min=3, max=60), DataRequired()])
    codigo_postal = StringField(label="Código-Postal", validators=[Length(min=3, max=60), DataRequired()])
    area_bruta = StringField(label="Área Bruta Privativa Total", validators=[Length(min=3, max=60), DataRequired()])
    num_w_c = StringField(label="Número de W.C.", validators=[Length(min=3, max=60), DataRequired()])
    ano_de_construcao = StringField(label="Ano de Construção", validators=[Length(min=3, max=60), DataRequired()])
    submit = SubmitField(label="Submeter")

class AcidentesForm(FlaskForm):
    nome = StringField(label="Nome Completo", validators=[Length(min=3, max=60), DataRequired()])
    email = StringField(label="E-mail", validators=[Length(min=7, max=60), DataRequired(), Email()])
    tlm = IntegerField(label="Telemóvel", validators=[DataRequired()])
    nif = IntegerField(label="NIF", validators=[DataRequired()])
    data_nascimento = StringField(label="Data de Nascimento", validators=[Length(min=8, max=12), DataRequired()])
    capitais = StringField(label="Capitais", validators=[Length(min=3, max=12), DataRequired()])
    profissao = StringField(label="Profissão", validators=[Length(min=3, max=60), DataRequired()])
    obs = StringField(label="Observações", validators=[Length(max=600)])
    submit = SubmitField(label="Submeter")