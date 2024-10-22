| Name            | Monitorsthree                                    |
| --------------- | ------------------------------------------------ |
| Platform        | HTB                                              |
| Difficulty      | Medium                                           |
| OS              | Linux                                            |
| Used techniques | sudomain enumeration,  SQLi, known vulnerability |
| Technologies    | cacti, duplicati                                 |
| Tools           | gobuster,  BurpSuite, sqlmap, nc                 |
| CVEs            |                                                  |

## Enumeration


Ports 22 and 80 open, with nginx server running on a Ubuntu:

```bash
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 86:f8:7d:6f:42:91:bb:89:72:91:af:72:f3:01:ff:5b (ECDSA)
|_  256 50:f9:ed:8e:73:64:9e:aa:f6:08:95:14:f0:a6:0d:57 (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: MonitorsThree - Networking Solutions
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```


## Web Enumeration


```bash
http://monitorsthree.htb [200 OK] Bootstrap, Country[RESERVED][ZZ], Email[sales@monitorsthree.htb], HTTPServer[Ubuntu Linux][nginx/1.18.0 (Ubuntu)], IP[10.10.11.30], JQuery, Script, Title[MonitorsThree - Networking Solutions], X-UA-Compatible[IE=edge], nginx[1.18.0]
```


**/login.php** and **forgot_password.php**, but none of them is vulnerable to injections.



### Subdomain enumeration

**cacti.monitorsthree.htb** shows up. If we visit it, we can find a login page with version number from the software.

![[Pasted image 20240829193534.png]]

A little bit of research and we see it has vulnerabilities:

![[Pasted image 20240829193811.png]]

It does not work because we are not authenticated and we still don't know any old password.

Directory enumeration takes us to cacti.monitorsthree.htb/app/, which is a copy of the main page. If we try the same injections, we find out that it has not all the functionalities like the production page. If we try SQLi, we find that it is vulnerable:

![[Pasted image 20240829194314.png]]

## Foothold

Once we know it is vulnerable to SQLi, let's run sqlmap. And we get credentials for admin:

![[Pasted image 20240829195023.png]]

Now we can test the above vulnerabilities and get RCE.

![[Pasted image 20240829201946.png]]




## Getting all

After looking up everywhere, we found some credentials in config.php to another db which does not give much more privileges. 


If we check network status, we see that the host is connected to two private networks (one docker) and *tcp port 8200 is open.*

```bash
chisel server -p 9999 --reverse #attacker machine
chisel client 10.0.0.1:9999 R:8090:172.16.22.2:8000
```


Once we portfwd 8200 with chisel, we see that is **duplicati** running.

![[Pasted image 20240829203234.png]]


Googling what duplicati is and if there are vulnerabilities, we found out that it can be bypassed.

![[Pasted image 20240829204344.png]]


Here, we can back up /marcus and /root and take flags.



#### Sources

[[https://github.com/Cacti/cacti/releases]]
[[https://www.stationx.net/sqlmap-cheat-sheet/]]
[[https://github.com/duplicati/duplicati/issues/5197]]
[[https://n3nu.medium.com/how-to-pivot-using-chisel-e59b1987e252]]
[[https://ap3x.github.io/posts/pivoting-with-chisel/]]