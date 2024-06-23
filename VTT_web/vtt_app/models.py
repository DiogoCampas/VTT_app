from django.db import models

# Create your models here.


class MedicalImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class TestResult(models.Model):
    image = models.ForeignKey(MedicalImage, on_delete=models.CASCADE)
    clinician_name = models.CharField(max_length=100)
    diagnosis = models.TextField()
    confidence = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)