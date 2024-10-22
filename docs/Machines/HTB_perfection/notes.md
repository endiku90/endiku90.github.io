| Name            | Perfection                                                   |
| --------------- | ------------------------------------------------------------ |
| Platform        | HTB                                                          |
| Difficulty      | Easy                                                         |
| OS              | Linux                                                        |
| Used techniques | input validation bypass, SSTI, attack mask cracking, sudo -l |
| Technologies    | Ruby, sqlite                                                 |
| Tools           | hashcat, burpsuit                                            |
| CVEs            |                                                              |

## Enumeration


![[Pasted image 20240706184117.png]]

```bash 
└──╼ $ whatweb 10.10.11.253
http://10.10.11.253 [200 OK] Country[RESERVED][ZZ], HTTPServer[nginx, WEBrick/1.7.0 (Ruby/3.0.2/2021-07-07)], IP[10.10.11.253], PoweredBy[WEBrick], Ruby[3.0.2], Script, Title[Weighted Grade Calculator], UncommonHeaders[x-content-type-options], X-Frame-Options[SAMEORIGIN], X-XSS-Protection[1; mode=block]
```

==Important: WEBrick 1.7.0, Ruby[3.0.2], nginx==


May be vulnerable WEBrick 1.7.0

Possible users on web: tina smith, susan miller.

### Directories

Just the ones in the web site.


### Subdomains

No subdomains.


## Foothold

Functionality on */weighted-grade-calc*.

"***Malicious input blocked***" message if we try to some injection. What should we look for? SQLi makes no sense since we are not requesting for data, however it makes "calculations", that means that somehow it interprets the input. It should be noted that it also reflects the input, so we ca go for XSS, but I may no be useful since it is a client-side vulnerability. First, we have to **bypass this input validation.** How may be able to bypass it? 

- Character that may work: **; , . " ' |  \\n** 
- Url encode list before and try to inject XSS.

In works if we use \\n url encoded (**%0A**):

![[Pasted image 20240706202808.png]]

Reflected XSS, client-side, no chance to SSRF. 

Now what? As it interprets our input it may be using a template, so we can try **SSTI**. 

Ruby is on back-end, let's use his sintax:

![[Pasted image 20240707104622.png]]


We got RCE, let's go for shell.
Python3 payload + urlencoded.


![[Pasted image 20240707105647.png]]



## Privilege Escalation


Credentials store in *~/Migration/pupilpath_credentials.db*

```bash
find / -name "*sql*" 2>/dev/null
sqlite3
```


Impossible to crack. If we look further looking for credential, we will find an email which says how the password should look like. With this information, we can attack the hashes using brute force:

```bash

hashcat -a 3 -m 1400 hash_5 susan_nasus_?d?d?d?d?d?d?d?d?d

```

#### Developed map

![[Pasted image 20240707170219.png]]

#### Sources
[[https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#erb-ruby]]
[[https://cheatsheet.haax.fr/passcracking-hashfiles/hashcat_cheatsheet/]]