# 6.0001 Spring 2020
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands

# Problem Set 3
# Name: Joy Bhattacharya
# Collaborators: None
# Time Spent: 5 hours
# Late Days Used: (only if you are using any)

import string

# - - - - - - - - - -
# Check for similarity by comparing two texts to see how similar they are to each other


### Problem 1: Prep Data ###
# Make a *small* change to separate the data by whitespace rather than just tabs
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        list of strings holding the file contents where
            each string was separated by a newline character (\t) in the file
    """
    inFile = open(filename, 'r')
    line = inFile.read()
    inFile.close()
    line = line.strip().lower()
    for char in string.punctuation:
        line = line.replace(char, "")
    return line.split() #splits the characters on whitespaces 

### Problem 2: Find Ngrams ###
def find_ngrams(single_words, n):
    """
    Args:
        single_words: list of words in the text, in the order they appear in the text
            all words are made of lowercase characters
        n:            length of 'n-gram' window
    Returns:
        list of n-grams from input text list, or an empty list if n is not a valid value
    """
    n_gram='' #initializes empty string 
    n_gram_list=[] #initializes empty list 
    empty_list=[]
    x=len(single_words)-(n) #this variable sets a boundary for the last element in the list you can still have an n_gram for. For example, if you have a list of 5 words like ["problem", "set", "number", "three", "cool"] and you want n to equal 3, then x tells you that the last element for which you could have an n-gram of length 3 is the (5-n) indexed element, what would be "number" in this case. 
    if n<=0 or n>len(single_words): #function returns an empty list if n is not a positive integer or if n is greater than the number of elements in the single_word list
        return empty_list 
    else:
        for i in range(len(single_words)): #iterate over the elements in the range of the list. Specifically iterates over the number of the element over the total number of elements in the list. 
            if i<=x: #if your i is less than or equal to the boundary (the last possible element you can still have an n-gram for)
                n_gram=' '.join(single_words[i:i+n]) #finds the elements indexed from i to the length of your n value. Say n=3, then this would get the element for index i, index i+1, and index i+2. Then it takes these elements and joins them into a string with a space separating elements. 
                n_gram_list.append(n_gram) #Takes the string created in the line above and adds it to a list. 
    return n_gram_list #returns the value of the list of n_grams
    

### Problem 3: Word Frequency ###
def compute_frequencies(words):
    """
    Args:
        words: list of words (or n-grams), all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a word (or n-gram) in words and the corresponding int
        is the frequency of the word (or n-gram) in words
    """
    frequency_dict={} #initializes a dictionary
    for element in words: #goes through every element in the list of words
        if element in frequency_dict:#if the element is already a key in the dictionary, then add 1 to the value associated with that element, in other words, increase the frequency that the word has appeared by 1
            frequency_dict[element]+=1
        else:#if the element isn't already in the dictionary, add it as a key and assign it a value of 1, meaning that it initially has a frequency of 1
            frequency_dict[element]=1
    return(frequency_dict)#returns the dictionary after the for loop is over 

### Problem 4: Similarity ###
def get_similarity_score(dict1, dict2, dissimilarity = False):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        dict1: frequency dictionary of words or n-grams for one text
        dict2: frequency dictionary of words or n-grams for another text
        dissimilarity: Boolean, optional parameter. Default to False.
          If this is True, return the dissimilarity score, 100*(DIFF/ALL), instead.
    Returns:
        int, a percentage between 0 and 100, inclusive
        representing how similar the texts are to each other

        The difference in text frequencies = DIFF sums words
        from these three scenarios:
        * If a word or n-gram occurs in dict1 and dict2 then
          get the difference in frequencies
        * If a word or n-gram occurs only in dict1 then take the
          frequency from dict1
        * If a word or n-gram occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 100*(1-(DIFF/ALL)) rounded to the nearest whole number if dissimilarity
          is False, otherwise returns 100*(DIFF/ALL)
    """
    a=0 
    b=0
    c=0
    total_frequency_1=0
    total_frequency_2=0
    for key in dict1: #iterate over all the keys in dictionary 1
        total_frequency_1+=dict1[key] #sums up all the frequencies for every key
        if key in dict2: #if the key is also in dictionary 2
            a+=abs(dict1[key]-dict2[key]) #finds the value of the difference between the frequency for that key in dictionary 1 and dictionary 2. This value is incremented for the final formula. 
        else:
            b+=dict1[key] #if the key is only in dictionary 1, then just fine the frequency associated with that value in dictionary 1. This vale is incremented for the final formula. 
    for key in dict2: #iterate over all the keys in dictionary 2
        total_frequency_2+=dict2[key] #sums up all the frequencies for every key
        if key not in dict1: #if your key is only in dictionary 2 
            c+=dict2[key] #Find the frequency associated with that key. Increment this value for the final formula. 
    DIFF=a+b+c #defines the variable DIFF of the sum of variables a, b, and c 
    ALL=total_frequency_1+total_frequency_2 #defines the variable ALL as the sum of the total frequencies in dict1 and dict2
    if dissimilarity==False: #if this parameter is false, return the following formula
        return round(100*(1-DIFF/ALL))
    else: #otherwise, return the following formula 
        return round(100*(DIFF/ALL))
            

### Problem 5: Most Frequent Word(s) ###
def compute_most_frequent(dict1, dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        dict1: frequency dictionary for one text
        dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
    #initialized variables, dictionaries, and lists to be used later
    x=0 
    total_frequency_dict={}
    max_frequency=[]
    L=[]
    sorted_answer=[]
    for key in dict1: #iterates over every key in dict 1
        if key in dict2: #if the key is also in dict2:
            x=dict1[key]+dict2[key] #define a new variable x that takes the frequency of the key in dict1 and adds it to the frequency of the key in dict2
            total_frequency_dict[key]=x #add this key to the total_frequency_dict with the frequency x, taken by adding frequencies in dict1 and dict2
        else: #if the key is only in dict1
            total_frequency_dict[key]=dict1[key] #add this key to the total_frequency_dict with an associated value given by the frequency of the key in dict1
    for key in dict2:
        if key not in dict1:#if the key is only in dict2:
            total_frequency_dict[key]=dict2[key] #add this key to the total_frequency_dict with an associated value given by the frequency of the key in dict2    
    #By this point, we have a total_frequency-dict whose keys are the keys from dict1 and dict2, and whose associated values are the total frequencies for each specific key in dict1 and dict2
    max_frequency=max(total_frequency_dict.values())#finds the max value or frequency from the total_frequency_dict
    for key in total_frequency_dict: #iterate over every key in total_frequency_dict
        if total_frequency_dict[key]==max_frequency: #if the value of that key is equal to the max value we found earlier
            L.append(key) #append that key to a list
    sorted_answer=sorted(L) #sort the list alphabetically
    return sorted_answer #returns the sorted list 

### Problem 6: Finding closest artist ###
def find_closest_artist(artist_to_songfiles, mystery_lyrics, ngrams = 1):
    """
    Args:
        artist_to_songfiles:
            dictionary that maps string:list of strings
            where each string key is an artist name
            and the corresponding list is a list of filenames (including the extension),
            each holding lyrics to a song by that artist
        mystery_lyrics: list of single word strings
            Can be more than one or two words (can also be an empty list)
            assume each string is made of lowercase characters
        ngrams: int, optional parameter. Default set to False.
            If it is greater than 1, n-grams of text in files
            and n-grams of mystery_lyrics should be used in analysis, with n
            set to the value of the parameter ngrams
    Returns:
        list of artists (in alphabetical order) that best match the mystery lyrics
        (i.e. list of artists that share the highest average similarity score (to the nearest whole number))

    The best match is defined as the artist(s) whose songs have the highest average
    similarity score (after rounding) with the mystery lyrics
    If there is only one such artist, then this function should return a singleton list
    containing only that artist.
    However, if all artists have an average similarity score of zero with respect to the
    mystery_lyrics, then this function should return an empty list. When no artists
    are included in the artist_to_songfiles, this function returns an empty list.
    """
        
    Artist_Totalaverage=[]
    Closest_artists=[]
    similarity_dict={}
    ngrams_list=find_ngrams(mystery_lyrics,ngrams) #finds the list of ngrams in the mystery lyrics
    mystery_dict=compute_frequencies(ngrams_list) #makes a dictionary computing the ngram in the mystery lyric with its frequency
    for key in artist_to_songfiles: #iterate over keys in artist_to_songfiles dictionary
        songlist=artist_to_songfiles[key] #define the songlist as the value associated with the key, or artist
        total_song_similarity=0 #initializes total_similarity
        for song in songlist: #iterates over every songfile in the list
            song_string=load_file(song) #loads a string of each songfile
            ngrams_of_song=find_ngrams(song_string,ngrams) #finds the ngrams in the song
            frequency_in_song_dict=compute_frequencies(ngrams_of_song) #gets a dictionary computing word frequency in the specific song
            song_similarity=get_similarity_score(mystery_dict, frequency_in_song_dict) #gets a similarity score between the mystery song and the artist's song
            total_song_similarity+=song_similarity
        average_similarity=total_song_similarity/len(songlist) #finds the average of all similarities for the songs of the artist
        average_rounded_similarity=round(average_similarity) #rounds the average to the nearest integer
        Artist_Totalaverage.append(average_rounded_similarity) #creates a list of average similarities for each artist
        similarity_dict[key]=average_rounded_similarity #creates a new dictionary mapping the artist name with their average similarity score
    if len(Artist_Totalaverage)!=0:#if the length of your list isn't 0, proceed
        highest_average=max(Artist_Totalaverage) #find the highest average in the list of average similarity scores per artist
        if highest_average==0: #return an empty list if highest_average is 0
            return []
        for artist in similarity_dict: #iterates over the artist: average similarity score dictionary
            if similarity_dict[artist]==highest_average: #if the average is the highest average
                Closest_artists.append(artist) #add the artist to a new list of artists with the highest similarity scores
        sorted_artists=sorted(Closest_artists) #sort the list alphabetically              
        return sorted_artists #returns sorted list 
    else:
        return []
        
        
if __name__ == "__main__":
    pass
    ##Uncomment the following lines to test your implementation
    # Tests Problem 0: Prep Data
    test_directory = "tests/student_tests/"
    world, friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    print(world) ## should print ['hello', 'world', 'hello']
    print(friend) ## should print ['hello', 'friends']
    print("--------------")

    # Tests Problem 1: Find Ngrams
    world_ngrams, friend_ngrams = find_ngrams(world, 2), find_ngrams(friend, 2)
    longer_ngrams = find_ngrams(world+world, 3)
    print(world_ngrams) ## should print ['hello world', 'world hello']
    print(friend_ngrams) ## should print ['hello friends']
    print(longer_ngrams) ## should print ['hello world hello', 'world hello hello', 'hello hello world', 'hello world hello']
    print("--------------")
    # Tests Problem 2: Get frequency
    world_word_freq, world_ngram_freq = compute_frequencies(world), compute_frequencies(world_ngrams)
    friend_word_freq, friend_ngram_freq = compute_frequencies(friend), compute_frequencies(friend_ngrams)
    print(world_word_freq) ## should print {'hello': 2, 'world': 1}
    print(world_ngram_freq) ## should print {'hello world': 1, 'world hello': 1}
    print(friend_word_freq) ## should print {'hello': 1, 'friends': 1}
    print(friend_ngram_freq) ## should print {'hello friends': 1}
    print('------------')
    # Tests Problem 3: Similarity
    word_similarity = get_similarity_score(world_word_freq, friend_word_freq)
    ngram_similarity = get_similarity_score(world_ngram_freq, friend_ngram_freq)
    print(word_similarity) ## should print 40
    print(ngram_similarity) ## should print 0
    print("-----------'")
    # Tests Problem 4: Most Frequent Word(s)
    freq1, freq2 = {"hello":5, "world":1}, {"hello":1, "world":5}
    most_frequent = compute_most_frequent(freq1, freq2)
    print(most_frequent) ## should print ["hello", "world"]
    print("-----------")
    # Tests Problem 5: Find closest matching artist
    test_directory = "tests/student_tests/"
    artist_to_songfiles_map = {
    "artist_1": [test_directory + "artist_1/song_1.txt", test_directory + "artist_1/song_2.txt", test_directory + "artist_1/song_3.txt"],
    "artist_2": [test_directory + "artist_2/song_1.txt", test_directory + "artist_2/song_2.txt", test_directory + "artist_2/song_3.txt"],
    }
    mystery_lyrics = load_file(test_directory + "mystery_lyrics/mystery_1.txt") # change which number mystery lyrics (1-5)
    print(find_closest_artist(artist_to_songfiles_map, mystery_lyrics)) # should print ['artist_1']
