from django.db import models

# Definindo o modelo alunoEntidade
class alunoEntidade(models.Model):
    # Campo para o nome do aluno, com no máximo 100 caracteres e não nulo
    nome = models.CharField(max_length=100, null=False)
    
    # Campo para o email do aluno, com no máximo 150 caracteres e não nulo
    email = models.CharField(max_length=150, null=False)

    # Método __str__ personalizado para representação de string legível
    def __str__(self):
        return "alunoEntidade [%s]" % self.nome
