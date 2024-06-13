#esse programinha é para testar as possibilidades de pontuar x pontos de formas diferentes com "size" extra(s) touchdown(s) 
#ele não é usado para alcançar o objetivo em questão, serve apenas para explicar a função get_list(size) definida para fazer o exercicio
def extra_touchdown_c(size):
    #indice: a quantidade de pontos marcados, valor: o numero de quantidades de formas possiveis
    counter_scores = [0] * (size*2 + 1)
    def recursive_score(scored):
        if len(scored) == size:
            #adiciona uma possibilidade de fazer x pontos (sum(scored))
            counter_scores[sum(scored)] += 1
            
            #print para visualizar as combinaçoes de possibilidades de pontos feitos com extra touch downs
            #print(" - ".join(map(str, scored)))
        else:
            #O score do momento pode variar de [0-2] caso seja o primeiro score, se não ele pode variar de [0 - ultimo score]
            #isso fara com todas as possibilidades de pontuaçoes de extra touch downs sejam anotadas ignorando a ordem 
            #ex: (3 touchdowns) 2 - 0 - 1 == 1 - 2 - 0 == 1 - 0 - 2; essas diferenças de ordens não existem seguindo a regra da função recursiva
            for i in range(scored[-1] + 1 if scored else 3):
                recursive_score(scored + [i])

    recursive_score([])        
    for i in range(len(counter_scores)):
        #começando de [0 até size * 2]
        print(f"{counter_scores[i]} | ", end="")
    print(f"size = {size}")
    
# extra_touchdown_c(0)
# extra_touchdown_c(1)
# extra_touchdown_c(2)
# extra_touchdown_c(3)
# extra_touchdown_c(4)
# extra_touchdown_c(5)
# extra_touchdown_c(6)
# extra_touchdown_c(7)
# extra_touchdown_c(8)
# extra_touchdown_c(9)
# extra_touchdown_c(10)
# extra_touchdown_c(11)
# extra_touchdown_c(12)
# extra_touchdown_c(13)
# extra_touchdown_c(14)
# ...
# extra_touchdown_c(32)

#foi observado um certo padrão ao plotar a lista de possibilidades de pontuar i pontos (indice da lista counter_scores [ 0 - n ]) de n formas diferentes.
#com essa observação, eu montei a função que simplismente respeita esse padrao e economiza nos calculos, a função get_list() que está def no main.py