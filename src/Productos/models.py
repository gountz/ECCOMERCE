from django.db import models

# Create your models here.
STATUS_CHOICES = (
    ('Placa de Video', ('Placa de Video')),
    ('Procesador', ('Procesador')),
    ('Mouse', ('Mouse')),
    ('Teclado', ('Teclado')),
)
class Producto(models.Model):
    title = models.CharField(max_length=80)
    category = models.CharField(choices=STATUS_CHOICES, default="Placa de Video", max_length=15)
    imagen = models.ImageField(upload_to='productos',null=True,blank=True)
    description = models.TextField(max_length=155)
    precio = models.IntegerField(default=0)
    def __str__(self):
        return f'Producto: {self.title} | categoria: {self.category} | precio:{self.precio}'
    class Meta:
        ordering = ["-id"]