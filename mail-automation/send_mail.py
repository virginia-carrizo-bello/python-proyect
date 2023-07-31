from email.message import EmailMessage
import ssl
import smtplib
import imghdr

email_emisor='user.automation.200@gmail.com'
email_contrasena='tpbrplpshixzprdq'
email_receptor= 'virginia.carrizo.bello@gmail.com'

asunto = 'Checkeando automatizaciones de Python'
cuerpo = """
Buenos días.

Este mensaje es para probar una automatización realizada por Virginia en el lenguaje Python

Saludos.
"""

em = EmailMessage()
em['From'] = email_emisor
em['To'] = email_receptor
em['Subject'] = asunto
em.set_content(cuerpo)

with open('foto.jpg', 'rb') as file:
    file_data = file.read()
    file_tipo = imghdr.what(file.name)
    file_nombre = file.name
em.add_attachment(file_data, filename=file_nombre, subtype=file_tipo, maintype='image')


contexto = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
    smtp.login(email_emisor, email_contrasena)
    smtp.sendmail(email_emisor, email_receptor, em.as_string())

