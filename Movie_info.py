movie_list=[ { "name": "Forrest Gump", "year": 1994, "duration": 142, "genres": ["Drama", "Romance"] },
{ "name": "Avengers: Endgame", "year": 2019, "duration": 181, "genres": ["Action",
"Adventure", "Drama"] }, { "name": "Back to the Future", "year": 1985, "duration": 114,
"genres": ["Adventure", "Comedy", "Sci-Fi"] } ]
print("Welcome to movies world!!")
new_dict={}
flag=True
def input_something(inp):
    user_input = input(inp)
    while user_input == "":
        print("Input cannot be empty. Please try again.")
        user_input = input(inp)
    return user_input
def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input should only be integer. please try again.")

while flag:
    user_choice=input("Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit: ").lower()
    if user_choice=="a":
        genre_list=[]
        m_name=input_something("Enter movie's name:")
        m_year=input_int("Enter movie's year:")
        m_duration=input_int("Enter duration in minutes:")
        m_genre_num=input_int("Enter genre numbers ")
        while m_genre_num==0:
            print("You should enter atleast one genre!")
            m_genre_num = input_int("Enter genre numbers ")
        new_dict["name"]=m_name
        new_dict["year"]=m_year
        new_dict["duration"]=m_duration
        for i in range(m_genre_num):
            m_genre = input_something("Enter genre ").title()
            genre_list.append(m_genre)
        new_dict["genre"]=genre_list
        print('movie added')
        movie_list.append(new_dict)
    elif user_choice=="l":
        index=0
        if movie_list:
            for ind,j in enumerate(movie_list,start=1):
                # print(f"{index+1} {i['name']};{i['year']}")
                index=index+1
                print(f"{ind} {j['name']};{j['year']}")
        else:
            print("No movies saved")
    elif user_choice=="s":
        search_term=input_something("Give the name of the movie to search:").lower()
        if movie_list:
            index=1
            for i in movie_list:
                if search_term in i["name"].lower():
                    print(f"{index}) {i["name"]}({i["year"]})")
                    index+=1
        else:
            print("The list is empty")
    elif user_choice == "v":
        if movie_list:
            try:
                index_number=input_int("Give me an index number for the movie..")
                index_number-=1
                print(movie_list[index_number])
            except IndexError:
                print("Invalid index number")
    elif user_choice == "d":
        if movie_list:
            try:
                index_number = input_int("Give me an index number for the movie to delete:")
                index_number -= 1
                movie_list.remove(movie_list[index_number])
                print("Movie deleted")
            except IndexError:
                print("Invalid index number")
    elif user_choice == "q":
        print("Goodbye!!")
        break
    else:
        print("Please enter only from the values suggested!!")