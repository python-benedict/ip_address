import ip2geotools.databases.noncommercial as ip2geo

def get_geolocation(ip_address):
    """
    Gets the geolocation information for a given IP address using the ip2geotools library.

    Args:
        ip_address (str): The IP address to lookup.

    Returns:
        dict: A dictionary containing geolocation information, including city, region,
              country, latitude, and longitude.
    """

    response = ip2geo.DbIpCity.get(ip_address)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get geolocation for IP address {ip_address}")

# Example usage:
ip_address = "8.8.8.8"  # Replace with the desired IP address
geolocation_data = get_geolocation(ip_address)

print("City:", geolocation_data["city"])
print("Region:", geolocation_data["region"])
print("Country:", geolocation_data["country"])
print("Latitude:", geolocation_data["latitude"])
print("Longitude:", geolocation_data["longitude"])