import lyricsgenius
import pandas as pd
import time
import os
api_key = "key_here"
genius_token = "token_here"
genius = lyricsgenius.Genius(genius_token)

def get_id(song):
    for platform in song.media:
        if platform['provider'] == "youtube":
            video_id = platform['url'].split("?v=")[-1]
            return video_id

def get_data_from_genius(artist_names, count=5, filename="dataset"):
    columns = ["title", "artist", "album", "year",
             "yt_url", "yt_id", "genius_url", "yt_id","featured_artists",
              "writer_artists", "producer_artists", "lyrics"]
    df = pd.DataFrame(columns=columns)
    if not os.path.isfile(f"lyrics/{filename}.csv"):
        df.to_csv(f"lyrics/{filename}.csv")
        

    for artist_name in artist_names:
        artist = genius.search_artist(artist_name, max_songs=count)
        songs = [song.title for song in artist.songs]
        for title in songs:
            try:
                song = genius.search_song(title, artist_name)
                title = song.title
                artist = song.artist
                album = song.album
                year = song.year
                yt_url = [item["url"] for item in song.media]
                yt_id = get_id(song)
                genius_url = song.url
                featured_artist = [item['name'] for item in song.featured_artists]
                writer_artist = [artist['name'] for artist in song.writer_artists]
                producer_artist = [producers['name'].strip(u'\u200b') for producers in song.producer_artists]
                lyrics = song.lyrics.replace('\n', ' ')
                
            except:
                print("Problem with song, go next...")

            data_dict = {
                    "title": title,
                    "artist": artist,
                    "album": album,
                    "year": year,
                    "yt_url": yt_url,
                    "yt_id": yt_id,
                    "genius_url": genius_url,
                    "featured_artists": featured_artist,
                    "writer_artists": writer_artist,
                    "producer_artists": producer_artist,
                    "lyrics": lyrics}
            #print(len(data))
            #df1 = pd.DataFrame(data_dict)
            df = df.append(data_dict, ignore_index=True)
            df.to_csv(f"lyrics/{filename}.csv", mode="a", index=False, header=False)
            df = pd.DataFrame(columns=columns)

