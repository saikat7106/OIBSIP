import random
import string

def generate_password(length):

    list_of_chars = string.ascii_letters + string.digits + "!@#$%^&*"

    selected_char = random.sample(list_of_chars,length)
    pass_str = "".join(selected_char)

    return pass_str

if__name__="__main__"

len = int(input("enter the length of the password: "))
pass_str = generate_password(len)

print("a randomly generated password is: ",pass_str) 