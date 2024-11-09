from django.db import models

class TipoSolo(models.Model):
    nome = models.CharField(max_length=100)
    ph_min = models.DecimalField(max_digits=3, decimal_places=1)
    ph_max = models.DecimalField(max_digits=3, decimal_places=1)
    mo_min = models.DecimalField(max_digits=3, decimal_places=1)
    mo_max = models.DecimalField(max_digits=3, decimal_places=1)
    fosforo_min = models.DecimalField(max_digits=5, decimal_places=2)
    fosforo_max = models.DecimalField(max_digits=5, decimal_places=2)
    potassio_min = models.DecimalField(max_digits=5, decimal_places=2)
    potassio_max = models.DecimalField(max_digits=5, decimal_places=2)
    calcio_min = models.DecimalField(max_digits=5, decimal_places=2)
    calcio_max = models.DecimalField(max_digits=5, decimal_places=2)
    magnesio_min = models.DecimalField(max_digits=5, decimal_places=2)
    magnesio_max = models.DecimalField(max_digits=5, decimal_places=2)
    saturacao_bases = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome
