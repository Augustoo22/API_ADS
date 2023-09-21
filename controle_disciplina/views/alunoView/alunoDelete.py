from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from controle_disciplina.models.alunoModelo import alunoEntidade
from controle_disciplina.serializers.alunoSerializer import alunoSerializer
from django.http import Http404

@api_view(['GET', 'DELETE'])
def Alunodelete(request, pk):
    try:
        # Tenta buscar um aluno pelo PK fornecido na URL
        aluno_entidade = alunoEntidade.objects.get(pk=pk)
    except alunoEntidade.DoesNotExist:
        # Se o aluno não for encontrado, retorna uma resposta de 404 (Não encontrado)
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Se a requisição for GET, serializa o aluno encontrado e retorna seus dados
        serializer = alunoSerializer(aluno_entidade)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        # Se a requisição for DELETE, exclui o aluno encontrado e retorna uma resposta de sucesso
        aluno_entidade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
