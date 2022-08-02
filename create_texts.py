import os
import json
import re
from lyricsgenius import Genius
from dotenv import load_dotenv

load_dotenv()

CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_ACCESS_TOKEN = os.environ.get('CLIENT_ACCESS_TOKEN')

def create_lyrics_json(search = None, song_count = 100):
  genius = Genius(CLIENT_ACCESS_TOKEN)
  if search == None:
    search = input('Enter artist to search: ')
  artist = genius.search_artist(search, max_songs = song_count)
  artist.save_lyrics()
  return f"Lyrics_{artist.name}"

def sanitize_text(text):
  return re.sub(r'[1]?Embed', '', text)

def create_txt_from_json(filename):
  text_string = ''
  with open(f'{filename}.json') as json_file:
    dict = json.load(json_file)
    print('Writing Songs')
    for song in dict['songs']:
      text_string += song['title'] + '\n'
      text_string += song['lyrics'] + '\n\n\n\n'
  text_string = sanitize_text(text_string)
  new_filename = filename.replace('Lyrics_', '')
  with open(f'./lyric_files/{new_filename}.txt', 'w', encoding='UTF-8') as text_file:
    text_file.write(text_string)
  print(f'Removing {filename}.json')
  os.remove(f'{filename}.json')

if __name__ == '__main__':
  filename = create_lyrics_json()
  filename.replace(' ', '') #get rid of spaces
  create_txt_from_json(filename)