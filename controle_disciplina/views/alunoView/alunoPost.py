from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from controle_disciplina.models.alunoModelo import alunoEntidade
from controle_disciplina.serializers.alunoSerializer import alunoSerializer

@api_view(['POST'])
def addAluno(request):
    if request.method == 'POST':
        # Cria um serializador com os dados fornecidos na requisição
        serializer = alunoSerializer(data=request.data)
        
        # Verifica se os dados fornecidos são válidos de acordo com o serializador
        if serializer.is_valid():
            # Salva o novo objeto aluno no banco de dados
            serializer.save()
            
            # Retorna uma resposta de sucesso com status HTTP 201 (Criado)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Se os dados não forem válidos, retorna uma resposta de erro com status HTTP 400 (Bad Request)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
