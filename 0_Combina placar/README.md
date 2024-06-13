# FUNÇÃO DO PROGRAMA
 O programa tem como objetivo resolver o seguinte problema:
 Dado um resultado de placar de jogo de futebol americano, precisa-se calcular o maior número
 de combinações de pontuações possíveis para o resultado daquela partida. A ordem das pontuações
 não importa, apenas os tipos de pontuações diferentes de cada time. Os pontos podem ser marcados
 da seguinte forma:
 - Touchdown: 6 pontos
 - Extra touchdown: 0, 1 ou 2 pontos (só pode ser marcado após um touchdown)
 - Field goal: 3 pontos

# COMO O PROGRAMA DEVE SER EXECUTADO:
 1-abra o terminal no diretório que está o Dockerfile
 2-digite o comando "docker build -t score:latest ." para criar a imagem
 3-digite o comando "docker container run --name score -p 8080:8080 score:latest"
 4-em outro terminal navegue para o diretório /src
 5-digite o comando "python test_api.py" para testar o programa, em alguns computadores o comando tem que ser "python3 test_api.py"
 6-para modificar os testes modifique a variavel 'test_scores' no arquivo de testes