from typing import List

def is_face_on_photo(photo: List[List[str]]) -> bool:
    for x in range(len(photo)):
        for y in range(len(photo[x])):
            if photo[x][y] == 'f': #Nalezeno F
                if y-1 >= 0:
                    if photo[x][y-1] == 'a' or photo[x][y-1] == 'c' or photo[x][y-1] == 'e': #Nalezeno 2. písmeno na lince y-1
                        if x+1 <= len(photo)-1:
                            if (photo[x+1][y] == 'a' or photo[x+1][y] == 'c' or photo[x+1][y] == 'e') and (photo[x+1][y] != photo[x][y-1]): #Nalezeno 3. písmeno které není zároveň písmeno 2.
                                if (photo[x+1][y-1] == 'a' or photo[x+1][y-1] == 'c' or photo[x+1][y-1] == 'e') and (photo[x+1][y-1] != photo[x][y-1] and photo[x+1][y-1] != photo[x+1][y]): #Nalezení 4. písmena které se neopakuje
                                    return True
                        if x-1 >= 0:
                            if (photo[x-1][y] == 'a' or photo[x-1][y] == 'c' or photo[x-1][y] == 'e') and (photo[x-1][y] != photo[x][y-1]): #3. písmeno
                                if(photo[x-1][y-1] == 'a' or photo[x-1][y-1] == 'c' or photo[x-1][y-1] == 'e') and (photo[x+1][y-1] != photo[x][y-1] and photo[x+1][y-1] != photo[x-1][y]): #4. Písmeno
                                    return True
                if y+1 <= (len(photo[x])-1):
                    if (photo[x][y+1] == 'a' or photo[x][y+1] == 'c' or photo[x][y+1] == 'e'): #Nalezení 2. písmene na lince y+1
                        if x+1 <= (len(photo)-1):
                            if (photo[x+1][y] == 'a' or photo[x+1][y] == 'c' or photo[x+1][y] == 'e') and (photo[x+1][y] != photo[x][y+1]): #3. písmeno
                                if (photo[x+1][y+1] == 'a' or photo[x+1][y+1] == 'c' or photo[x+1][y+1] == 'e') and (photo[x+1][y+1] != photo[x][y+1] and photo[x+1][y+1] != photo[x+1][y]): #4. písmeno
                                    return True
                        if x-1 >= 0:
                            if (photo[x-1][y] == 'a' or photo[x-1][y] == 'c' or photo[x-1][y] == 'e') and (photo[x-1][y] != photo[x][y+1]): #3. písmeno
                                if (photo[x-1][y+1] == 'a' or photo[x-1][y+1] == 'c' or photo[x-1][y+1] == 'e') and (photo[x-1][y+1] != photo[x][y+1] and photo[x-1][y+1] != photo[x-1][y]):
                                    return True
    return False
# Veřejné testy:
print(is_face_on_photo([['f', 'a'], ['c', 'e']]))  # True
print(is_face_on_photo([['f', 'a', 'c', 'e']]))  # False
print(is_face_on_photo([['e', 'c', 'x'], ['a', 'f', 'x'], ['x', 'x', 'x']]))  # True
print(is_face_on_photo([['f', 'f', 'x'], ['a', 'a', 'x'], ['x', 'x', 'x']]))  # False
