from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from controle_disciplina.models.disciplinaModelo import disciplinaEntidade
from controle_disciplina.serializers.disciplinaSerializer import disciplinaSerializer
from django.http import Http404

@api_view(['GET'])
def get_simplesDisciplina(request):
    if request.method == 'GET':
        # Recupera todos os objetos disciplinaEntidade do banco de dados
        disciplina_entidades = disciplinaEntidade.objects.all()
        
        # Serializa a lista de disciplinas e retorna os dados
        serializer = disciplinaSerializer(disciplina_entidades, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_objectDisciplina(request, pk):
    try:
        # Tenta encontrar uma disciplina pelo PK fornecido na URL
        disciplina_entidade = disciplinaEntidade.objects.get(pk=pk)
    except disciplinaEntidade.DoesNotExist:
        # Se a disciplina não for encontrada, retorna uma resposta de 404 (Não encontrado)
        raise Http404
    
    # Serializa a disciplina encontrada e retorna seus dados
    serializer = disciplinaSerializer(disciplina_entidade)
    return Response(serializer.data)
