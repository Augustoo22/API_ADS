from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from controle_disciplina.models.disciplinaModelo import disciplinaEntidade
from controle_disciplina.serializers.disciplinaSerializer import disciplinaSerializer
from django.http import Http404

@api_view(['GET', 'DELETE'])
def Disciplinadelete(request, pk):
    try:
        # Tenta buscar uma disciplina pelo PK fornecido na URL
        disciplina_entidade = disciplinaEntidade.objects.get(pk=pk)
    except disciplinaEntidade.DoesNotExist:
        # Se a disciplina não for encontrada, retorna uma resposta de 404 (Não encontrado)
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Se a requisição for GET, serializa a disciplina encontrada e retorna seus dados
        serializer = disciplinaSerializer(disciplina_entidade)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        # Se a requisição for DELETE, exclui a disciplina encontrada e retorna uma resposta de sucesso
        disciplina_entidade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
