from django.db import models
from controle_disciplina.models.alunoModelo import alunoEntidade
from controle_disciplina.models.disciplinaModelo import disciplinaEntidade

# Definindo o modelo tarefaEntidade
class tarefaEntidade(models.Model):
    # Campo para o título da tarefa, com no máximo 100 caracteres e não nulo
    titulo = models.CharField(max_length=100, null=False)
    
    # Campo para a descrição da tarefa, com no máximo 320 caracteres e não nulo
    descricao = models.CharField(max_length=320, null=False)
    
    # Campo para a data de entrega da tarefa, não nulo
    data_entrega = models.DateField(null=False)
    
    # Relacionamento com o modelo alunoEntidade usando uma chave estrangeira (ForeignKey)
    aluno = models.ForeignKey(alunoEntidade, on_delete=models.CASCADE)
    
    # Relacionamento com o modelo disciplinaEntidade usando uma relação ManyToMany
    disciplina = models.ManyToManyField(disciplinaEntidade)

    # Método __str__ personalizado para representação de string legível
    def __str__(self):
        return "tarefaEntidade [%s]" % self.titulo
