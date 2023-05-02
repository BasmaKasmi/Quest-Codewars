#La fonction vérifie d'abord si le tableau a 0 ou 1 élément, auquel cas il est considéré comme déjà trié dans l'ordre croissant.
#Sinon, elle parcourt le tableau et vérifie si chaque élément est inférieur ou égal à l'élément suivant.

#Si elle trouve une paire d'éléments adjacents où l'élément de gauche est supérieur à l'élément de droite, elle renvoie False.

#Si elle parcourt l'intégralité du tableau sans trouver une telle paire, elle renvoie True.


def in_asc_order(arr):
    # Check if the array has 0 or 1 elements
    if len(arr) < 2:
        return True
    
    # Check if the array is in ascending order
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    
    # If we make it through the loop without returning False, the array is in ascending order
    return True




print(in_asc_order([1,2,4,7,19]))
print(in_asc_order([1,2,3,4,5]))
print(in_asc_order([1,6,10,18,2,4,20]))
print(in_asc_order([9,8,7,6,5,4,3,2,1]))
