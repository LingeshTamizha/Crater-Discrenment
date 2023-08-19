import requests

def get_geo_location():
    def get_ip():
        response = requests.get('https://api64.ipify.org?format=json').json()
        return response["ip"]

    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        
    latitude = response.get("latitude")
    longitude = response.get("longitude")
        
    return latitude, longitude

print(get_geo_location())
