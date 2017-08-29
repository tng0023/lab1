#gather input
y = str(input("Type in a sentence: "))

#capitalize each word
ysplit = y.title()
#slice all words
camelcase = ysplit[::1]
#remove spaces
ysplit = camelcase.replace(" ", "")


print(ysplit)
