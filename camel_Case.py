#variable
sentence = "fOnt proCESSOR and ParsER"
sentence_Split = sentence.split()
#list
my_List = [sentence_Split[0].lower()]
new_word = ""
print(sentence_Split)

#for loop
for j in range(1, len(sentence_Split)):
    word = sentence_Split[j].capitalize()
    my_List.append(word)
    print("" .join(my_List))

