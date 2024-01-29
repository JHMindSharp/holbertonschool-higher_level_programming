def delete_at(my_list=[], idx=0):
    # Vérifier si l'indice est valide (ni négatif ni en dehors des limites)
    if idx < 0 or idx >= len(my_list):
        return my_list  # Renvoyer la liste inchangée si l'indice est invalide

    # Créer une nouvelle liste sans l'élément à l'indice idx
    new_list = my_list[:idx] + my_list[idx + 1:]

    return new_list  # Renvoyer la nouvelle liste sans l'élément supprimé
