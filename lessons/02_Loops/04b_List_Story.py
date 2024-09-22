"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story

            0       1       2   3       4       5       6      7    8
"""            
words = ['Once', '👦', 'upon', '🐕', 'park', 'met', 'with', 'a', 'the', 
    'time', 'to', 'who', '🐈', '👧', 'and', 'went', 'had', 'play', '⚽.', 
    'they','at']

story = [words[0],words[2],words[7],words[9],words[7],words[13],words[14],words[1],words[15],words[10],words[17],words[20],words[8],words[4],words[10],words[17],words[18],words[19],words[16],words[7],words[3],words[14],words[12],words[11],words[17],words[6],words[1],words[14],words[13]]

# Create a story using the words in the list

# Display the story to the user
print(' '.join(story))