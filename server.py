# Para Python 2
# from SimpleHTTPServer import SimpleHTTPRequestHandler
# from BaseHTTPServer import HTTPServer

# Para Python 3
from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

# Obtiene el directorio actual del script
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Configura el puerto en el que se ejecutará el servidor
puerto = 8000

# Cambia el directorio de trabajo al directorio actual
os.chdir(directorio_actual)

# Crea el manejador de solicitudes HTTP
manejador = SimpleHTTPRequestHandler

try:
    # Crea el servidor HTTP
    servidor = HTTPServer(('localhost', puerto), manejador)

    print(f'Servidor en ejecución en http://localhost:{puerto}')
    # Inicia el servidor
    servidor.serve_forever()

except KeyboardInterrupt:
    # Detiene el servidor con Ctrl+C
    print('\nServidor detenido.')
    servidor.shutdown()
