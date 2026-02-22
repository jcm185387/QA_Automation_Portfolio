# Proyecto 4: API CRUD con Integración CI/CD ## 
🎯 Objetivo Este proyecto demuestra la automatización de pruebas de API con autenticación y operaciones CRUD (Create, Read, Update, Delete), integradas en un pipeline de CI/CD con **GitHub Actions**. El propósito es mostrar cómo las pruebas se ejecutan automáticamente en cada push al repositorio, generando evidencia y reportes profesionales. 
--- 
## 📂 Estructura del proyecto

royecto4_API_CRUD_CICD/
│
├── tests/
│   ├── test_auth.py          # pruebas de login/autenticación
│   ├── test_create.py        # pruebas de creación de recurso
│   ├── test_read.py          # pruebas de lectura de recurso
│   ├── test_update.py        # pruebas de actualización
│   ├── test_delete.py        # pruebas de eliminación
│
├── reports/                  # reportes HTML generados con pytest-html
├── evidence/                 # evidencia adicional (JSON, logs)
├── requirements.txt          # dependencias del proyecto
├── README.md                 # documentación del proyecto
└── .github/
└── workflows/
└── ci.yml            # pipeline de GitHub Actions

---

## ⚙️ Tecnologías utilizadas
- **Python 3.10+**
- **Pytest** para ejecución de pruebas
- **Requests** para consumo de APIs
- **Pytest-HTML** para generación de reportes
- **GitHub Actions** para CI/CD

---

## ▶️ Ejecución local
1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt


2. Ejecutar pruebas con reporte HTML:
pytest -v --html=reports/report.html --self-contained-html
Revisar el reporte en reports/report.html.

3. Revisar el reporte en reports/report.html.
El archivo .github/workflows/ci.yml define el flujo de integración continua:
Se ejecuta en cada push o pull request a la rama main.
Instala dependencias.
Corre los tests con Pytest.
Genera un reporte HTML en la carpeta reports/.


## 📦 Instalación de dependencias 
Este proyecto utiliza un archivo `requirements.txt` para gestionar las librerías necesarias: 
```text
pytest==8.2.0
requests==2.31.0 
pytest-html==4.2.0