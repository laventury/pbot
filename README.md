# PBot - Sistema Modular de Processamento de Tarefas

Os Módulos de Tarefas são compostos por arquivos python inseridos no diretório raiz do projeto. Tais módulos devem ser nomeados atendendo o padrão taskXXXX.py, onde o XXXX refere-se ao ID númerico e sequêncial da tarefa.

A rotina principal pbot.py se encarrega de verificar a existência do módulos, carrega-los dinamicamente e executar a função execute().
