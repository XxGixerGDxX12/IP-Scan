import requests

def get_ip_info(ip, api_key):
    # URL de la API con el parámetro de clave API
    url = f"https://ipinfo.io/{ip}/json?token={api_key}"

    try:
        # Realizar la solicitud a la API
        response = requests.get(url)
        data = response.json()

        # Verificar si la respuesta contiene datos de geolocalización
        if 'bogon' in data:
            print(f"La IP {ip} es una dirección reservada o bogon.")
        else:
            # Mostrar los datos obtenidos
            print(f"Información para la IP: {ip}")
            print(f"IP: {data.get('ip', 'No disponible')}")
            print(f"País: {data.get('country', 'No disponible')}")
            print(f"Región: {data.get('region', 'No disponible')}")
            print(f"Ciudad: {data.get('city', 'No disponible')}")
            print(f"Organización: {data.get('org', 'No disponible')}")
            print(f"Ubicación: {data.get('loc', 'No disponible')}")
            print(f"Zona horaria: {data.get('timezone', 'No disponible')}")
            print(f"Código postal: {data.get('postal', 'No disponible')}")
    except requests.RequestException as e:
        print(f"Error al conectar con la API: {e}")

# Ejemplo de uso
ip_address = input("Introduce la IP que quieres escanear: ")
api_key = 'b00fe5e6124f1a'
get_ip_info(ip_address, api_key)
