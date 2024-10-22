****

| Name            | Bizness                                                                                   |
| --------------- | ----------------------------------------------------------------------------------------- |
| Platform        | HTB                                                                                       |
| Difficulty      | Easy                                                                                      |
| OS              | Linux                                                                                     |
| Used Techniques | known vulnerability, crack hashes, credentials finding, hex, hidden ports, special nmap   |
| Technologies    | https, Enterprise Resource Plannning (ERP), Apache OFBIZ, deserialization, derby database |
| Tools           | gobuster,  ysoserial, hashcat                                                             |
| CVEs            | CVE-2023-49070                                                                            |

## Enumeration



Regular scans let the port `43425` hidden. Once we adjust the parameter, we could enumerate it.
```bash
nmap 10.10.11.252 -p- --min-rate=1000 -T4
```


![[Pasted image 20240816135446.png]]

If we do basic enumeration on the website, we can see on the botton that Apache OFBIZ is running on the server.

![[Pasted image 20240816141250.png]]
### Directories

Basic fuzzing bring us `/control`, which show us, as we have seen before, that  **Apache OFBIZ**  is running on the website. 

If we follow redirects, then we find way more directories:
`content, catalog, marketing, ap, ar, ecommerce...`
Those show us a Loggin Panel wit the OFBiz version on the bottom:

![[Pasted image 20240816142643.png]]


This version has two vulnerabilities. The one which interests us is **the pre-auth RCE CVE-2023-49070**.


## Foothold

Foothold will be accomplish with the previous vulnerability. The exploit takes advantage from one error validating the login user.  Check sources, it is well explained. In order to exploit it, we will need **ysoserial** to serialize and then inject it on a xml post request. Everything is well documented on the exploit.

![[Pasted image 20240816184123.png]]  


## Privilege Escalation

After basic enumeration, we found a port for ofbizsetup. Searching for something interesting on the documentation, we find out :
- that it is always connected to a database.
- In `/framework/security/security.properties`we see that SHA is used for hashing passwords.
- Apache Derby is the db per default.

Once we know that the database is called Derby, we found out that there is a directory ` /opt/ofbiz/runtime/data/derby`.

If we imported and check it with `derby-tools` we find a hash:

![[Pasted image 20240816215302.png]]

Looking for credentials, OFZBiz has a database. We can export it and then look on the USER_LOGIN table to find admin's hash.


#### Developed map


![[Bizness10.10.11.252.jpg]]
#### Sources

[[https://github.com/UserConnecting/Exploit-CVE-2023-49070-and-CVE-2023-51467-Apache-OFBiz/blob/main/ofbiz_exploit.py]]

[[https://blog.sonicwall.com/en-us/2023/12/sonicwall-discovers-critical-apache-ofbiz-zero-day-authbiz/]]
[[https://db.apache.org/derby/docs/10.0/manuals/tools/tools23.html]]

[[https://github.com/frohoff/ysoserial]]