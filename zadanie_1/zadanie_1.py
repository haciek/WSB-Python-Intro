import random

def main():
    list_1 = [random.randint(0,10) for _ in range(0,10)]
    list_2 = [random.randint(10,20) for _ in range(0,10)]
    zipped = zip(list_1, list_2) 

    print(f'List #1: {list_1}')
    print(f'List #2: {list_2}')
    try:
        sum = 0;
        for (x1, x2) in zipped:
            sum += x2 / x1
        print(f'Sum: {sum}')
    except ZeroDivisionError:
        print(f'Error while dividing {x2} by {x1}')


if __name__ == "__main__":
    main()


