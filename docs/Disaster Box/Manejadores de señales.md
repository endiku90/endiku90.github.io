
## bash
``` bash
#!/bin/bash

function handle_interrupt() {
    echo -e "\n[INFO] Se ha presionado Ctrl+C. Saliendo del script..."
    exit 1
}

# Capturar la señal SIGINT y ejecutar la función handle_interrupt
trap handle_interrupt SIGINT
... snip ...

```