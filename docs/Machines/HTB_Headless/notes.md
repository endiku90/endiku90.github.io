| Name            | Headless                                                    |
| --------------- | ----------------------------------------------------------- |
| Platform        | HTB                                                         |
| Difficulty      | Easy                                                        |
| OS              | Linux                                                       |
| Used techniques | DOM XSS, Header injection, Command Injection, relative path |
| Technologies    | web app                                                     |
| Tools           | nmap, nc,                                                   |
| CVEs            | none                                                        |

## Enumeration


![[Pasted image 20240724154028.png]]

Two open ports, one corresponds to ssh and the other to some http service with no information about the domain or technologies. 

![[Pasted image 20240724154210.png]]



### Directories

- /support
	- Possible injection, but it seems sanitized when we try basic xss. After trying some xss, one message shows up and

![[Pasted image 20240724154539.png]]

There we can see that there is a cookie that can be used to personify as admin, and that this request *has been sent to the administrators for investigation.*

- /dashboard
	- no Authorization. There we may need the token from above.


### Subdomains

none.

## Foothold


The successful injection occurs on the **User-Agent** header, there we can paste the payload and wait till the administrators checks the hacking attempt. 

![[Pasted image 20240724153903.png]]

Once we got the admin token, we can visit /dashboard. There, there is just one functionality "Generate Report". If we inspect the request made, we can inject commands in the "date" parameter:

![[Pasted image 20240724153950.png]]

![[Pasted image 20240724145618.png]]



## Lateral Movement

No other users.


## Privilege Escalation

Once we are *dvir*,  with basic enumeration we can see that we can execute one script as **sudo**. If we check it, we can realize that one script is executed using his **relative path**. 

![[Pasted image 20240724151628.png]]

Exploitation in this case is direct: just create a **initdb.sh** which executes bash and then execute **/usr/bin/syscheck** in the same directory.

#### Developed map

![[Headless10.10.16.8.jpg]]
#### Sources

[[https://book.hacktricks.xyz/pentesting-web/xss-cross-site-scripting#xss-common-payloads]]