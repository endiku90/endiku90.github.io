| Name            | Crafty                                                                                                                                                                                                                                              |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Platform        | HTB                                                                                                                                                                                                                                                 |
| Difficulty      | Easy                                                                                                                                                                                                                                                |
| OS              | Windows                                                                                                                                                                                                                                             |
| Used techniques | Known vulnerability, log4s                                                                                                                                                                                                                          |
| Technologies    | minecraft, IIS, JNDI                                                                                                                                                                                                                                |
| Tools           | nmap, [minecraft-client](https://github.com/MCCTeam/Minecraft-Console-Client/releases/tag/20240713-273https://github.com/MCCTeam/Minecraft-Console-Client/releases/tag/20240713-273), [Rogue-jndi](https://github.com/veracode-research/rogue-jndi) |
| CVEs            |                                                                                                                                                                                                                                                     |

## Enumeration



tcp 80:
```shell-session
http://crafty.htb [200 OK] Country[RESERVED][ZZ], HTML5, HTTPServer[Microsoft-IIS/10.0], IP[10.10.11.249], JQuery[3.6.0], Microsoft-IIS[10.0], Script[text/javascript], Title[Crafty - Official Website]
```



#### ¿Qué es JNDI?

JNDI es una API en Java que proporciona un servicio de directorio y nombres, permitiendo a las aplicaciones Java descubrir y buscar datos y recursos utilizando nombres. JNDI se usa comúnmente para:

- Buscar objetos remotos en servidores RMI (Remote Method Invocation).
- Conectar a servicios LDAP (Lightweight Directory Access Protocol).
- Registrar y buscar recursos como bases de datos, colas de mensajería, etc.

#### JNDI injection:

La inyección JNDI (Java Naming and Directory Interface Injection) es una vulnerabilidad de seguridad que ocurre cuando una aplicación Java acepta entradas no confiables y las utiliza en consultas JNDI sin la debida validación o sanitización



### Directories





### subdomains



## Foothold




## Lateral Movement




## Privilege Escalation




#### Developed map



#### Sources

https://www.youtube.com/watch?v=w2F67LbEtnk
https://github.com/o7-Fire/Log4Shell
https://medium.com/@hackingvarangian/log4shell-vulnerability-part-1-minecraft-poc-ef770e5800de