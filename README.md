# UpScore

Durante este proyecto se estara usando la API de Capital One con la tematica financiera.

### Herramientas
- FrontEnd: `HTML5`, `CSS3` y `Bootstrap 5`
- BackEnd: `Flask`
- Base de datos: `SQLalchemy` / `SQLite`

## Descargar repositorio
Clona el repositorio

```bash
  git clone https://link-to-project
  cd ./capital-one
```

## Instalacion de dependencias

crear el entorno virtual
```bash 
python -m venv venv
```

activa el entorno virtual en `Windows`
```bash
.\venv\Scripts\activate
```

activa el entorno virtual en `Mac/Linux`
```bash
source venv/bin/activate
``` 

instalar Flask y las herramientas a usar
```bash 
pip install flask flask-login flask-sqlalchemy
```

o ejecutar
```bash
pip install -r requirements.txt
```
## Proceso de ejecucion

Una vez teniendo instalado los paquetes necesarios, sigue los siguientes pasos:

ejecuta 
```bash
python create_db.py
```
cambia el nombre de la carpeta `instance` por `db`, despues de ello ejecuta el servidor

```bash
python run.py
```

OPCIONAL --> Usa `DB Browser for SQLite` asi podras ver las bases de datos de manera grafica