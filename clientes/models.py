from django.db import models

class Departamento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.nome)

class CPF(models.Model):
    numero = models.CharField(max_length=12)
    data_exp = models.DateField(auto_now=False)

    def __str__(self):
        return "{}".format(self.numero)


class Empregado(models.Model):
    nome     = models.CharField(max_length=50, blank=False, null=False)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    salario  = models.DecimalField(max_digits=10, decimal_places=2)
    idade    = models.IntegerField()
    email    = models.EmailField(max_length=254)
    cpf      = models.OneToOneField(CPF, blank=True, null=True, on_delete=models.DO_NOTHING, unique=True)
    departamentos = models.ManyToManyField(Departamento, blank=True)
    foto = models.ImageField(upload_to="empregados_fotos")

    def __str__(self):
        return "{} {}".format(self.nome, self.email)

class Telefone(models.Model):
    numero   = models.CharField(max_length=20, blank=False, null=False)
    descricao = models.CharField(max_length=80, blank=True, null=False)
    empregado = models.ForeignKey(Empregado, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "{} - {}".format(self.numero, self.descricao)



