Crear entorno virtual
python -m venv .venv

Activar entorno (PowerShell)
.venv\Scripts\Activate

Activar entorno (Git Bash)
source .venv/Scripts/activate

Instalar dependencias
pip install -r requirements.txt

Guardar dependencias
pip freeze > requirements.txt

Salir del entorno
deactivate
