from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from controle_disciplina.models.alunoModelo import alunoEntidade
from controle_disciplina.serializers.alunoSerializer import alunoSerializer
from django.http import Http404

@api_view(['GET', 'PUT'])
def Alunoupdate(request, pk):
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

    elif request.method == 'PUT':
        # Se a requisição for PUT, atualiza o aluno com os dados fornecidos na requisição
        serializer = alunoSerializer(aluno_entidade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # Se os dados não forem válidos, retorna uma resposta de erro com status HTTP 400 (Bad Request)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
