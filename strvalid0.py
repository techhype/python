if __name__ == '__main__':
    s = input()
#check each char in string
    #whether it conatins alphanumeric characters
    print(any(c.isalnum() for c in s))
    #whether it conatins alphabet characters
    print(any(c.isalpha() for c in s))
    #whether it conatins digits
    print(any(c.isdigit() for c in s))
    #whether it conatins  lowercase characters
    print(any(c.islower() for c in s))
    #whether it conatins uppercase characters
    print(any(c.isupper() for c in s))
