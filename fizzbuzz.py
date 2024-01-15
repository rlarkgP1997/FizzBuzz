def print_fizz(num):
		if i % 3 == 0:
		    print('fizz')

def print_buzz(num):
    if num % 5 == 0:
        print('buzz')
          
def print_fizzbuzz(num):
    if num % 15 == 0:
        print("fizzbuzz")
        
        
if __name__ == '__main__':
    for i in range(1,21):
        if i % 15 == 0:
            print(print_fizzbuzz(i))
        elif i % 3 == 0:
            print(print_fizz(i))
        elif i % 5 == 0:
            print(print_buzz(i))
