def friends():
    contents = {}
    filename = "dwarves.txt"
    with open(filename, "r") as file:
        for line in file:
            parts = line.split()
            if len(parts) == 0:
                continue
            contents[parts[0]] = parts[1:]
    return contents

def overwrite(friends_dic):
    filename = "dwarves.txt"
    with open(filename, "w") as file:
        for key in friends_dic.keys():
            file.write(key + " ")
            friends_list = friends_dic[key]
            file.write(" ".join(friends_list))
            file.write("\n")


def main():
    user_input = input("Which of the 7 dwarves is logging in?\n")
    friends_dic = friends()
    friends_list = friends_dic[user_input]
    while True:
        question = input("Choose from one of the options below:\n P: Print your friends list\n U <name>: Unfriend someone\n F <name>: Frined someone\n Q: Quit\n")
        if question == "P":
            print("Your friends: " + " ".join(friends_list))
        elif question[0] == "U":
            name = question[2:]
            if name in friends_list:
                friends_list.remove(name)
                print(name + " has been unfriended.")
            else:
                print(name + " is not your friend.")

        elif question[0] == "F":
            name = question[2:]
            if name in friends_list:
                print(name + " is your friend already.")
            else:
                friends_list.append(name)
                print(name + " is your friend now.")

        elif question == "Q":
            break
    overwrite(friends_dic)


if __name__ == "__main__":
    main()

