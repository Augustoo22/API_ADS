from rest_framework import serializers
from controle_disciplina.models.disciplinaModelo import disciplinaEntidade

# Definindo o serializador disciplinaSerializer
class disciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        # Especifica o modelo que o serializador deve usar
        model = disciplinaEntidade
        
        # Define os campos que devem ser incluídos na representação JSON
        fields = '__all__'
