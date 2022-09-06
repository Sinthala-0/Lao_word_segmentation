
words_list = ["ຂ້ອຍ","ເຂົ້າ","ກັບ","ລັບ","ບ້ານ","ກິນ","ເຂົ້າ", "ນອນ", 'ຫຼີ້ນ', 'ຕ້ອງ', 'ໄປ', 'ມາ', 'ໃສ', 'ເກມ', 'ສາວ', 'ແມ່ນ','ຢູ່',".",",",
'ສະບາຍດີ', 'ໝູ່', 'ເພື່ອນ', 'ທຸກ', 'ຄົນ', 'ພ້ອມ', 'ກັນ', 'ແລ້ວ', 'ຫຼື', 'ຍັງ','ທີ່','ຈະ','ເຮັດ','ວຽກ','ກັບ','ພວກ','ເຮົາ','ໃນ','ການ','ຊ່ວຍ', 
'ພັດທະນາ', 'ທັກສະ', 'ພາສາອັງກິດ', 'ໃຫ້', 'hello']

import string 

def counter_decorator(func):
    def wrapper(*args, **kwargs):
        # getting result
        words = func(*args, **kwargs) 
        print(words)
        # output
        print(f"There are {len(words)} words.")
        
    return wrapper;


# Essentail function for the parser
@counter_decorator
def parser(text):
    tokens = []
    boundary = 0
    while boundary < len(text):
        # Prepare to store the longest word matches from each loop
        max_word = ""
        # Loops:
        for j in range(boundary, len(text)):
            # Attemping to match each word from the string to a word from the words_list
            temp_word = text[boundary:j+1]
            if temp_word in words_list and len(temp_word) > len(max_word):
                max_word = temp_word
            # Numbers:
            elif str(temp_word).isdigit():
                max_word = temp_word
            # Signs:
            if temp_word in string.punctuation or temp_word == " ":
                max_word = temp_word
            # English letters
            if temp_word in string.ascii_letters:
                max_word = temp_word
            
        # Changing the boundary of word and adding a word to the tokens list
        boundary += len(max_word)
        tokens.append(max_word)

    # Merge english word
               
        
    # Removing spaces
    while (" " in tokens or '\n' in tokens):
        tokens.remove(" ")

    return tokens


def main(): 
    text = "ສະບາຍດີໝູ່ເພື່ອນທຸກຄົນພ້ອມກັນແລ້ວ ຫຼືຍັງທີ່ຈະເຮັດ, ວຽກກັບພວກເຮົາໃນການຊ່ວຍພັດທະນາທັກສະພາສາອັງກິດໃຫ້ກັບທຸກຄົນ123ຄົນ ຄົນ ຄົນ !!!!"
    parser(text)
    



if __name__ == '__main__':
    main()








