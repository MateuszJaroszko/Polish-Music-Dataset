from scrapers import songs_list
import yaml

if __name__ == "__main__":

    with open('artists.yaml') as file:
        yaml_data = yaml.load(file, Loader=yaml.FullLoader)

    for artist in yaml_data['Artists']:
        songs_list.get_songs(artist, 3)
