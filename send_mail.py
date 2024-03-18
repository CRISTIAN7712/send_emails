from flask import Flask, request, jsonify
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask_cors import CORS


# Cargar las variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/send_mail', methods=['POST'])
def send_mail():
    data = request.get_json()
    user = data.get('user')
    subject = data.get('subject')
    recipients = data.get('recipients')
    body = data.get('body')

    # Obtener las variables de entorno
    user_mail = os.getenv("USER_MAIL")
    password = os.getenv("PASSWORD")
    port = int(os.getenv("FLASK_PORT", 5000))  # Lee el puerto desde la variable de entorno FLASK_PORT

    msg = MIMEMultipart()
    msg['From'] = user
    msg['Subject'] = subject
    msg['To'] = ', '.join(recipients)
    msg.attach(MIMEText(body))

    with smtplib.SMTP('smtp.gmail.com', port) as server:  # Usa el puerto obtenido de la variable de entorno
        server.starttls()
        server.login(user_mail, password)
        
        for recipient in recipients:
            # Enviar el correo a cada destinatario individualmente
            server.sendmail(user_mail, recipient, msg.as_string())

    return jsonify({'message': 'Correo enviado con éxito'})

if __name__ == '__main__':
    app.run(debug=True, port=int(os.getenv("FLASK_PORT", 5000)))  # Usa el puerto obtenido de la variable de entorno FLASK_PORT

