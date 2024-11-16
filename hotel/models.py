from django.db import models
from rest_framework.views import APIView


class Klassi(models.Model):
    nomi = models.CharField(max_length=50, verbose_name='nomi')
    narxi = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='narxi')

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name = "Klass"
        verbose_name_plural = "Klasslar"


class Mehmonhona(models.Model):
    nomi = models.CharField(max_length=50, verbose_name='nomi')
    stars = models.IntegerField()
    narxi = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='narxi')

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name = "Mehmonhona"
        verbose_name_plural = "Mehmonhonalar"


class Travel(models.Model):
    nomi = models.CharField(max_length=50, verbose_name='nomi')
    izoh = models.CharField(max_length=500, verbose_name='izoh')
    muddati = models.DateField(verbose_name='muddati')
    narxi = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='narxi')
    klass = models.ForeignKey(Klassi, on_delete=models.CASCADE, verbose_name='klass')
    mehmonhona = models.ForeignKey(Mehmonhona, on_delete=models.CASCADE, verbose_name='mehmonhona')


    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name = 'Sayohat'
        verbose_name_plural = 'Sayohatlar'
