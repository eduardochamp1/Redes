import http.client

IP = input('Informe o endereço de IP do servidor: ')

HOST = IP
PORT = 5000

filename = input("Digite o caminho do arquivo: ")

with open(filename, 'rb') as file:
    file_content = file.read()

# Concatenar o nome do arquivo com os dados do arquivo usando o separador '|||'
message = filename.encode() + b'|||' + file_content

conn = http.client.HTTPConnection(HOST, PORT)
conn.request("POST", "/", body=message)
response = conn.getresponse()

print(response.read().decode())

conn.close()
