result = []
input_string = input("Input original word: ")
shift = int(input("Input a number to shift by: "))
result = list(input_string)
results=[]
newList = []
for a in result:
    a = a.lower()
    results.append(a)
for y in results:
    if y == ' ':  # Check if the character is a space
        newList.append(' ')  # Append the space as is
    elif 'a' <= y <= 'z':  # Handle lowercase letters
        x = ord(y) - ord('a')  # Normalize to 0-25
        x = (x + shift) % 26  # Apply shift and wrap around
        z = chr(x + ord('a'))  # Convert back to ASCII
        newList.append(z)
    else:
        # Append other characters (like numbers or punctuation) unchanged
        newList.append(y)

word = ''.join(newList)
print(word)
