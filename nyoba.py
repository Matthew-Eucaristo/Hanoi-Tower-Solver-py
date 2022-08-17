# Solving Hanoi Tower with my algorithm
import string

def main():
    alphabet = string.ascii_letters
    
    # input n of poles and block
    n: int = int(input('Input number of poles and block: '))

    # get fixed number of tower and poles
    # in this state poles are represented by ABC and blocks are respresented by 123
    poles: tuple = tuple(alphabet[0:n])
    blocks: tuple = tuple(range(1, n+1))

    answer = hanoi_algorithm(poles, blocks)

def hanoi_algorithm(poles: tuple, blocks: tuple):
    results = [] # container for the answers

    # move all blocks in order from biggest (block 1) to smallest (block n)
    for i in range(n, 0, -1):
        
        
    

if __name__ == '__main__':
    main()
