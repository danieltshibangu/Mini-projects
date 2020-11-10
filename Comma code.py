# program uses function to turn list into printed string no matter
# what is passed to it.



def listToStr( list ):
    newList = ''

    for i in range(len(list)):
        if i < len(list)-1:
            newList = newList + str(list[i]) + ', '
        else:
            newList = newList + 'and ' + str(list[i]) + '.'

    return newList

# the main function here will return the newList
def main():
    randList = [ 'apples', 810, 'berleese', 0.2738927 ]
    print( listToStr( randList ))

if __name__ == '__main__':
    main() 
