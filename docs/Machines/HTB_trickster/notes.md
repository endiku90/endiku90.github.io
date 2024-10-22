| Name            | Trickster                                 |
| --------------- | ----------------------------------------- |
| Platform        | HTB                                       |
| Difficulty      | Medium                                    |
| OS              | Linux                                     |
| Used techniques |                                           |
| Technologies    | Laravel, Laravel-admin                    |
| Tools           | gobuster,  BurpSuite, sqlmap, nc, strings |
| CVEs            | cve-2023-24249                            |

## Enumeration


PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 8c:01:0e:7b:b4:da:b7:2f:bb:2f:d3:a3:8c:a6:6d:87 (ECDSA)
|_  256 90:c6:f3:d8:3f:96:99:94:69:fe:d3:72:cb:fe:6c:c5 (ED25519)
80/tcp open  http    Apache httpd 2.4.52
|_http-title: Did not follow redirect to http://trickster.htb/
|_http-server-header: Apache/2.4.52 (Ubuntu)
Service Info: Host: _; OS: Linux; CPE: cpe:/o:linux:linux_kernel



### Directories





### subdomains



## Foothold




## Lateral Movement




## Privilege Escalation




#### Developed map



#### Sources

https://github.com/aelmokhtar/CVE-2024-34716
https://blog.hacktivesecurity.com/index.php/2024/05/08/cve-2024-32651-server-side-template-injection-changedetection-io/