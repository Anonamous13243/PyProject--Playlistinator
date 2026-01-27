if __name__ == "__main__":
    from Dictionary import blues, classical, country, electronic, folk, hip_hop, jazz, reggae, rock
    
    info_of_genres = blues.items, classical.items, country.items, electronic.items, folk.items, hip_hop.items, jazz.items, reggae.items, rock.items

    genre = []
    serial = []
    for i in info_of_genres:
        genre.append(i)
        serial.append(i)
    print(genre, serial)
        

'''
print(input("Welcome to the Playlistinator! Here you can organise your favorite songs into personal playlists!\
File Directory (type the corresonding number): {main_genres}"))
'''