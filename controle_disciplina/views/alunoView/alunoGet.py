from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from controle_disciplina.models.alunoModelo import alunoEntidade
from controle_disciplina.serializers.alunoSerializer import alunoSerializer
from django.http import Http404

@api_view(['GET'])
def get_simplesAluno(request):
    if request.method == 'GET':
        # Recupera todos os objetos alunoEntidade do banco de dados
        aluno_entidades = alunoEntidade.objects.all()
        
        # Serializa a lista de alunos e retorna os dados
        serializer = alunoSerializer(aluno_entidades, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_objectAluno(request, pk):
    try:
        # Tenta encontrar um aluno pelo PK fornecido na URL
        aluno_entidade = alunoEntidade.objects.get(pk=pk)
    except alunoEntidade.DoesNotExist:
        # Se o aluno não for encontrado, retorna uma resposta de 404 (Não encontrado)
        raise Http404
    
    # Serializa o aluno encontrado e retorna seus dados
    serializer = alunoSerializer(aluno_entidade)
    return Response(serializer.data)
