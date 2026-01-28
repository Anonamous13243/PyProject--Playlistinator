if __name__ == "__main__":
    from Dictionary import main
    
    for interface, dict_path in main.items():
        print(input("Welcome to the Playlistinator! Here you can organise your favorite songs into personal playlists! \n\
        File Directory, type the corresponding genre: \n\
        \n\
        'blues': 1.(1-9),\n\
        'classical': 2.(1-9),\n\
        'country': 3.(1-9),\n\
        'electronic': 4.(1-9),\n\
        'folk': 5.(1-9),\n\
        'hip_hop': 6.(1-9),\n\
        'jazz': 7.(1-9),\n\
        'reggae': 8.(1-9),\n\
        'rock': 9.(1-9), \n\
        \n\
        Enter here: "))
        
        input_path = main["blues"]["classical"]["country"]["electronic"]["folk"]["hip_hop"]["jazz"]["reggae"]["rock"]
        
        if input == input_path:
            print(main[input_path])