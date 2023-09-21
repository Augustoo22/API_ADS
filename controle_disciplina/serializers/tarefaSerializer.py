from rest_framework import serializers
from controle_disciplina.models.tarefaModelo import tarefaEntidade

# Definindo o serializador tarefaSerializer
class tarefaSerializer(serializers.ModelSerializer):
    class Meta:
        # Especifica o modelo que o serializador deve usar
        model = tarefaEntidade
        
        # Define os campos que devem ser incluídos na representação JSON
        fields = '__all__'
