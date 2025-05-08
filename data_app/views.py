from django.shortcuts import render
from .forms import ArchivoCSVForm
from django.core.files.storage import default_storage
import pandas as pd

def upload_file(request):
    df_html = None
    error = None

    if request.method == 'POST':
        form = ArchivoCSVForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Guardamos el archivo de forma temporal
            archivo = request.FILES['archivo']
            file_path = default_storage.save('tmp/' + archivo.name, archivo)

            try:
                with default_storage.open(file_path, mode='r') as f:
                    df = pd.read_csv(f)
                    df_html = df.describe().to_html(classes='table table-bordered')
            except Exception as e:
                error = f"⚠️ Error al leer el archivo: {e}"
    else:
        form = ArchivoCSVForm()

    return render(request, 'upload.html', {'form': form, 'df_html': df_html, 'error': error})
