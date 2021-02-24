from django.db import models



class Usuario(models.Model): 
    nome = models.CharField(max_length = 200) 
    sobrenome = models.CharField(max_length = 200) 
    cpf = models.IntegerField() 
    rg = models.IntegerField() 
    last_modified = models.DateTimeField(auto_now_add = True) 
    endereco = models.CharField(max_length = 200) 
    bairro = models.CharField(max_length = 200) 
    cidade = models.CharField(max_length = 200) 
    estado = models.CharField(max_length = 200) 
    cep = models.CharField(max_length = 200) 
    numero = models.CharField(max_length = 200) 
    complemento = models.CharField(max_length = 200) 

    def __str__(self): 
        return self.nome


class Dividas(models.Model): 
    
    STATUS = [
    ('A', 'Ativa'),
    ('I', 'Inativa'),
    ]

    nome = models.CharField(max_length = 200) 
    data = models.DateField()
    valor = models.FloatField()
    status = models.CharField(
        max_length=2,
        choices= STATUS,
    )
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return (self.nome)

