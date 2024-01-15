def print_buzz(num):
    if num % 5 == 0:
        return "buzz"
          
def print_fizzbuzz(num):
    if num % 15 == 0:
        print("fizzbuzz")
        
        
if __name__ == '__main__':
    for i in range(1,21):
        if i % 15 == 0:
            print(print_fizzbuzz(i))
        elif i % 5 == 0:
            print(print_buzz(i))
