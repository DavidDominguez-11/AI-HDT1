# Task 4 - HDT1

Implementación de un sistema de control de temperatura utilizando un agente inteligente que regula automáticamente la temperatura de un entorno simulado.

## Características

- Simulación de entorno con temperatura variable
- Agente inteligente que toma decisiones basadas en la temperatura actual
- Sistema de retroalimentación para el control de temperatura

## Requisitos Previos

- Python 3.6 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clona el repositorio:
   ```bash
   git clone [URL_DEL_REPOSITORIO]
   cd AI-HDT1
   ```

2. Crea y activa un entorno virtual (recomendado):
   - Windows (PowerShell):
     ```powershell
     python -m venv .venv
     .venv\Scripts\Activate
     ```
   - Linux/MacOS (bash/zsh):
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

## Uso

Ejecuta el programa principal con:

```bash
python main.py
```

El programa simulará 10 iteraciones del sistema de control de temperatura, mostrando:
- Temperatura actual
- Acción tomada por el agente
- Nueva temperatura después de la acción

## Estructura del Proyecto

```
AI-HDT1/
├── main.py          # Código fuente principal
├── README.md        # Este archivo
└── requirements.txt # Dependencias del proyecto (vacío)
```

## Cómo funciona

1. El entorno simulado genera una temperatura aleatoria inicial entre 15°C y 30°C
2. El agente percibe la temperatura actual
3. Basado en la temperatura, el agente decide:
   - **Enfriar** si la temperatura es mayor a 25°C
   - **Calentar** si la temperatura es menor a 18°C
   - **Esperar** si la temperatura está entre 18°C y 25°C
4. El entorno se actualiza según la acción del agente
5. El proceso se repite para 10 iteraciones