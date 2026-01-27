if __name__ == "__main__":
    from Dictionary import blues, classical, country, electronic, folk, hip_hop, jazz, reggae, rock
    
    info_of_genres = blues.items.split, classical.items.split, country.items.split, electronic.items.split, folk.items.split, hip_hop.items.split, jazz.items.split, reggae.items.split, rock.items.split

    subgenre_interface = [str(info_of_genres)]
    serial = [float(info_of_genres)]
    for i in info_of_genres:
        subgenre_interface.append(i)
        serial.append(i)
    print(subgenre_interface, serial)
        

'''
print(input("Welcome to the Playlistinator! Here you can organise your favorite songs into personal playlists!\
File Directory (type the corresonding number): {main_genres}"))
'''