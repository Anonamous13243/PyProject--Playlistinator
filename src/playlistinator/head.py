if __name__ == "__main__":
    from Dictionary import main
    
    for interface, serial in main.items():
        print(input("Welcome to the Playlistinator! Here you can organise your favorite songs into personal playlists!\
        File Directory (type the corresonding number): "))
        print(main[interface][serial])
        
    
    if input == serial:
        print("You selected {serial}")
