import os
import re

KEYWORDS = ['take']

def filter_empty_strings(lst):
  lst = list(filter(lambda elem: elem != '', lst))
  return list(filter(lambda elem: elem != '\n', lst))

def analyze_texts():
  for filename in os.listdir('./lyric_files'):
    with open(f'./lyric_files/{filename}', 'r', encoding='UTF-8') as all_lyrics:
      text_string = ''
      songs = filter_empty_strings(all_lyrics.read().split('\n\n\n'))

      for song in songs:
        song = filter_empty_strings(song.split('\n'))
        text_string += song[0] + "\n##########\n\n" #Title

        for index, line in enumerate(song):
          if any(re.findall(word, line) for word in KEYWORDS):

            if index >= 2 and index <= len(song) - 2: #attempt to add context lines
              for x in song[index-2:index+3]:
                text_string += x + '\n'

            else: #if near end or beginning, just add line
              text_string += line + '\n'

            text_string += '\n\n'

      with open(f'./analyzed_files/{filename}', 'w', encoding='UTF-8') as new_text_file:
        new_text_file.write(text_string)
    
if __name__ == '__main__':
  analyze_texts()