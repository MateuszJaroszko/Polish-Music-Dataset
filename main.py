from scrapers import genius
import yaml
import time

if __name__ == "__main__":

    with open('artists.yaml') as file:
        yaml_data = yaml.load(file, Loader=yaml.FullLoader)
    genius.dataframe_init(filename="test")
    for artist in yaml_data['Artists']:
        try:
            genius.get_songs(artist, 3, filename="test")
        except ConnectionError:
            time.sleep(5*60)
