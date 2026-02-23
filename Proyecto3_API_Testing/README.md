# Proyecto 3: Pruebas de API con Python y Pytest

Este proyecto valida endpoints públicos utilizando **Python**, **Requests** y **Pytest**.  
El objetivo es demostrar la capacidad de automatizar pruebas de servicios REST y documentar resultados de manera clara.

## Herramientas
- Lenguaje: Python
- Framework de pruebas: Pytest
- Cliente HTTP: Requests
- Reportes: Pytest (con salida en consola y opción de integración futura con CI/CD)

## Casos de prueba
1. Validar respuesta exitosa (código 200) de un endpoint público.
2. Verificar estructura del JSON devuelto.
3. Validar campos específicos dentro de la respuesta.
4. Manejo de errores (códigos 404, 500).
5. Pruebas parametrizadas para distintos endpoints.

## Cobertura de pruebas negativas Además de validar escenarios exitosos, este proyecto incluye **pruebas negativas** para asegurar la robustez del sistema. Ejemplo: se solicita un recurso inexistente y se valida que el servicio responda con un **código 404**. ```python def test_get_invalid_post_returns_404(): response = requests.get("https://jsonplaceholder.typicode.com/posts/999999") assert response.status_code == 404

## Ejecución
```bash
pip install -r requirements.txt
pytest -v tests/test_api.py


## Reportes HTML con historial 
Este proyecto genera reportes visuales de las ejecuciones usando **pytest-html**. 
Cada ejecución crea un archivo único con fecha y hora en el nombre, almacenado en la carpeta `reports/`. 

Ejemplo de ejecución en Linux/Mac: 
```bash 
pytest -v --html=reports/report_$(date +"%Y-%m-%d_%H-%M-%S").html --self-contained-html

Ejemplo de ejecución en Windows PowerShell:
pytest -v --html=reports/report_$(Get-Date -Format "yyyy-MM-dd_HH-mm-ss").html --self-contained-html
