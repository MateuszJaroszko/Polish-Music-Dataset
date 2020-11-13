from scrapers import songs_list
import yaml
import time

if __name__ == "__main__":

    with open('artists.yaml') as file:
        yaml_data = yaml.load(file, Loader=yaml.FullLoader)

    for artist in yaml_data['Artists']:
        try:
            songs_list.get_songs(artist, None, filename="all_titles")
        except ConnectionError:
            time.sleep(5*60)
