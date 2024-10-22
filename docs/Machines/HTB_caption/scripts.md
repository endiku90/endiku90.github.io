## Copiar log_service:

namespace go log_service
```go
service LogService {
    string ReadLogFile(1: string filePath)
}
```


## Generar el cliente Python a partir del archivo anterior:

```bash
thrift --gen py log_service.thrift
```

Esto generará un directorio `gen-py` con los archivos necesarios para el cliente en Python. Asegúrate de tener instalado Thrift en tu sistema, y si no lo tienes, puedes instalarlo con:

```python
import sys

sys.path.append('/home/endiku/HTB/Maquinas/HTB_caption/content/gen-py')

  

from thrift import Thrift

from thrift.transport import TSocket

from thrift.transport import TTransport

from thrift.protocol import TBinaryProtocol

from log_service import LogService # Importa el cliente generado por Thrift

  

def main():

try:

# Crear socket y conectar al servidor en localhost:9090

transport = TSocket.TSocket('localhost', 9090)

# Usar un transporte con buffer

transport = TTransport.TBufferedTransport(transport)

# Usar el protocolo binario para la comunicación

protocol = TBinaryProtocol.TBinaryProtocol(transport)

# Crear un cliente del servicio LogService

client = LogService.Client(protocol)

# Abrir la conexión

transport.open()

  

# Llamar al método ReadLogFile con la ruta del archivo

filePath = "/tmp/tmp2/test"

content = client.ReadLogFile(filePath)

# Mostrar el contenido del archivo

print("Contenido del archivo:", content)

  

with open('output_cliente.log', 'w') as f:

f.write(content)

  

# Cerrar el transporte

transport.close()

  

except Thrift.TException as tx:

print(f'Error: {tx.message}')

  

if __name__ == "__main__":

main()
```



script:
