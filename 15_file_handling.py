with open('weather_data.csv','r') as f:
    # print(f.readline(),end='')
    # print(f.readline())
    print(f.read(10))#first 10 char of the file
    size_to_read=15
    f.seek(2)
    f_contents=f.read(size_to_read)
    print(f.tell())#tells us the location of a file

    #print(f.readlines())
    # for l in f:
    #     #As it doesnt read all file at once we dont get memory issue
    #     print(l,end="")
    # while len(f_contents)>0:
    #     print(f_contents)
    #     f_contents=f.read(size_to_read)