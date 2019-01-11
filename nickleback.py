# In this exercises, you're going to use a conditional statement inside a comprehension. 

# 1. Define a set that contains tuples. Each tuple should contain two strings:
#     -The name of an artist
#     -A song by that artist
#
#    Make sure that some of the songs are from the band Nickelback.

songs = {
    ('Nickelback', 'How You Remind Me'),
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals')
}

# 2. Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.

''' 
    
    Note to self: In comprehensions, if you were to write them in a traditional for loop, the return that is at the end of the for loop actually goes at the 
    beginning of the comprehension. In the example below the "return" would be band[1}
    
'''
new_songs = {band[1] for band in songs if band[0] != "Nickelback"}

print(new_songs)