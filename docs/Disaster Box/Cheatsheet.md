	
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
for i in $(seq 1 254); do ping -c1 172.17.0.$i >/dev/null && echo "host en 172.17.0.$i"; done;
```
```shell-session
for i in {1..254} ;do (ping -c 1 172.16.5.$i | grep "bytes from" &) ;done
```
```cmd-session
for /L %i in (1 1 254) do ping 172.16.5.%i -n 1 -w 100 | find "Reply"
```

```powershell-session
1..254 | % {"172.16.5.$($_): $(Test-Connection -count 1 -comp 172.15.5.$($_) -quiet)"}
```


### Manual port scan:
```bash
for i in $(seq 1 65535); do nc -zv 172.17.0.1 $i; done 2>&1 | grep succ
```


### Port fwd

```bash
chisel server -p 9999 --reverse #attacker machine
chisel client 10.0.0.1:9999 R:8090:172.16.22.2:8000

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