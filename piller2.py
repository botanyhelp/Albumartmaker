#!/usr/bin/python
import Image
import ImageDraw
import ImageFont
import textwrap

astr='''Maynard Ferguson & Chris Connor
"I Feel a Song Coming On"
Two's Company
Roulette
1963
Cannonball Adderley
"Del Sosser"
Riverside - The Soul of Jazz 1961
Riverside
1961
Shorty Rogers
"Everybody Loves a Lover"
Chances are it Swings
RCA
1958
Shorty Rogers
"Come to Me"
Chances are it Swings
RCA
1958
Jimmy Smith & Wes Montgomery
"James & Wes"
The Dynamic Duo
Verve
1966
Sonny Rollins
"Valse Hot"
Sonny Rollins Plus Four
Prestige
Barney Kessel
"Green Dolphin Street"
The Poll Winners
Contemporary
1957
Hampton Hawes
"Hip"
For Real
Contemporary
1961
Sarah Vaughan and Oscar Peterson
"How Long Has this Been Going On"
How Long has this Been Going On
Pablo
1978
Oscar Peterson
"I Got Plenty of Nuthin'"
Porgy and Bess
Pablo
1976
Charles Mingus
"Dizzy Moods"
Tijuana Moods
RCA
1962
Dizzy Gillespie
"Be Bop"
Dizzy Gillespie's Big 4
Pablo
1975
Victor Feldman
"Bloke's Blues"
Merry Olde Soul
Riverside
1961
Wes Montgomery
"Up and At It"
Down Here on the Ground
CTI
1967
Ray Charles
"In the Evening"
Recipe for Soul
ABC-Paramount
1963
Victor Feldman
"You and Me"
Victor Feldman Plays Everything in Sight
Pacific Jazz
Ella Fitzgerald
"I'm In the Mood for Love"
Lady Time
Pablo
1978
Cannonball Adderley
"Never Will I Marry"
The Poll Winners
Riverside
1960
Count Basie
"Eleanor Rigby"
Basie on the Beatles
Happy Tiger
1969
Anita O'Day
"anks for the Boogie Ride"
Gene Krupa, Anita O'Day & the Orchestra
Columbia
1974'''
para=textwrap.wrap(astr,width=48)

MAX_W,MAX_H=300,300
im = Image.new('RGB', (MAX_W, MAX_H), (145, 145, 120, 0))
draw = ImageDraw.Draw(im)
#font = ImageFont.truetype('/usr/share/fonts/truetype/msttcorefonts/Arial.ttf', 36)
#font = ImageFont.truetype('/usr/share/fonts/bitstream-vera/Vera.ttf', 36)

current_h=0
for line in para:
    #w,h=draw.textsize(line, font=font)
    w,h=draw.textsize(line)
    #draw.text(((MAX_W-w)/2, current_h), line, font=font)
    draw.text(((MAX_W-w)/2, current_h), line)
    current_h+=h

im.save('test.png')
