from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from controle_disciplina.models.tarefaModelo import tarefaEntidade
from controle_disciplina.serializers.tarefaSerializer import tarefaSerializer
from django.http import Http404

@api_view(['GET'])
def get_simplesTarefa(request):
    if request.method == 'GET':
        # Recupera todas as tarefas no banco de dados
        tarefa_entidades = tarefaEntidade.objects.all()
        
        # Serializa a lista de tarefas
        serializer = tarefaSerializer(tarefa_entidades, many=True)
        
        return Response(serializer.data)

@api_view(['GET'])
def get_objectTarefa(request, pk):
    try:
        # Tenta encontrar uma tarefa pelo PK fornecido na URL
        tarefa_entidade = tarefaEntidade.objects.get(pk=pk)
    except tarefaEntidade.DoesNotExist:
        # Se a tarefa não for encontrada, retorna uma resposta de 404 (Não encontrado)
        raise Http404
    
    # Serializa a tarefa encontrada e retorna seus dados
    serializer = tarefaSerializer(tarefa_entidade)
    return Response(serializer.data)
