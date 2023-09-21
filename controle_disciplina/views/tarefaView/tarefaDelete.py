from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from controle_disciplina.models.tarefaModelo import tarefaEntidade
from controle_disciplina.serializers.tarefaSerializer import tarefaSerializer
from django.http import Http404

@api_view(['GET', 'DELETE'])
def Tarefadelete(request, pk):
    try:
        # Tenta buscar uma tarefa pelo PK fornecido na URL
        tarefa_entidade = tarefaEntidade.objects.get(pk=pk)
    except tarefaEntidade.DoesNotExist:
        # Se a tarefa não for encontrada, retorna uma resposta de 404 (Não encontrado)
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Se a requisição for GET, serializa a tarefa encontrada e retorna seus dados
        serializer = tarefaSerializer(tarefa_entidade)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        # Se a requisição for DELETE, exclui a tarefa encontrada e retorna uma resposta de sucesso
        tarefa_entidade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
