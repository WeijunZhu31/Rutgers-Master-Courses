def main(array, x):
    if len(array) == 1:
        return array[0]
    else:
        output = array[0] + x * main(array[1:], x)
        return output


print(main([9, 7, 5, 3, 1], x=2))
