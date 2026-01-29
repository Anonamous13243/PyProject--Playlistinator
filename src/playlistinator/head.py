if __name__ == "__main__":
    from Dictionary import main
    for interface in main.keys():
        print("Welcome to the Playlistinator! Here you can organise your favorite songs into personal playlists! \n\
        File Directory, type the corresponding genre: \n\
        \n\
        --------------------------------------------------------------------------------------------------------------\n\
        blues\n\
        classical\n\
        country\n\
        electronic': 4.(1-9),\n\
        'folk': 5.(1-9),\n\
        'hip_hop': 6.(1-9),\n\
        'jazz': 7.(1-9),\n\
        'reggae': 8.(1-9),\n\
        'rock': 9.(1-9),\n\
        \n\
        ---------------------------------------------------------------------------------------------------------------")
        key = input("\n\
        Please put quotations around your desired input. \n\
        ")
        print(interface.get(key))
        for sub, serial in interface.keys():
            print(sub)
            print(serial)
        break
    user_input = main.keys
    print(main[user_input])
    for label, serial in user_input():
        print(input("Now, type the corresponding serial. \n\
                    The serials (which name subclasses) should be printed above this guide. \n\
                    ------------------------------------\n\
                    "))
        if input == serial:
            print(label)
