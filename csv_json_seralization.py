import json
from csv import DictReader
""" A simple program that will create a formatted JSON file using CSV data."""

# open *.csv file and read it into a DictReader
with open('netflix_titles.csv', 'r', encoding='utf-8') as nflx_file:
    reader = DictReader(nflx_file)
    # initial list of "tv show" values
    show_list = []
    # sort through each column of interest and create a list of the values
    for row in reader:
        if row['type'] == 'TV Show':
            show_list.append({'show_id': row['show_id'],
                              'title': row['title'],
                              'director': row['director'],
                              'country': row['country'],
                              'date_added': row['date_added'],
                              'duration': row['duration']})
            # creates a file, writes to it the formatted json info
            with open('tv_show_info.json', 'w') as json_file:
                json.dump(show_list, json_file, indent=4)
