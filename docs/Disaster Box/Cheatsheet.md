	
```bash
grep -v '^#' file | less
```

```bash
zip nombre_archivo.zip archivo_a_comprimir.txt
```

```bash
rustscan -t 10000 -u 5000 -a 10.10.11.252
sudo nmap -p22,80,443 -sCV 10.10.11.252
nmap 10.10.11.252 -p- --min-rate=1000 -T4
sudo nmap 10.10.11.252 -sS --min-rate=5000 -Pn -n -p- --open -vvv
```

Crear archivos de archivos, empaquetados pero no comprimidos.
```shell
tar cvf mi_archivo.tar mi_carpeta/
tar xvf mi_archivo.tar

```
- c crear
- v verbose
- f file, nombre de archivo de salida

### Manual host scan:

```bash
for i in $(seq 1 254); do ping -c1 192.168.178.$i >/dev/null && echo "host en 172.223.0.$i"; done;
```

### Docker build

```bash
docker build . -t ysoserial
```

-t = tag

### grep + 2 lines

```bash
grep -A 2 tun0 archivo.txt
grep -B 2 tun0 archivo.txt
```


### php server

```shell-session
sudo php -S 0.0.0.0:80
```