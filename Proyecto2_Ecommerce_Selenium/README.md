# Proyecto 2: Automatización de flujo de compra en e-commerce

Este proyecto automatiza el proceso de compra en el sitio demo:
https://www.saucedemo.com/

## Herramientas
- Lenguaje: Python
- Framework: Selenium
- Reportes: Pytest

## Casos de prueba
1. Login con credenciales válidas
2. Selección de producto
3. Agregar al carrito
4. Checkout con datos de usuario
5. Validación de mensaje de confirmación

## Ejecución
```bash
python test_ecommerce.py

## 🎯 Qué demuestra este proyecto 
- Automatización de un flujo completo de negocio (login → compra → confirmación). 
- Validación de resultados con aserciones. 
- Documentación y estructura profesional del proyecto.

## Evidencia visual
Durante la ejecución se generan capturas de pantalla en cada paso:
- `01_login.png` → Login exitoso
- `02_carrito.png` → Producto agregado al carrito
- `03_checkout.png` → Datos de checkout completados
- `04_confirmacion.png` → Mensaje de confirmación de compra
