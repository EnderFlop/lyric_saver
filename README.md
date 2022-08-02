# Lyric Saver - Find keywords in artist's lyrics!
Ever forget a bar from a song but it's on the tip of your tongue? Ever want to make a playlist where all the songs have a common theme? All you need is an artist and some keywords and these scripts will help you cherry pick the best songs available!
## Usage

 1. Install the python files and install the related packages in the
    requirements.txt 
 2. Create a .env file and put in your Genius API Access Token 
 3. Run create_texts.py and type in the artist you want to look up 
 4. Wait while the script collects all the songs for you and places a text file in lyric_files 
 5. Comb through the lyrics manually or go to analyze_texts.py and type in some keywords in the KEYWORDS list! Run the file and check out the corresponding files in
    analyzed_files, specially formatted to only give you lines relating
    to your keywords.
