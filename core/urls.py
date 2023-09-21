from django.urls import path
from controle_disciplina.views.alunoView.alunoGet import get_simplesAluno, get_objectAluno
from controle_disciplina.views.alunoView.alunoPost import addAluno
from controle_disciplina.views.alunoView.alunoPut import Alunoupdate
from controle_disciplina.views.alunoView.alunoDelete import Alunodelete
from controle_disciplina.views.disciplinaView.disciplinaGet import get_simplesDisciplina, get_objectDisciplina
from controle_disciplina.views.disciplinaView.disciplinaPost import addDisciplina
from controle_disciplina.views.disciplinaView.disciplinaPut import Disciplinaupdate
from controle_disciplina.views.disciplinaView.disciplinaDelete import Disciplinadelete
from controle_disciplina.views.tarefaView.tarefaGet import get_simplesTarefa, get_objectTarefa
from controle_disciplina.views.tarefaView.tarefaPost import addtarefa
from controle_disciplina.views.tarefaView.tarefaPut import tarefaupdate
from controle_disciplina.views.tarefaView.tarefaDelete import Tarefadelete
from controle_disciplina.views.tarefaView.tarefaAluo import listar_tarefas_aluno

urlpatterns = [
    # Alunos
    path('alunosGet/', get_simplesAluno, name='get_alunos'),
    path('alunosGetId/<int:pk>/', get_objectAluno, name='get_aluno_by_id'),
    path('alunosAdd/', addAluno, name='add_aluno'),
    path('alunosUpdate/<int:pk>/', Alunoupdate, name='update_aluno'),
    path('alunosDelete/<int:pk>/', Alunodelete, name='delete_aluno'),

    # Disciplinas
    path('disciplinaGet/', get_simplesDisciplina, name='get_disciplinas'),
    path('disciplinaGetId/<int:pk>/', get_objectDisciplina, name='get_disciplina_by_id'),
    path('disciplinaAdd/', addDisciplina, name='add_disciplina'),
    path('disciplinaUpdate/<int:pk>/', Disciplinaupdate, name='update_disciplina'),
    path('disciplinaDelete/<int:pk>/', Disciplinadelete, name='delete_disciplina'),

    # Tarefas
    path('tarefaGet/', get_simplesTarefa, name='get_tarefas'),
    path('tarefaGetId/<int:pk>/', get_objectTarefa, name='get_tarefa_by_id'),
    path('tarefaAdd/', addtarefa, name='add_tarefa'),
    path('tarefaUpdate/<int:pk>/', tarefaupdate, name='update_tarefa'),
    path('tarefaDelete/<int:pk>/', Tarefadelete, name='delete_tarefa'),

    # Tarefas de um Aluno
    path('tarefaListAluno/<int:pk>/tarefas/', listar_tarefas_aluno, name='listar_tarefas_aluno'),
]
