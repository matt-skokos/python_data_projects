import json
from csv import DictReader


def retrieve_tv_shows(file):
    """ Takes in a *.csv file, reads it and returns selected data in a
    list.
    """
    with open(file, 'r', encoding='utf-8') as nflx_file:
        reader = DictReader(nflx_file)
        show_list = []
        for row in reader:
            if row['type'] == 'TV Show':
                show_list.append({'show_id': row['show_id'],
                                  'title': row['title'],
                                  'director': row['director'],
                                  'country': row['country'],
                                  'date_added': row['date_added'],
                                  'duration': row['duration']})

    return show_list


def write_json(list_of_shows):
    """Takes a list of fields and attributes and returns a JSON file."""
    with open('tv_show_info.json', 'w') as json_file:
        json.dump(list_of_shows, json_file, indent=4)


def main():
    # returns a list object with 'show_id', 'title', 'director',
    # 'country', 'date_added', 'duration'
    data = retrieve_tv_shows('netflix_titles.csv')

    # Write the list in JSON format to the *.json file
    write_json(data)


if __name__ == '__main__':
    main()
