# Automation Framework - Selenium + Python + Edge

Framework de automatización web desarrollado en Python utilizando Selenium, pytest y EdgeDriver.

## 🧰 Tecnologías
- Python 3.12
- Selenium
- Pytest
- Pytest-HTML
- Microsoft Edge

## 📂 Estructura
pages/
tests/
utils/
data/
drivers/
reports/

## ▶️ Ejecución
```bash
# Activar entorno virtual
source venv/Scripts/activate

# Ejecutar tests
pytest -v --html=reports/report.html --self-contained-html

⚠️ Notas

El EdgeDriver debe colocarse manualmente en la carpeta drivers/

Las evidencias (screenshots / reportes) no se versionan

Automatización con enfoque ético y controlado

👤 Autor

Dante Medina