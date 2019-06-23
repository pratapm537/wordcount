from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def count(request):
    data=request.GET['fulltextarea']
    word_list=data.split()
    list_length=len(word_list)

    worddictionary={}

    for word in word_list: #store the value as key in empty dic
        if word in worddictionary:
            #if word already exit then increase the value by 1
            worddictionary[word]+=1 #im confuse on this point/worddictionary[word]=worddictionary[word]+1

        else:
            #if word does not exit then add to the dictionary and set value to 1
            worddictionary[word]=1

    return render(request,'count.html',{'fulltext':data,'wordcount':list_length,'worddictionary':worddictionary.items()})

def about(request):
    return render(request,'about.html')
