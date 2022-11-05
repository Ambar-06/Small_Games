import random as rp
import requests
import json

def main():
    l = get_url()
    rn_word = generate_random_word(l)
    user_guess(rn_word)


def user_guess(r_w):       #will ask the user to guess letters by letters and take randomword as argument
    m_t_list = []           #created an empty list to store each letter as a value
    dash_list = []           #created another empty list to store _ as values
    duplicate_list = []         #creating a duplicate list
    for letters in r_w:     #for each letters of the word
        dash_list.append("_")     #will append _ as values
        m_t_list.append(letters)    #will store each letters of the word in the list as single value
        duplicate_list.append(letters)  #creating a duplicate list
    for j in range(len(r_w)):           #for iterating in the list of _
        print(dash_list[j], end =" ")     #will print a blankspace on the same line

    while dash_list != duplicate_list:           #will start a loop to keep asking user for guesses
        guesses = input("Guess a Letter: ").strip().lower()     #will ask the user to guess
        index_of_element = find_element(guesses, m_t_list)  #will pass the guess and the list of letters to func
        if index_of_element != 123456:          #if index is not a garbage value returned by the function
            dash_list.pop(index_of_element)
            dash_list.insert(index_of_element, guesses)
            m_t_list.pop(index_of_element)
            m_t_list.insert(index_of_element, "*")
            for __ in range(len(dash_list)):
                print(dash_list[__], end =" ")
            print(duplicate_list)
            print(m_t_list)
            print(dash_list)
        else:
            print("Wrong Guess!")
        
        if dash_list == duplicate_list:
            print("Level Cleared!")
            break


def get_url():
    url = requests.get("https://www.randomlists.com/data/words.json")   #requsting link
    readable_url = url.json()       #making json dict readable
    return readable_url['data']     #returning a list for key 'data' with a value as list

def generate_random_word(r):        #will pass the list as an argument
    random_word = rp.choice(r)        #will pick a random word from the list
    return random_word              #will return that word


def find_element(x, z):
    if x in z:
        y = z.index(x)
        return y
    else:
        return 123456   #returning a garbage value to make sure that func is returning an int


if __name__=="__main__":
    main()