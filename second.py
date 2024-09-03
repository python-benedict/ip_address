import requests

def get_geolocation(ip_address):
    try:
        # Send a request to the ipinfo.io API with the IP address
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Extracting geolocation details
            location = {
                'IP': data.get('ip'),
                'City': data.get('city'),
                'Region': data.get('region'),
                'Country': data.get('country'),
                'Location': data.get('loc'),
                'Postal': data.get('postal'),
                'Timezone': data.get('timezone')
            }
            return location
        else:
            return {"error": "Unable to retrieve information"}
    except Exception as e:
        return {"error": str(e)}

# Example usage
ip_address = "10.170.116.28"  # Replace with the IP address you want to lookup
geolocation = get_geolocation(ip_address)
print(geolocation)
