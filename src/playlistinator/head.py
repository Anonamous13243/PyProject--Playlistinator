if __name__ == "__main__":
    from Dictionary import main
    
    for interface, serial in main.items():
        print(input("Welcome to the Playlistinator! Here you can organise your favorite songs into personal playlists!\
            File Directory (type the corresonding number): "))
        print("\
        'blues': 1.(1-9),\
        'classical': 2.(1-9),\
        'country': 3.(1-9),\
        'electronic': electronic,\
        'folk': folk,\
        'hip_hop': hip_hop,\
        'jazz': jazz,\
        'reggae': reggae,\
        'rock': rock,")
        if interface != serial:
            print("Error! Given serial does not match corresponding dictionary cache.")