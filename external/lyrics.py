#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# SimSimI Telegram Bot
# This program is dedicated to the public domain under the CC0 license.
import urllib
import urllib3
import json


def get_lyrics(user_text):
    song_info = user_text.replace('musica', '').split('-')
    print song_info
    if len(song_info) == 2:
        artist, song = urllib.quote_plus(song_info[0]), urllib.quote_plus(song_info[1])
        http = urllib3.PoolManager()
        url = ("http://api.vagalume.com.br/search.php?"
               "art={art}&mus={song}".format(art=artist, song=song))
        r = http.request('GET', url)
        status = r.status
        dict_ = json.loads(r.data.strip())
        lyrics_info = dict_.get('mus')[0]
        lyrics = lyrics_info.get('text')
        return lyrics, status
    return 'Música não encontrada', 404
