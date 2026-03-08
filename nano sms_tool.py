from twilio.rest import Client
import time

account_sid = "ACb3e6c60ce55dd68b6f9417702de3e1fc"
auth_token = "8bf2723272b4ff14b2c2cc07ba4049d3"

client = Client(account_sid, auth_token)

to_number = input("Numero destino (+54...): ")
message = input("Mensaje: ")
count = int(input("Cantidad de mensajes: "))
delay = int(input("Intervalo entre mensajes (segundos): "))

from_number = "+5493515778063"

for i in range(count):
    client.messages.create(
        body=message,
        from_=from_number,
        to=to_number
    )

    print(f"Mensaje {i+1} enviado")

    time.sleep(delay)