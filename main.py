
def palindrome_check(string_value):
    # slice the input to reverse the string
    if string_value == string_value[::-1]:
        return True
    return False


run = True
while (run):
    string_value = input("Enter a string or 'exit':")

    # Using exit to quit the program
    if string_value == "exit":
        run = False
        break

    # convert the string to all lower case
    string_value = string_value.lower()

    # remove all spaces and punctuation from the string
    new_string_value = ""
    for value in string_value:
        if value.isalnum():
            new_string_value += value

    print("Palindrome Check:", palindrome_check(new_string_value))
