#Author: Aaron Wajah
#Date: 11/01/2023
#Description: List Manipulation 1; ascending, descending,


user_list=[2,3,4,56,6,23]
user_sort_choice =input("Insert sorting method: \n 1. ascending(asc) \n 2. descending(dsc) \n 3. none \n ")


def sorting_list(user,user_input):
    user=user_list

    if user_input =='asc':
        user.sort()
        print(user)

    elif user_input=='dsc':
        user.sort(reverse=True)
        print(user)

    elif user_input == 'none': 
        print(user)
    

sorting_list(user_list,user_sort_choice)




