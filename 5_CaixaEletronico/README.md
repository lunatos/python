# CaixaEletronico
    Esta API simula o funcionamento de um caixa eletrônico. Ela recebe um valor de saque desejado e retorna a quantidade de cédulas de cada valor necessárias para compor esse saque, utilizando a menor quantidade de cédulas possível. As cédulas consideradas são: 100, 50, 20, 10, 5 e 2.

# Como rodar
    1.Abra o terminal no diretorio do projeto e ative o virtual env, no windows utilize: "myvenv\Scripts\activate", no linux "source myvenv/bin/activate"

    2.Com o terminal aberto no diretorio rode o seguinte comando para rodar o servidor "uvicorn main:app --host 0.0.0.0 --port 8000"

    3.Com outro terminal aberto no diretorio e com o myvenv ativado rode o script com o seguinte comando "python test_api.py"