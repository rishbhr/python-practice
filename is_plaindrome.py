#python
# input a bunch of palidromes and 
# number and list of words
# list of words that are palindromes

class verify_palindrome:
    
    #number of words: 4
    #word: refer, revolt, palindrome, rotator
    #response: refer, rotator

    # O(nm)
    # O(n^2)
    # O(n)

    def is_palindrome(word_count, word_list):
        #[0,1,2,3]
        is_plaindrome = []

        reverse_words = []

        # r e v e r

        for word in word_list:
            if word == word[::-1]:
                is_plaindrome.append(word)
            
        return is_plaindrome
        
    plaindrome_list = is_palindrome(4,["refer", "revolt", "palindrome", "rotator"])
    print(plaindrome_list)