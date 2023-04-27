from django.db import models
from login.models import User

class Solicitudes(models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    usr_envia = models.ForeignKey(User, verbose_name='user_envia', related_name='user_env', on_delete=models.CASCADE)
    usr_recibe = models.ForeignKey(User, verbose_name='user_recibe', related_name='user_rec', on_delete=models.CASCADE)
    
    
    class ElegirTipo(models.TextChoices):
        PENDING = 'PENDIENTE'
        ACCEPTED = 'ACEPTADA'
        REJECTED = 'RECHAZADA'
    
    
    estado = models.CharField(choices=ElegirTipo.choices, null=False, default=ElegirTipo.PENDING, max_length=9)    
    
    class Meta:
        db_table = 'solicitudes'
