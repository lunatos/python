def manipula_lista(list_of_numbers):
    
    if not all(isinstance(num, (int, float)) for num in list_of_numbers):
        raise TypeError("Todos os elementos da lista devem ser numeros")
    
    new_list = []

    for num in list_of_numbers:
        if num % 2 == 0:
            new_list.append(num * 2)

    return new_list
