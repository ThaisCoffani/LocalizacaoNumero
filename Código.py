import phonenumbers

from phonenumbers import geocoder, carrier, timezone

print("Bem-Vindo, digite o número de telefone que deseja obter as informações")
print("Ele deve estar no formato ex(+5511987586371)")

numero = input()

phoneNumber = phonenumbers.parse(numero)

timeZone = timezone.time_zones_for_number(phoneNumber)

Chip = carrier.name_for_number(phoneNumber, 'BR')

Estado = geocoder.description_for_number(phoneNumber, 'BR')


print(phoneNumber)
print("Este número no fuso horário: ", timeZone)
print("Seu chip é: ", Chip)
print("Está localizado no estado: ",Estado)
