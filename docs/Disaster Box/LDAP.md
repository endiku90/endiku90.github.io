
LDAP, o **Lightweight Directory Access Protocol** (Protocolo Ligero de Acceso a Directorios), es un protocolo estándar para acceder y mantener servicios de directorio distribuidos a través de una red. LDAP es utilizado principalmente para buscar información en una estructura jerárquica de directorios y es ampliamente empleado en diversas aplicaciones y servicios, incluyendo autenticación de usuarios, búsqueda de contactos, gestión de acceso y más.


LDAP enables organizations to manage users centrally, as well as groups and other directory information, often used for authentication and authorization purposes in web and internal applications.

LDAP soporta varias operaciones básicas, incluyendo:

- **Bind:** Autenticar y establecer una sesión con el servidor LDAP.
- **Search:** Buscar y recuperar entradas del directorio.
- **Compare:** Comparar un valor con un atributo en una entrada.
- **Modify:** Modificar atributos de una entrada.
- **Add:** Añadir una nueva entrada al directorio.
- **Delete:** Eliminar una entrada del directorio.
- **Unbind:** Terminar la sesión con el servidor LDAP.

### Usos principales de LDAP:

1. **Autenticación y Autorización:**
    
    - LDAP es comúnmente utilizado en sistemas de autenticación para validar credenciales de usuario. Los servidores de autenticación, como Microsoft [[Active Directory]], utilizan LDAP para gestionar usuarios y permisos.
2. **Búsqueda y Directorios de Contactos:**
    
    - LDAP es utilizado para buscar información en grandes directorios de contactos, como en entornos corporativos donde se necesita acceder a información de empleados.
3. **Gestión de Recursos:**
    
    - LDAP puede ser usado para gestionar recursos como equipos, impresoras y aplicaciones dentro de una organización.


### Cómo se organiza?

Cada entrada en el directorio LDAP tiene un identificador único llamado **Distinguished Name (DN)**. Un DN es una cadena que especifica el camino desde la raíz del directorio hasta la entrada específica.

Está bien explicado en THM:

![[Pasted image 20240729171335.png]]


En el top tenemos el **top-level domain (TLD),** como dc=ldap y dc=thm. Esto desciende como un árbol, seguido de las **unidades organizacionales (ou)**. 
- Los **DN** de antes mencionados, son todos los eslabones hasta llegar al TLD, es decir, por ejemplo *cn = John Doe, ou = people, dc = ldap, dc = thm* sería un DN.
- Luego tenemos los **RDN** (Relative Distinguished Names), que podríamos verlo como el análogo al *relative path y absolut*, como ejemplo sería *cn = John Doe*.
- También hay atributos que corresponden a cada *entry*, por ejemplo mail. 


## Queries

Para navegar en un árbol LDAP y obtener información de las entradas, debemos saber cómo utilizar las queries. 

La sintaxis de las queries es la siguiente:
```default
(base DN) (scope) (filter) (attributes)
```

1. Base DN, es el punto de partida para buscar.
2. Scope, define qué tan profundo hay que buscar:
	1. base, solo busca en la base. (el punto 1.)
	2. one, sólo busca en el escalón siguiente (next child)
	3. sub, busca todo lo que hay abajo.
3. Filter
4. Atributos, qué nos interesa devolver de la entrada buscada.
#### Filtros
equality (`=`), presence (`=*`), greater than (`>=`), and less than (`<=`), wildcard `*`.

For a more complex search query, filters can be used with each other using logical operators such as AND (`&`), OR (`|`), and NOT (`!`).

```default
(&(objectClass=user)(|(cn=John*)(cn=Jane*)))
```

# Injections

### Common Attack Vectors

1. **Authentication Bypass:** Modifying LDAP authentication queries to log in as another user without knowing their password.
2. **Unauthorized Data Access:** Altering LDAP search queries to retrieve sensitive information not intended for the attacker's access.
3. **Data Manipulation:** Injecting queries that modify the LDAP directory, such as adding or modifying user attributes.


### Authentication Bypass Techniques

**Tautology-Based Injection**

Tautology-based injection involves inserting conditions into an LDAP query that are inherently true, thus ensuring the query always returns a positive result, irrespective of the intended logic.

```php
(&(uid={userInput})(userPassword={passwordInput}))
```

An attacker could provide a tautology-based input, such as `*)(|(&` for `{userInput}` and `pwd)` for `{passwordInput}` which transforms the query into:

```php
(&(uid=*)(|(&)(userPassword=pwd)))
```


**Blind Injection**

Al igual que en sql, podemos averiguar información comparando las respuestas del servidor.


## Sources
https://tryhackme.com/r/room/ldapinjection
