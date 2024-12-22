import random

def gen_random(num_count, begin, end):
    numbers = [random.randint(begin, end) for _ in range(num_count)]
    return numbers

def main():
    print(gen_random(5, 1, 3))

if __name__ == '__main__':
    main()