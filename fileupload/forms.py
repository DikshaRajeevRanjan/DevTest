from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Select a CSV/Excel file')

    def clean_file(self):
        file = self.cleaned_data.get('file')

        # Validate file type
        if not file.name.endswith(('.csv', '.xls', '.xlsx')):
            raise forms.ValidationError('File type is not supported. Please upload a CSV or Excel file.')

        # Optionally, you can add file size validation
        if file.size > 10 * 1024 * 1024:  # Limit file size to 10MB
            raise forms.ValidationError('File size exceeds the 10 MB limit.')

        return file
