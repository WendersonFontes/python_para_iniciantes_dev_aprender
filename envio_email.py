import os
import smtplib
from email.message import EmailMessage
from envio_email_senha import senha

# Configurar email, senha
EMAIL_ADRESS= '' #neste local coloca o endereço do e-mail de origem
E_MAIL_PASSWORD = senha

# Criar um e-mail
msg = EmailMessage()
msg['Subject'] = 'Carga #35 chegou ao porto'
msg['From'] = '' #neste local coloca o endereço do e-mail de origem
msg['To'] = '' #neste local coloca o endereço do e-mail de destino

msg.set_content('Favor buscar a carga #35 que acaba de chegar na portaria')


#enviar um e-mail
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADRESS, E_MAIL_PASSWORD)
    smtp.send_message(msg)