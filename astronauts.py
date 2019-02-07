import requests
import json

if __name__ == "__main__":

	# Get the API response.
	response = requests.get("http://api.open-notify.org/astros.json")

	# Convert the response to a dictionary.
	data = response.json()

	# Display the astronauts.
	print("People currently in space:")
	print("")
	for p in data.items():
		if p[0] == "people":
			for astronaut in p[1]:
				print("   " + astronaut['name'] + " (" + astronaut['craft'] + ")") 