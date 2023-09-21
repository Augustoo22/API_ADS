from rest_framework import serializers
from controle_disciplina.models.alunoModelo import alunoEntidade

# Definindo o serializador alunoSerializer
class alunoSerializer(serializers.ModelSerializer):
    class Meta:
        # Especifica o modelo que o serializador deve usar
        model = alunoEntidade
        
        # Define os campos que devem ser incluídos na representação JSON
        fields = '__all__'
