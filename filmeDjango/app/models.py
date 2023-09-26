from django.db import models

class Paises(models.Model):
    nome = models.CharField()
    continente = models.CharField()
    def __str__(self):
        return f'{self.nome} {self.continente}'

class AtoresDiretores(models.Model):
    nome = models.CharField()
    site = models.CharField()
    insta = models.CharField()
    face = models.CharField()
    twitter = models.CharField()
    nacionalidade = models.CharField()
    def __str__(self):
        return f'{self.nome} {self.site} {self.insta} {self.face} {self.twitter} {self.nacionalidade}'

class Genero(models.Model):
    nome = models.CharField()
    def __str__(self):
        return self.nome

class Filme(models.Model):
    nome = models.CharField()
    duracao = models.IntegerField()
    sinopse = models.CharField()
    site_oficial = models.CharField()
    data_lancamento = models.DateField()
    nota_avaliacao = models.IntegerField()
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE)
    pais = models.ForeignKey(Paises, on_delete=models.CASCADE)
    diretor = models.ForeignKey(AtoresDiretores, on_delete= models.CASCADE)
    def __str__(self):
        return  f'{self.nome} {self.duracao} {self.sinopse} {self.site_oficial} {self.data_lancamento} {self.nota_avaliacao} {self.genero} {self.pais} {self.diretor}'

class FilmeAtores(models.Model):
    filme = models.CharField()
    ator =  models.ForeignKey(AtoresDiretores, on_delete= models.CASCADE)
    def __str__(self):
        return f'{self.filme} {self.ator}'


class Series(models.Model):
    nome = models.CharField()
    duracao = models.IntegerField()
    sinopse = models.CharField()
    site_oficial = models.CharField()
    data_lancamento = models.DateField()
    nota_avaliacao = models.IntegerField
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    pais = models.ForeignKey(Paises, on_delete=models.CASCADE)
    diretor = models.ForeignKey(AtoresDiretores, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nome} {self.duracao} {self.sinopse} {self.site_oficial} {self.data_lancamento} {self.nota_avaliacao} {self.genero} {self.pais} {self.diretor}'
    
class Episodios(models.Model):
    nome = models.CharField()
    duracao = models.CharField()
    data_disponibilizacao = models.DateField()
    def __str__(self):
        return f'{self.nome} {self.duracao} {self.data_disponibilizacao}'

class Temporadas(models.Model):
    temporada = models.CharField()
    def __str__(self):
        return self.temporada

class SeriesComEpisodios(models.Model):
    serie = models.ForeignKey(Series, on_delete=models.CASCADE)
    temporada = models.ForeignKey(Temporadas, on_delete=models.CASCADE)
    episodio = models.ForeignKey(Episodios, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.serie} {self.temporada} {self.episodio}'

class Continentes(models.Model):
    nome = models.CharField()
    def __str__(self):
        return self.nome


