first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result=(len(x1)-len(x2)for x1,x2 in zip(first, second) if len(x1)!=len(x2))
second_result=(len(first[i])==len(second[i])for i in range(len(first)))
print(list(first_result))
print(list(second_result))
