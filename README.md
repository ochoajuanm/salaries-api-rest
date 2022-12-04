# Paginación de API REST

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)

Este proyecto tiene como finalidad exponer los datos de una base de datos de numerosos registros mediante una API que pueda paginar los resultados. La API fue desarrollada en Flask y se creó una base PostgreSQL poblada con un dataset de [Kaggle](https://www.kaggle.com/datasets/kaggle/sf-salaries)

## Estructura del proyecto

```bash
.
├── Dockerfile
├── exceptions.py
├── extensions.py
├── models.py
├── README.md
├── requirements.txt
├── schemas.py
├── server.py
├── template.env # Se debe renombrar a '.env' e indicar las variables de entorno
└── utils.py
```

## Configuración del entorno e instalación de dependencias

Se debe usar el gestor de dependencias [pip](https://pip.pypa.io/en/stable/):


```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 server.py
```

## Ejecución con Docker

Realizamos build de la imagen partiendo de una imagen de Python

```bash
docker build -t salaries-api .
docker run -p 80:1337 -it salaries-api /bin/bash
```

Una vez dentro del contenedor ejecutamos

```bash
python3 server.py
```

Finalmente podemos ejecutar http://127.0.0.1:80/salaries?page=1&per-page=100 y veremos los resultados
