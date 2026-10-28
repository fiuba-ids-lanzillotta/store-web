# Store - Web

> **Aviso:** este proyecto es **codigo de ejemplo** con fines didacticos. Puede contener errores, simplificaciones o decisiones de diseno discutibles. Si se usa como base para un trabajo practico u otro entregable, **debe adaptarse a las buenas practicas y consignas especificas de la materia/catedra**.

## Motivacion

Frontend **server-rendered** (Flask + Jinja2) del ejemplo integrador *store*.
Renderiza el catalogo publico y una zona de administracion. **No tiene base de
datos propia** y, a proposito, **no tiene autenticacion**: la zona `/admin` es
publica para mantener el ejemplo minimo.

En `main` el sitio es **standalone**: los services devuelven datos de ejemplo
hardcodeados en `web/constants.py`. La rama
[`integracion-api`](../../tree/integracion-api) muestra el codigo que hay que
agregar para consumir la API [`store-api`](../store-api) por HTTP.

## Arquitectura (version standalone)

```
  Navegador
     |
     v
  store-web (Flask + Jinja, puerto 5001)
     |
     v
  Datos de ejemplo (web/constants.py)

  Rama integracion-api: en lugar de datos de ejemplo, los services hacen
  requests HTTP a store-api (Flask, puerto 5000, /store_api) -> MySQL
```

## Estructura del proyecto

```
store-web/
├── app.py                        # Entry point Flask (puerto 5001)
├── requirements.txt
├── .env.example
├── web/
│   ├── constants.py              # Datos de ejemplo (standalone)
│   ├── routes/
│   │   ├── site/                 # Zona publica: /, /productos, /productos/<id>
│   │   └── admin/                # Zona admin: /admin/productos, /admin/categorias
│   └── services/                 # "Capa de datos": hoy mocks, en la rama HTTP
├── templates/
│   ├── base.html                 # Layout + navbar + flash messages
│   ├── site/                     # inicio, catalogo, detalle producto
│   └── admin/                    # listados y formularios CRUD
└── static/
    └── css/estilos.css
```

Capas: `routes` (blueprints, presentacion/flujo) -> `services` (acceso a
datos). Las rutas no saben de donde salen los datos: eso es lo que permite
integrar la API en la rama `integracion-api` tocando solo `web/services/`.

## Datos de ejemplo

Las **lecturas** (catalogo, detalle, listados del admin) devuelven
`PRODUCTOS_EJEMPLO` / `CATEGORIAS_EJEMPLO` de `web/constants.py`, con la misma
forma que los DTOs de la API (las imagenes son data URIs, aca SVGs minimos).
Las **escrituras** del admin (crear/editar/eliminar) devuelven un error de
"sin backend": necesitan la API de la rama `integracion-api`.

## Configuracion y ejecucion

```bash
cp .env.example .env            # los defaults ya funcionan en local

python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux/macOS
pip install -r requirements.txt

python app.py                   # http://localhost:5001
```
