from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from django.contrib import messages
import pandas as pd

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            try:
                # Handling CSV and Excel files
                if file.name.endswith('.csv'):
                    df = pd.read_csv(file)
                else:
                    df = pd.read_excel(file)

                # Create styled summary report
                summary = df.describe().to_html(classes="table table-striped table-bordered")
                
                # Feedback success message
                messages.success(request, 'File successfully uploaded and processed!')
                return HttpResponse(f'<h2>File Summary</h2><br>{summary}')
            except Exception as e:
                messages.error(request, f'An error occurred while processing the file: {e}')
        else:
            messages.error(request, 'Invalid file format. Please upload a CSV or Excel file.')

    else:
        form = UploadFileForm()

    return render(request, 'fileupload/upload.html', {'form': form})
