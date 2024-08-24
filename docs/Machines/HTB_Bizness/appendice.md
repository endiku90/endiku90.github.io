```bash
rustscan -t 10000 -u 5000 -a 10.10.11.252
nmap 10.10.11.252 -p- --min-rate=1000 -T4
sudo nmap -p22,80,443 -sCV 10.10.11.252
sudo nmap 10.10.11.252 -sS --min-rate=5000 -Pn -n -p- --open -vvv
```

```bash
ffuf -u https://bizness.htb/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -k -r -fw 9218
```

ysoserial? 

/dev/shm sistema de archivos temporales en la memoria ram, conocido por tmpfs. Muy rapido de acceder.

```bash
# sudo apt install derby-tools
ij
connect 'jdbc:derby:./ofbiz';
show tables;
select * from ofbiz.user_login;
```



sha1 41 chars
```bash
echo "uP0_QaVBpDWFeo8-dRzDqRwXQ2I=" | basenc -d --base64url | xxd -p
```

***Without padding**: En Base64 estándar, si los datos codificados no completan un bloque de 4 caracteres, se agregan uno o dos signos de igual (`=`) al final para "rellenar" la cadena. En Base64URL sin padding, estos caracteres de relleno se omiten.*
