def swappingfile():  
    with open("sample1.txt","r") as a:
     data_a= a.read()
    with open("sample1.txt","w") as a:
     a.write("sample2.txt")
    with open("sample2.txt","r") as b:
     data_b= b.read()
    with open("sample2.txt","w") as b:
     b.write("sample1.txt")
    print(data_a)
    print(data_b)
swappingfile()