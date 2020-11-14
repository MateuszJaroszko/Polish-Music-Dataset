import lyricsgenius
import pandas as pd
import os

genius_token = ""

genius = lyricsgenius.Genius(genius_token, timeout=10)

def dataframe_init(filename):
    df = pd.DataFrame(columns=['title', 'album', 'year', 'lyrics', 'image'])
    if not os.path.isfile(f"./data/{filename}.csv"):
            df.to_csv(f"./data/{filename}.csv", index=False)
            print("CREATE DATAFRAME")

def get_songs(artist_name, max_songs, filename):
    df = pd.read_csv(f"./data/{filename}.csv")
    artist = genius.search_artist(artist_name, max_songs=max_songs)
    print("Finish GENIUS API") 
    for song in artist.songs:
        try:
            print("Start writing songs")
            song = song.to_dict()
            song['artist'] = artist.name
                
            row = pd.Series(data=song, name=len(df))
            df = df.append(row)
            df.to_csv(f"./data/{filename}.csv", index=False)
        except:
            "Error"
