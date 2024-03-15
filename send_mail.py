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

    msg = MIMEMultipart()
    msg['From'] = user
    msg['Subject'] = subject
    msg['To'] = ', '.join(recipients)
    msg.attach(MIMEText(body))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(user_mail, password)
        
        for recipient in recipients:
            # Enviar el correo a cada destinatario individualmente
            server.sendmail(user_mail, recipient, msg.as_string())

    return jsonify({'message': 'Correo enviado con éxito'})

if __name__ == '__main__':
    app.run(debug=True)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)
