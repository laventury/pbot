# PBot - Rotina Modular de Processamento de Tarefas

Os Módulos de Tarefas devem ser escritos em linguagem python e dispostos no diretório raiz do projeto seguindo o padrão taskXXXX.py, onde o XXXX refere-se ao ID númerico e sequêncial da tarefa.

A rotina principal carrega os módulo dinamicamente e executa a tarefa caso a condicionante seja atendida. A biblioteca original utilizará condicionantes de tempo (à implementar), adicionalmente cada modulo poderá adotar suas próprias condicionantes.

