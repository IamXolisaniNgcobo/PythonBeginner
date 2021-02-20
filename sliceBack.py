          #012345678901234567890123456
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1]    #zyxwvutsrqonmlkjihgfedcb print from 25 to 0 but not including char[0]
print(backwards)
backwards = letters[25::-1]     #zyxwvutsrqonmlkjihgfedcba print from 25 to 0  including char[0]
print(backwards)

#slice the string to produce qpo
print(letters[16:13:-1])    #qpo start @char[16] up to char[13] but not including char[13] in reverse -1

#slice the string to produce edcba
print(letters[4::-1])

#slice the string to produce last 8 characters in reverse order
print(letters[:17:-1])     #start @char[17] up to the last char including it (in reverse -1)
print(letters[:-9:-1])     #start @char[-9] up to the last char including it (in reverse -1)

print(letters[::6])

