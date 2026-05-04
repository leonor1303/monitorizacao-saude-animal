import requests

api_key = "1234"
cidade = "Leiria"

url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric"

response = requests.get(url)
dados = response.json()

temp = dados["main"]["temp"]
humidade = dados["main"]["humidity"]

print(f"Temperatura: {temp}°C")
print(f"Humidade: {humidade}%")


if temp > 30:
    print("Risco de stress térmico em animais!")

with open("outputs/meteo.json", "w") as f:
    f.write(str(dados))
