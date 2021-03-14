from collections import Counter


##Cracking the Coding Interview String Problems
'''
These are the solution for the string and array problems found in the famous 
"Cracking the Coding Interview" book (pages 90-91)
Hope it helps!

'''

##Is Unique
def is_unique():
    string = input("Enter a string = ")
    c = Counter(string)
    # print(c)
    flag = False
    for key in c.keys():
        # print(key)
        if (c[key] > 1):
            print("Not Unique !")
            flag = True
            break

    if not flag:
        print("Unique!")




# Is Permutation
def is_permutation():
    s1 = input("Enter a string = ")
    s2 = input("Enter another string = ")

    c1 = Counter(s1)
    c2 = Counter(s2)

    if (c1 == c2):
        print("True")
    else:
        print("False")



#Urlify
def urlify():
    string = input("Enter a string = " )
    string = string.strip()
    string = string.replace(" ", "%")
    print(string)


#Palindrome Permutation
def palindrome_permutation():
    string = input("Enter a string = ")
    string = string.replace(" ", "")
    string = string.lower()
    if (len(string) == 1):
        print("Could be a Palindrome!")
    else:
        flag1 = False
        flag2 = False
        c = Counter(string)
        #print(c)
        for elem in c:
            #print(elem, c[elem])
            if c[elem] % 2 == 0:
                continue
            elif (flag1):
                print("No palindrome :( ")
                flag2 = True
                break
            else:
                flag1 = True
        if not flag2:
            print("Palindrome Permutation :) ")

#One Away
def check_replace(str1,str2):
    flag = False
    flag2= False
    for elem,elem2 in zip(str1, str2):
        if(elem ==elem2):
            continue
        elif(flag):
            print("NOT 1 edit distance away")
            flag2=True
            break
        else:
            flag=True
    if not flag2:
        print("1 edit-distance away!!!")


def check_add(str1,str2):
    if(len(str1)>len(str2)):
        longstr = str1
        shortstr= str2
    else:
        longstr = str2
        shortstr = str1
    i =0
    j=0
    flag = False
    while(i < len(longstr) and j <len(shortstr)):
        if(longstr[i] == shortstr[i]):
            i+=1
            j+=1
        else:
            i+=1
            if(longstr[i:]==shortstr[j:]):
                print("One edit distance away!")
                flag = True
                break
            else:
                print(" Not one edit distance away!")
                flag= True
                break
    if not flag:
        print("One edit distance away!")


def string_compression():

    #This one I changed slightly from the one in the book...
    '''
   Instead of returning a2b1c5a3, mine would actually save space and return a2bc5a3,
    meaning that if it is a single char
   it will just return that (w/o the 1).
    '''
    string = input("Enter a string (to be compressed)")
    resstr = ""
    i =0
    current = string[0]
    reps = 0
    for char in string:
        if(char == current):
            reps +=1
        else:
            if(reps>1):
                resstr=resstr+current+str(reps)
            else:
                resstr = resstr + current
            current = char
            reps = 1
    if (reps > 1):
        resstr = resstr + current + str(reps)
    else:
        resstr = resstr + current
    print(resstr)






#One Edit Away
def one_edit_away():
    str1 = input("Enter a string = ")
    str2 = input("Enter another string = ")
    if (abs(len(str1) - len(str2)) > 1):  # This takes the case of more than one letter diff
        print("Not one edit distance away!")
    elif (str1 == str2):  # this takes the case for same string
        print("One edit distance away!")
    elif (len(str1) == len(str2)):  # Same lenght, simply checks if one letter can be replaced
        check_replace(str2, str1)
    else:  # checks if there is a letter that could be added to make it true
        check_add(str1, str2)

def Exit():
    exit(0)





def Main():
   while(True):
       print("Welcome to the string problem solver")
       print("Options = ")
       print("1 - Is Unique --- determines if all the characters in a given string are unique")
       print("2 - Is a Permutation --- determines if a string is a permutation of another string")
       print("3 - Urlify --- urlifys a given string")
       print("4 - Palindrome Permutation --- determines if a string could be a palindrome")
       print("5 - One Edit Distance --- determines if a string is one edit distance away from another string")
       print("6 - String Compression --- will return a compressed string")
       print("E - Exit ")
       optdict = {"1": is_unique, "2": is_permutation, "3": urlify, "4": palindrome_permutation, "5": one_edit_away, '6':string_compression,
                  "E": Exit}
       option = input("Pick an option = ")
       while option not in optdict.keys():
           print("Invalid Option try again!")
           option = input("Pick an option =  ")
       optdict[option]()
Main()
