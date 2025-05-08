# Data Analyzer Django

Proyecto web hecho con **Django + Pandas** que permite subir archivos `.csv`, procesarlos automáticamente y mostrar estadísticas básicas como media, mediana, desviación estándar, etc.

---

## Funcionalidades

-  Subida de archivos CSV
-  Análisis automático con Pandas
-  Tabla con estadísticas descriptivas (`mean`, `count`, `std`, etc.)
-  Interfaz simple con Bootstrap
-  Soporte para múltiples columnas numéricas

---

## Tecnologías utilizadas

- Python 3
- Django 5
- Pandas
- Matplotlib (opcional para visualización)
- Bootstrap 5 (CDN)

```bash
 Subí tu archivo CSV
 Mostrá estadísticas automáticamente

---

## Cómo ejecutar el proyecto

1. Cloná el repositorio:

```bash
git clone https://github.com/maurorecalde/data-analyzer-django.git
cd data-analyzer-django

2. Creá y activá un entorno virtual
python -m venv venv
venv\Scripts\activate    # En Windows
source venv/bin/activate # En Mac/Linux

3. Instalá las dependencias
pip install -r requirements.txt

4.Aplicá las migraciones
python manage.py migrate

5. Ejecuta el servidor
python manage.py runserver

Estructura de carpetas destacadas
data_analyzer_project/
├── data_app/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── templates/
│   │   └── upload.html
├── media/           ← Archivos CSV subidos
├── static/          ← Archivos estáticos (opcional)
├── manage.py
└── requirements.txt

## Contacto

**Mauro Recalde**  
🔗 [github.com/maurorecalde]

---

¡Podés seguir mejorándolo agregando gráficos, filtros o exportación a Excel!

