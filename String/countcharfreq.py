## Taking the input from the user
user_input=input("Enter the sentence or word")
lower_input=user_input.lower()
dic={}
for i in lower_input:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
  

print(dic)