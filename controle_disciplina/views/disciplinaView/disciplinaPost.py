from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from controle_disciplina.models.disciplinaModelo import disciplinaEntidade
from controle_disciplina.serializers.disciplinaSerializer import disciplinaSerializer

@api_view(['POST'])
def addDisciplina(request):
    if request.method == 'POST':
        # Cria um serializador com os dados fornecidos na requisição
        serializer = disciplinaSerializer(data=request.data)
        
        # Verifica se os dados fornecidos são válidos de acordo com o serializador
        if serializer.is_valid():
            # Salva o novo objeto disciplina no banco de dados
            serializer.save()
            
            # Retorna uma resposta de sucesso com status HTTP 201 (Criado)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Se os dados não forem válidos, retorna uma resposta de erro com status HTTP 400 (Bad Request)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
