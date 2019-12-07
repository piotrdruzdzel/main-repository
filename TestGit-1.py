print("Start\n")

def generate_numbers(numbers):
        for number in numbers:
                yield number*number

numbers = [1, 2, 3, 4, 5]
new_numbers = [6, 7, 8, 9, 10]
new_new_numbers = [11, 12, 13, 14, 15]

generator_1 = generate_numbers(numbers)
generator_2 = (n*n for n in new_numbers) #with () it's a generator, with [] it's a list
generator_3 = generate_numbers(new_new_numbers)

for number in generator_1:
        print(number)

print(f"Generator 2: {type(generator_2)}")

print("Printowanie1")

print("\nKoniec")

