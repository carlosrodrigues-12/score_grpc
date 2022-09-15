# score_grpc

Passos para execução:

$:> cd python

2) Editar o arquivo "const.py" como no exemplo a seguir |CHAT_SERVER_HOST = "172.17.0.2:50051"|. Altere o endereço dos players também.

3) Executar o seguinte para gerar os protótipos

$:> python3 -m grpc_tools.protoc -I../protos --python_out=. --grpc_python_out=. ../protos/score.proto

4) Executar Server gRPC

$:> python3 score.py

5) Executar os jogadores, um exemplo para seguir abaixo.

$:> python3 client.py player1