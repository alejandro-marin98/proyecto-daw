from django.db import models
from login.models import User

class Libros(models.Model):
    isbn = models.CharField(null=False, primary_key=True, max_length=13)
    titulo = models.CharField(null=False, unique=True, max_length=150)
    paginas = models.IntegerField(null=False)
    autor = models.CharField(null=False, max_length=30)
    foto = models.ImageField(upload_to="images/", null=True, blank=True)
    sinopsis = models.CharField(null=True, blank=True, max_length=10000)
    class Meta:
        db_table = 'libros'
    
    def __str__(self):
        return f'{self.titulo} ({self.isbn})'

class Listas(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Libros, on_delete=models.CASCADE)
    estado = models.CharField(default='pendiente', max_length=20)
    
    class Meta:
        db_table = 'listas'

class Opiniones(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Libros, on_delete=models.CASCADE)
    opinion = models.CharField(blank=False, max_length=255)
    
    class Meta:
        db_table = 'opiniones'
