def print_buzz():
    for i in range(1, 21):
        if i % 5 == 0:
            return "buzz"

if __name__ == '__main__':
    print(print_buzz())