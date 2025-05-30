from django.db import models

class Job(models.Model):

    firm = models.CharField(max_length=80, 
                            blank=False, 
                            null=False, 
                            unique=True,
                            verbose_name= "Empresa")
    
    name = models.CharField(max_length=255,
                            blank=False,
                            null= False,
                            verbose_name= "Vaga")
    
    salary = models.FloatField(max_length=80,
                               blank= False,
                               null= False,
                               verbose_name= "Salário")
    
    is_home = models.BooleanField (blank= False,
                                   null= False,
                                   verbose_name= "É home office?")
    
    date_applied = models.DateField(auto_created= True, 
                                    auto_now_add=True,
                                    verbose_name= "Data do Envio do Currículo")
    
    date_response = models.DateField(auto_created= False,
                                     blank=True,
                                     null=True,
                                     verbose_name= "Data resposta")
    
    offer = models.TextField(max_length=400,
                             blank= True,
                             null= True,
                             verbose_name= "Oferta/Resposta da empresa")
    
    def __str__(self) -> str:
        return self.firm