import strawberry
from strawberry.asgi import GraphQL
  
TD_POINTS = 6
FG_POINTS = 3

#REGRAS DE NEGOCIO
def get_list(size: int) -> list[int]:
    '''
    Parameter: 
    size (int): Quantidade de extra touchdowns que o time pode ter marcado
    
    Return:
    list[int]: Uma lista onde o indice é a quantidade de pontos marcados e o valor é o numero de formas distintas de marcar i pontos (ignorando a ordem)
    '''
    #a explicação do algoritmo dessa função se encontra no arquivo etd_combinations.py
    result = []
    num = 1
    equal = False
    for i in range(size):
        result.append(num)
        if equal:
            num += 1
        equal = not equal      
    if size % 2 == 0 :
        result.append(int(size / 2 + 1))
        num -= 1
    else:
        result.append(int((size+1) / 2))       
    for i in range(size):
        result.append(num)
        if equal:
            num -= 1
        equal = not equal    
    return result
  
def calculate_touchdown_combinations(score: int, remainder: int) -> int:
    #Resto 0 ja acrescenta uma possibilidade de fazer apenas field_goals (ou se o score for 0 também só tem uma possibilidade de marcar 0 pts)
    result = 1 if remainder == 0 else 0
    touchdowns = 0
      
    while touchdowns * TD_POINTS <= score:
        touchdowns += 1
        extra_points = get_list(touchdowns)
        for i in range(len(extra_points)):
            #so pegamos as pos que vao fechar a soma de pontos ou que sera possivel fechar essa soma adicionando field_goals
            if i % FG_POINTS == remainder:
                #testa se o valor do total pode ser menor ou igual do que o score (se for igual não terão field_goals para o caso)
                if i + touchdowns * TD_POINTS <= score:
                    #o numero de possibilidades de se marcar i pontos com x_touchdowns é o valor que está guardado na lista num_extra_td
                    result += 1 * extra_points[i]
    return result                
  
def score_combination(score: int) -> int:
    remainder_score_divided_to_field_goal = {0: 0, 1: 1, 2: 2}
    remainder = score % FG_POINTS
    return calculate_touchdown_combinations(score, remainder_score_divided_to_field_goal[remainder])      

#MODELOS         
@strawberry.type
class VerifyResolver:
    score: str
    
    @strawberry.field
    def combinations(self) -> int:
        parts = self.score.split('x')
        score_a, score_b = int(parts[0]), int(parts[1])
        
        #primeiro descobrimos a combinação do placar de cada time separado
        num_scores_a = score_combination(score_a)
        num_scores_b = score_combination(score_b)
        
        return num_scores_a * num_scores_b

@strawberry.type
class Mutation:
    @strawberry.mutation
    def verify(self, score: str) -> VerifyResolver:
        return VerifyResolver(score=score)

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello, World!"  

schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQL(schema)