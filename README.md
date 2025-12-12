# Automation Boot — Python + Selenium + Edge + Pytest

Framework base de automatización web en **Python** usando **Selenium**, **Microsoft Edge (EdgeDriver)** y **pytest**.
Incluye:
- Page Object Model (POM)
- Esperas explícitas (WebDriverWait)
- Ejecución con pytest
- Reporte HTML con **screenshot adjunta por test**

---

## ✅ Requisitos

- **Python 3.10+** (recomendado 3.12)
- **Microsoft Edge** instalado
- **Git** instalado
- **EdgeDriver** compatible con tu versión de Edge

> Para ver tu versión de Edge:
> Abre Edge y entra a `edge://settings/help`

---

## 📥 1) Descargar el repositorio

### Opción A: Clonar con Git
```bash
git clone https://github.com/DanteZMedina/Bot-busquedas-bing.git
cd TU_REPO
```
###  Opción B: Descargar ZIP

En GitHub, haz clic en Code → Download ZIP

Extrae el ZIP

Abre la carpeta del proyecto en tu terminal


🧪 2) Crear y activar el entorno virtual (venv)
Crear venv
```bash
python -m venv venv
```
Activar venv
Git Bash (MINGW64)
```bash
source venv/Scripts/activate
```
PowerShell
```bash
venv\Scripts\Activate.ps1
```
✅ Si se activó verás (venv) al inicio de la línea.
📦 3) Instalar dependencias
```bash
pip install -r requirements.txt
```
Si no tienes requirements.txt por alguna razón:
```bash
pip install selenium pytest pytest-html openpyxl
```
🧩 4) Configurar EdgeDriver (obligatorio)
Este proyecto usa EdgeDriver local (ideal para redes corporativas/firewall).

4.1 Descargar EdgeDriver
Descárgalo desde el sitio oficial:
Microsoft Edge WebDriver (elige la versión que coincida con tu Edge)
4.2 Colocar el ejecutable
Coloca el archivo:
msedgedriver.exe
en la carpeta:
```bash
drivers/msedgedriver.exe
```
Nota: el .exe NO se sube al repo por seguridad/buenas prácticas (está ignorado por .gitignore).
▶️ 5) Ejecutar los tests
Ejecutar normal
```bash
pytest -v
```
Ejecutar con reporte HTML (con screenshots embebidas)
```bash
pytest -v --html=reports/bing_report.html --self-contained-html
```
📄 El reporte se genera en:
```bash
reports/bing_report.html
```
📁 Estructura del proyecto
```bash
.
├── conftest.py
├── requirements.txt
├── README.md
├── drivers/
│   └── (coloca aquí msedgedriver.exe)
├── pages/
│   ├── base_page.py
│   └── bing_search_page.py
├── tests/
│   └── test_bing_searches.py
├── data/
│   └── bing_queries.py
├── utils/
│   ├── throttling.py
│   └── screenshot.py (si aplica en tu versión)
└── reports/
    └── (se genera al ejecutar)
```
🔎 ¿Qué hace el flujo de Bing?
1. Abre Bing
2. Escribe la query de forma progresiva (pausas pequeñas)
3. Ejecuta la búsqueda
4. Espera a que carguen resultados (esperas explícitas)
5. Genera reporte HTML con screenshot por test
6. Este enfoque está pensado como automatización controlada (no agresiva), con fines educativos / QA.

🛠️ Troubleshooting
Estás en Git Bash. Usa:
```bash
source venv/Scripts/activate
```
2) EdgeDriver no abre / error de versión

Tu EdgeDriver no coincide con tu Edge. Verifica:

edge://settings/help
y descarga el EdgeDriver correspondiente.

3) No se genera el reporte HTML
Asegúrate de correr:
```bash
pytest -v --html=reports/bing_report.html --self-contained-html
```
Y que pytest-html esté instalado:
```bash
pip show pytest-html
```



⚠️ Notas

El EdgeDriver debe colocarse manualmente en la carpeta drivers/
Las evidencias (screenshots / reportes) no se versionan
Automatización con enfoque ético y controlado

👤 Autor
Dante Medina