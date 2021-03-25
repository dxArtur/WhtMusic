from django.db import models

# Create your models here.

class Watcher(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Player(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Vibe(models.Model):
    nome = models.CharField(max_length=100)
    data_upload = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Vibes'


class Genero(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Generos'


class Musica(models.Model):
    nome = models.CharField(max_length=100)
    vibe = models.ForeignKey(Vibe, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    historia = models.TextField(null=True, blank=True)
    data_upload = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Musicas'