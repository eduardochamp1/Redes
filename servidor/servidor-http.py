import http.server
import socketserver

HOST = ''
PORT = 5000

class FileUploadHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        file_data = self.rfile.read(content_length)

        # Extrair nome do arquivo e dados do arquivo
        file_parts = file_data.split(b'|||')
        file_name = file_parts[0].decode('latin-1')
        file_content = file_parts[1]

        with open(file_name, 'wb') as file:
            file.write(file_content)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Arquivo recebido e salvo com sucesso.")

with socketserver.TCPServer((HOST, PORT), FileUploadHandler) as httpd:
    print(f'Servidor rodando em {HOST}:{PORT}')
    httpd.serve_forever()
