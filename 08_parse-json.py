import urllib.parse
import requests

main_api="https://www.mapquestapi.com/diresctions/v3/route?"
orig="Washington"
dest="Baltimore"
key="9ytf1a9zklWaKrFgWzuMkSy90mySmuXl"
url=main_api+urllib.parse.urlencode({'key':key,'from':orig,'to':dest})
json_data=requests.get(url).json()
print(json_data)
