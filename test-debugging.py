def add(a, b):
    # This function adds two numbers.
    return a + b

def multiply(a, b):
    # This function multiplies two numbers.
    return a * b

def compute_complex_operation(x, y):
    # Compute an intermediate sum.
    intermediate = add(x, y)
    
    # Use conditional branching to choose a further operation.
    if intermediate % 2 == 0:
        # Multiply if the sum is even.
        result = multiply(intermediate, intermediate)
    else:
        # Otherwise, add the sum to itself.
        result = add(intermediate, intermediate)
    
    return result

def process_numbers(numbers):
    # Process each number in the list.
    processed = []
    for num in numbers:
        # Step into this function to see iteration.
        if num % 2 == 0:
            processed_value = multiply(num, 2)
        else:
            processed_value = add(num, 3)
        processed.append(processed_value)
    return processed

def main():
    x = 5
    y = 7
    # Test breakpoint here to observe initial values.
    result_add = add(x, y)
    
    # Compute a complex operation to step into functions.
    result_complex = compute_complex_operation(x, y)
    
    # Process a list of numbers to see loop iteration
    num_list = [1, 2, 3, 4, 5]
    processed_list = process_numbers(num_list)
    
    print("Result of add({},{}) = {}".format(x, y, result_add))
    print("Result of complex operation on ({},{}) = {}".format(x, y, result_complex))
    print("Processed list:", processed_list)

if __name__ == '__main__':
    main()