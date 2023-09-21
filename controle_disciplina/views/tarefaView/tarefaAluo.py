from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from controle_disciplina.models.alunoModelo import alunoEntidade
from controle_disciplina.models.tarefaModelo import tarefaEntidade
from controle_disciplina.serializers.tarefaSerializer import tarefaSerializer

@api_view(['GET'])
def listar_tarefas_aluno(request, aluno_id):
    # Verificar se o aluno existe ou retornar 404 caso não exista
    aluno = get_object_or_404(alunoEntidade, pk=aluno_id)
    
    # Filtrar as tarefas associadas a esse aluno
    tarefas = tarefaEntidade.objects.filter(aluno=aluno)
    
    # Serializar as tarefas
    serializer = tarefaSerializer(tarefas, many=True)
    
    return Response(serializer.data)
