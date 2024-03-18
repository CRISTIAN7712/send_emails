# Flask Email Sender

Este es un proyecto simple de Flask que permite enviar correos electrónicos utilizando un servidor SMTP de Gmail.

## Configuración

1. Crea un entorno virtual e instala las dependencias:
python -m venv venv
source venv/bin/activate  # En Windows, utiliza `venv\Scripts\activate`
pip install -r requirements.txt

2. Crea un archivo .env en el directorio raíz y configura las variables de entorno:
USER_MAIL=nombre_usuario@gmail.com
PASSWORD=tu_contraseña_de_aplicacion
FLASK_PORT=puerto_de_tu_app

4. Ejecuta la aplicación:
python send_mail.py

5. Uso
{
  "user": "nombre_usuario",
  "subject": "Asunto del correo",
  "recipients": ["destinatario@example.com"],
  "body": "Cuerpo del correo"
}


Este README básico proporciona instrucciones sobre cómo configurar y ejecutar tu aplicación Flask, así como una breve descripción del proyecto. Personaliza el contenido según las necesidades específicas de tu proyecto.

Autor
Cristian Diaz - Ingeniero de Sistemas
Correo electrónico: cristian.diaz8918@gmail.com
