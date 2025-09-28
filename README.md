# EDA de tendencias climáticas (temperatura y precipitaciones)

## Objetivo
Analizar la evolución de la **temperatura media** y las **precipitaciones** por ciudad y detectar **tendencias (°C/década)**, **anomalías** y **relaciones** básicas.

## Estructura
- `data/temperaturas.csv`, `data/precipitaciones.csv`
- `src/csv_loader.py`, `src/transforms.py`, `src/analysis.py`

## Ejecucion
```bash
python -m venv .venv
.venv/Scripts/activate 
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter notebook