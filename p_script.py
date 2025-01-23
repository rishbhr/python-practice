#python
class Solution:
    def my_function():
        # given int array return an array such that your answer of index i 
        # i = [1,2,3]
        # ans = [6,3,2] product of all elements 
        
        #iter thru array
        # [i[2]*i[1], i[2]*i[0], i[1]*i[0]]

        
        #3*2
        #last num, and * with the prior
        #if index = 0

        #last element of array * element before
        #if element is at 0 
        #break

        x = [1,2,3]
        
        res = [1] * (len(x))

        prefix = 1

        for i in range(len(x)):
            res[i] = prefix
            # print(res[i])
            prefix *= x[i]
            print(prefix)

        postfix=1
        print("postfix")

        for i in range(len(x)- 1, -1, -1):
            res[i] *= postfix
            # print(res[i])
            postfix *= x[i]
            print(postfix)

        print(res)

    my_function()




# input a bunch of palidromes and 
# number and list of words
# list of words that are palindromes

class verify_palindrome:
    
    #number of words: 4
    #word: refer, revolt, palindrome, rotator
    #response: refer, rotator

    
    def is_palindrome(int: word_count, list<string>: word_list):
        
        
        
        return None
        
    
    
    
    
    
    is_palindrome(4,list["refer", "revolt", "palindrome", "rotator"])



 if word_count != len(word_list):
            return None

            
        for i in word_count:
            word_len = len(word)

            # access the list at the index of i from word count
            word = word_list[i]
            
            #r, e, v, v, e, r
            for letter in word:
                if letter == word[word_len-1]:
                    word_len -= 1
            
            if word_len == 0:
                is_plaindrome.append(word)
 if word_count != len(word_list):
            return None

            
        for i in word_count:
            word_len = len(word)

            # access the list at the index of i from word count
            word = word_list[i]
            
            #r, e, v, v, e, r
            for letter in word:
                if letter == word[word_len-1]:
                    word_len -= 1
            
            if word_len == 0:
                is_plaindrome.append(word)