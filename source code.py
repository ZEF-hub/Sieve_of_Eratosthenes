import json


def sieve(prime_number=2):
    if prime_number < nums[-1]:
        print(prime_number)
        for non_prime_number in range(2 * prime_number, input_num + 1, prime_number):
            if non_prime_number in nums:
                nums.remove(non_prime_number)
        return sieve(nums[nums.index(prime_number) + 1])


non_int = True
while non_int:
    try:
        input_num = int(input('Введите число до которого будем искать простые числа '))
        nums = [num for num in range(2, input_num + 1)]
        non_int = False
    except Exception as e:
        print('\nНу я же попросил число, ну что здесь непонятного? \n'
              'Даю тебе ещё попытку, постарайся попать по цифрам.\n')


if __name__ == '__main__':
    sieve()

    data = {}
    for num in nums:
        data['Prime number №' + str(len(data)+1)] = num

    with open('prime_numbers.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
