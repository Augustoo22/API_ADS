from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from controle_disciplina.models.tarefaModelo import tarefaEntidade
from controle_disciplina.serializers.tarefaSerializer import tarefaSerializer

class ListarTarefasAlunoView(APIView):
    """
    View para listar todas as tarefas de um aluno.

    Esta view permite listar todas as tarefas associadas a um aluno específico.
    Você pode acessar esta view fornecendo o ID do aluno na URL.

    Exemplo de uso:
    1. Faça uma requisição GET para /api/listar_tarefas_aluno/<aluno_id>/
    2. Substitua <aluno_id> pelo ID do aluno desejado.

    Parâmetros da URL:
    - aluno_id: O ID do aluno para o qual você deseja listar as tarefas.

    Resposta:
    - Status 200 OK: Retorna a lista de tarefas do aluno.
    - Status 404 Not Found: Se o aluno não existe ou não possui tarefas.

    Exemplo de resposta (JSON):
    ```
    [
        {
            "id": 1,
            "titulo": "Tarefa 1",
            "descricao": "Descrição da Tarefa 1",
            "aluno": 1
        },
        {
            "id": 2,
            "titulo": "Tarefa 2",
            "descricao": "Descrição da Tarefa 2",
            "aluno": 1
        }
    ]
    ```

    """
    def get(self, request, aluno_id, format=None):
        try:
            tarefas = tarefaEntidade.objects.filter(aluno_id=aluno_id)
            serializer = tarefaSerializer(tarefas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except tarefaEntidade.DoesNotExist:
            return Response({"detail": "Nenhuma tarefa encontrada para este aluno."}, status=status.HTTP_404_NOT_FOUND)
