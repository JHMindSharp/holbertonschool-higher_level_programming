# Python - Data Structures: Lists, Tuples

## Résumé

Ce projet se concentre sur les structures de données en Python, en particulier les listes et les tuples. Les tâches du projet couvrent divers aspects, tels que l'impression d'éléments d'une liste, l'accès sécurisé aux éléments, le remplacement d'éléments, etc.

## Détails du Projet

- **Auteur**: Guillaume
- **Poids**: 1
- **Suivi des Points**: Votre score sera mis à jour au fur et à mesure de votre progression dans les tâches.

## Ressources

Avant de commencer les tâches, assurez-vous de lire ou de regarder les ressources suivantes :

- [Python Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Data Structures (jusqu'à 5.3. Tuples et Séquences)](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Apprendre à Programmer 6 : Listes](https://docs.python.org/3/tutorial/introduction.html#lists)

## Objectifs d'Apprentissage

À la fin de ce projet, vous devriez être capable d'expliquer les concepts suivants sans l'aide de Google :

### Généralités

- Ce que sont les listes et comment les utiliser
- Les différences et similitudes entre les chaînes de caractères et les listes
- Les méthodes les plus courantes des listes et comment les utiliser
- Comment utiliser les listes comme des piles et des files d'attente
- Les compréhensions de liste et comment les utiliser
- Ce que sont les tuples et comment les utiliser
- Quand utiliser des tuples par rapport aux listes
- Ce qu'est une séquence
- L'emballage de tuples et le déballage de séquences
- L'instruction `del` et comment l'utiliser

## Exigences

### Scripts Python

- Éditeurs autorisés : vi, vim, emacs
- Tous vos fichiers seront interprétés/compilés sur Ubuntu 20.04 LTS en utilisant python3 (version 3.8.5)
- Tous vos fichiers doivent se terminer par une nouvelle ligne
- La première ligne de tous vos fichiers doit être exactement `#!/usr/bin/python3`
- Un fichier README.md, à la racine du dossier du projet, est obligatoire
- Votre code doit utiliser pycodestyle (version 2.7.*)
- Tous vos fichiers doivent être exécutables
- La longueur de vos fichiers sera testée à l'aide de `wc`

## Tâches

### 1. Imprimer une liste d'entiers
   - Écrire une fonction qui imprime tous les entiers d'une liste.
   - Prototype : `def print_list_integer(my_list=[]):`
   - Format : un entier par ligne. Voir exemple.
   - Vous n'êtes pas autorisé à importer de module.
   - Vous pouvez supposer que la liste ne contient que des entiers.
   - Vous n'êtes pas autorisé à convertir les entiers en chaînes de caractères.
   - Vous devez utiliser `str.format()` pour imprimer les entiers.

### 2. Accès sécurisé à un élément
   - Écrire une fonction qui récupère un élément d'une liste.
   - Prototype : `def element_at(my_list, idx):`
   - Si `idx` est négatif, la fonction doit renvoyer None.
   - Si `idx` est hors de portée (supérieur au nombre d'éléments dans `my_list`), la fonction doit renvoyer None.
   - Vous n'êtes pas autorisé à importer de module.
   - Vous n'êtes pas autorisé à utiliser try/except.

### 3. Remplacer un élément
   - Écrire une fonction qui remplace un élément d'une liste à une position spécifique.
   - Prototype : `def replace_in_list(my_list, idx, element):`
   - Si `idx` est négatif, la fonction ne doit rien modifier et renvoyer la liste d'origine.
   - Si `idx` est hors de portée (supérieur au nombre d'éléments dans `my_list`), la fonction ne doit rien modifier et renvoyer la liste d'origine.
   - Vous n'êtes pas autorisé à importer de module.
   - Vous n'êtes pas autorisé à utiliser try/except.

### 4. Imprimer une liste d'entiers en sens inverse
   - Écrire une fonction qui imprime tous les entiers d'une liste en sens inverse.
   - Prototype : `def print_reversed_list_integer(my_list=[]):`
   - Format : un entier par ligne en sens inverse. Voir exemple.
   - Vous n'êtes pas autorisé à importer de module.
   - Vous pouvez supposer que la liste ne contient que des entiers.
   - Vous n'êtes pas autorisé à convertir les entiers en chaînes de caractères.
   - Vous devez utiliser `str.format()` pour imprimer les entiers en sens inverse.

### 5. Remplacer dans une copie
   - Écrire une fonction qui remplace un élément d'une liste à une position spécifique sans modifier la liste d'origine.
   - Prototype : `def new_in_list(my_list, idx, element):`
   - Si `idx` est négatif, la fonction doit renvoyer une copie de la liste d'origine.
   - Si `idx` est hors de portée (supérieur au nombre d'éléments dans `my_list`), la fonction doit renvoyer une copie de la liste d'origine.
   - Vous n'êtes pas autorisé à importer de module.

### 6. Supprimer "c" et "C"
   - Écrire une fonction qui supprime tous les caractères "c" et "C" d'une chaîne de caractères.
   - Prototype : `def no_c(my_string):`
   - La fonction doit renvoyer la nouvelle chaîne de caractères.
   - Vous n'êtes pas autorisé à importer de module.
   - Vous n'êtes pas autorisé à utiliser `str.replace()`.

### 7. Matrice de listes
   - Écrire une fonction qui imprime une matrice d'entiers.
   - Prototype : `def print_matrix_integer(matrix=[[]]):`
   - Format : voir exemple.
   - Vous n'êtes pas autorisé à importer de module.
   - Vous pouvez supposer que la liste ne contient que des entiers.
   - Vous n'êtes pas autorisé à convertir les entiers en chaînes de caractères.
   - Vous devez utiliser `str.format()` pour imprimer les entiers.

### 8. Addition de Tuples
   -
