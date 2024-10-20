from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import UploadFileForm

class FileUploadTests(TestCase):

    def test_csv_file_upload(self):
        file = SimpleUploadedFile("test.csv", b"some,csv,content")
        form = UploadFileForm(files={'file': file})
        self.assertTrue(form.is_valid())

    def test_invalid_file_upload(self):
        file = SimpleUploadedFile("test.txt", b"some,text,content")
        form = UploadFileForm(files={'file': file})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['file'], ['File type is not supported. Please upload a CSV or Excel file.'])
