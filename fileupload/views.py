from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import pandas as pd
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            try:
                # Process CSV or Excel file
                if file.name.endswith('.csv'):
                    df = pd.read_csv(file)
                else:
                    df = pd.read_excel(file)

                # Generate the summary
                summary = df.describe().to_string()

                # Send the summary as the email body
                # send_mail(
                #     'File Upload Summary',  # Email subject
                #     summary,  # Email body (the summary)
                #     settings.EMAIL_HOST_USER,  # From email
                #     ['tech@themedius.ai'],  # To email
                #     fail_silently=False,
                # )
                send_mail(
                    'Python Assignment - Diksha Rajeev Ranjan Gupta',  # Updated subject
                    summary,  # Email body (the summary)
                    settings.EMAIL_HOST_USER,  # From email
                    ['tech@themedius.ai'],  # To email
                    fail_silently=False,
                )


                # Show a success message
                messages.success(request, 'File uploaded and summary sent via email.')
                return HttpResponse(f'<h2>File Summary</h2><br>{df.describe().to_html(classes="table table-hover table-bordered")}')
            except Exception as e:
                messages.error(request, f'An error occurred while processing the file: {e}')
        else:
            messages.error(request, 'Invalid file format. Please upload a CSV or Excel file.')
    else:
        form = UploadFileForm()

    return render(request, 'fileupload/upload.html', {'form': form})
