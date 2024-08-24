| Name            | Sea                                                                                                                  |
| --------------- | -------------------------------------------------------------------------------------------------------------------- |
| Platform        | HTB                                                                                                                  |
| Difficulty      | Easy                                                                                                                 |
| OS              | Linux                                                                                                                |
| Used techniques | sudomain enumeration,  SQLi, crack hashes, File Upload attack, credentials finding, reverse, wildcards spare tricks. |
| Technologies    | Laravel, Laravel-admin                                                                                               |
| Tools           | gobuster,  BurpSuite, sqlmap, nc, strings                                                                            |
| CVEs            | cve-2023-24249                                                                                                       |

## Enumeration


![[Pasted image 20240812170319.png]]

After inspecting the web, we found some form where it drives us to nothing. 
Using feroxbuster we find some directories that show us the CMS on use.
### Directories





### subdomains



## Foothold




## Lateral Movement




## Privilege Escalation




#### Developed map



#### Sources
