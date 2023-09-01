def simple():
    for i in range(19):
        if i % 2 == 0:  # Check if i is even
            yield i

# Call the generator function and print the yielded values
for num in simple():
    print(num)
