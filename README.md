# 🎬 API de películas

## 1. Descripción del proyecto

Este proyecto consiste en la creación de una API REST utilizando **FastAPI** para gestionar un catálogo de películas.

La API permite realizar diferentes operaciones sobre una colección de películas almacenadas en un archivo JSON.

Cada película contiene los siguientes campos:

- **id:** identificador único de la película.
- **titulo:** título de la película.
- **director:** nombre del director.
- **anio:** año de estreno.

## 2. Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **FastAPI:** framework para desarrollar la API.
- **Pydantic:** validación de los datos.
- **JSON:** almacenamiento de las películas.
- **Uvicorn:** servidor para ejecutar la API.

## 3. Instalación y ejecución

Para ejecutar el proyecto en local, sigue estos pasos:

**1. Clonar el repositorio**

```bash
git clone https://github.com/paulals1128/fastapi-paula.git
```

**2. Entrar en la carpeta del proyecto**

```bash
cd fastapi-paula
```

**3. Crear y activar el entorno virtual**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**4. Instalar las dependencias**

```bash
pip install fastapi uvicorn
```

**5. Iniciar el servidor**

```bash
uvicorn main:app --reload
```

Una vez iniciado, la API estará disponible en:

- API: http://127.0.0.1:8000
- Documentación interactiva: http://127.0.0.1:8000/docs

## 4. Rutas de la API

La API dispone de cinco rutas principales:

| Método | Ruta | Función |
|---|---|---|
| GET | `/peliculas` | Mostrar todas las películas. |
| GET | `/peliculas/{id}` | Buscar una película por su ID. |
| POST | `/peliculas` | Añadir una película nueva. |
| PUT | `/peliculas/{id}` | Editar una película existente. |
| DELETE | `/peliculas/{id}` | Eliminar una película. |

### Funcionamiento

- **Listar:** muestra todas las películas del catálogo.
- **Buscar:** encuentra una película mediante su ID. Si no existe, devuelve un error 404.
- **Agregar:** permite añadir una película nueva y genera automáticamente su ID.
- **Editar:** permite modificar los datos de una película existente. Si no existe, devuelve un error 404.
- **Borrar:** elimina una película del catálogo. Si no existe, devuelve un error 404.

Los cambios se guardan en el archivo JSON y se mantienen aunque se reinicie el servidor.


