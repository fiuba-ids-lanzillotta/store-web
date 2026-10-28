# Store - Web

> **Aviso:** este proyecto es **codigo de ejemplo** con fines didacticos. Puede contener errores, simplificaciones o decisiones de diseno discutibles. Si se usa como base para un trabajo practico u otro entregable, **debe adaptarse a las buenas practicas y consignas especificas de la materia/catedra**.

## Motivacion

Frontend **server-rendered** (Flask + Jinja2) del ejemplo integrador *store*.
Renderiza el catalogo publico y una zona de administracion, consumiendo la API
[`store-api`](../store-api) por HTTP. **No tiene base de datos propia** y,
a proposito, **no tiene autenticacion**: la zona `/admin` es publica para
mantener el ejemplo minimo.

Esta rama (`integracion-api`) contiene el codigo de integracion con el backend;
en `main` el sitio es standalone (los services devuelven datos de ejemplo).

## Arquitectura

```
  Navegador
     |
     v
  store-web (Flask + Jinja, puerto 5001)
     |
     |  requests.get/post/put/delete (JSON)
     v
  store-api (Flask, puerto 5000, /store_api)
     |
     v
  MySQL 8
```

## Estructura del proyecto

```
store-web/
├── app.py                        # Entry point Flask (puerto 5001)
├── requirements.txt
├── .env.example
├── web/
│   ├── constants.py              # API_BASE_URL + datos de ejemplo (fallback)
│   ├── routes/
│   │   ├── site/                 # Zona publica: /, /productos, /productos/<id>
│   │   └── admin/                # Zona admin: /admin/productos, /admin/categorias
│   └── services/                 # Llamadas HTTP a store-api (requests)
├── templates/
│   ├── base.html                 # Layout + navbar + flash messages
│   ├── site/                     # inicio, catalogo, detalle producto
│   └── admin/                    # listados y formularios CRUD
└── static/
    └── css/estilos.css
```

Capas: `routes` (blueprints, presentacion/flujo) -> `services` (llamadas HTTP a
la API). Las rutas no tienen logica de cliente HTTP; los services encapsulan
`requests`.

## Contacto

`/contacto` tiene un formulario (nombre, email, mensaje) que envia un email a la
casilla del admin (`CONTACTO_EMAIL`) via SMTP con **Flask-Mail** (mismo patron
que `gradebook-mailer`): si no hay credenciales `MAIL_*` en el `.env`, no se
envia nada y el mensaje solo se loguea (modo dev). El HTML del email vive en
`templates/emails/contacto.html`.

## Datos de ejemplo (fallback sin backend)

Si la API no responde, las **lecturas** devuelven los datos hardcodeados en
`web/constants.py` (`CATEGORIAS_EJEMPLO` / `PRODUCTOS_EJEMPLO`, con la misma
forma que los DTOs de la API), asi el sitio se puede ver y navegar sin el
backend. Las **escrituras** del admin (crear/editar/eliminar) si necesitan la
API: sin backend devuelven un error de conexion y no guardan nada.

Las **imagenes** se suben como archivo en el form del admin; el service las
convierte a data URI base64 (`archivo_a_data_uri`) y la API las guarda asi en
la columna `imagen` (LONGTEXT). Los mocks usan SVGs minimos.

## Configuracion y ejecucion

```bash
cp .env.example .env            # los defaults ya funcionan en local

python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux/macOS
pip install -r requirements.txt

python app.py                   # http://localhost:5001
```

> El catalogo y el admin consumen `store-api` (y esta, MySQL via
> `docker compose up -d`). Si la API esta caida, las paginas se ven igual con
> los datos de ejemplo, pero el admin no puede guardar cambios.
