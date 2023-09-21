from django.db import models

# Definindo o modelo disciplinaEntidade
class disciplinaEntidade(models.Model):
    # Campo para o nome da disciplina, com no máximo 100 caracteres e não nulo
    nome = models.CharField(max_length=100, null=False)
    
    # Campo para a descrição da disciplina, com no máximo 320 caracteres e não nulo
    descricao = models.CharField(max_length=320, null=False)

    # Método __str__ personalizado para representação de string legível
    def __str__(self):
        return "disciplinaEntidade [%s]" % self.nome
