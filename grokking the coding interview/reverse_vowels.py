#Given a string s, reverse only all the vowels in the string and return it.

#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

def sol(s):
    vowels = 'AEIOUaeiou'
    lst = list(s)
    
    front_ptr = 0
    back_ptr = len(lst) - 1

    while front_ptr<back_ptr:
        if lst[front_ptr] in vowels and lst[back_ptr] in vowels:
            lst[front_ptr], lst[back_ptr] = lst[back_ptr], lst[front_ptr]
            front_ptr += 1
            back_ptr -= 1
        elif lst[back_ptr] in vowels:
            front_ptr+=1
        elif lst[front_ptr] in vowels:
            back_ptr-=1
        else:
            front_ptr+=1
            back_ptr-=1
    
    return ''.join(lst)
    
print(sol('hello'))
print(sol('aeiou'))
    