from rest_framework import serializers
from controle_disciplina.models.tarefaModelo import tarefaEntidade

class TarefaAlunoSerializer(serializers.ModelSerializer):
    """
    Serializer para serializar tarefas de alunos.

    Este serializer serializa objetos tarefaEntidade e inclui os seguintes campos:
    - id: O ID único da tarefa.
    - titulo: O título da tarefa.
    - descricao: A descrição da tarefa.
    - aluno: O ID do aluno associado à tarefa.

    Exemplo de uso em uma view:

    ```python
    class MinhaView(APIView):
        def get(self, request, *args, **kwargs):
            tarefa = tarefaEntidade.objects.get(pk=1)
            serializer = TarefaAlunoSerializer(tarefa)
            return Response(serializer.data)
    ```
    """

    class Meta:
        model = tarefaEntidade
        fields = ['id', 'titulo', 'descricao', 'aluno']
