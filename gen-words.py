from random import randint

words = list(set([word.strip().lower() for word in open('words.txt', 'r')]))
words.sort()

left = ['q','w','e','r','t','a','s','d','f','g','z','x','c','v','b']
right = ['y','u','i','o','p','h','j','k','l','n','m']

def lrdist(word):
    """Given a word, returns its distribution in terms of the percentage
    of characters that one would have to type with the left hand and with the
    right in a (leftPercent, rightPercent) tuple.
    """
    left_total = 0
    right_total = 0
    word_length = len(word)

    for char in word:
        if char in left:
            left_total += 1
        elif char in right:
            right_total += 1

    return (left_total/word_length, right_total/word_length)


def alternates(word):
    """Returns true if each consecutive character in the given word alternates
    between the left and right hands.
    """
    last_key = None

    for char in word:
        if char in left:
            if last_key == None or last_key == 'r':
                last_key = 'l'
            else:
                return False
        elif char in right:
            if last_key == None or last_key == 'l':
                last_key = 'r'
            else:
                return False

    return True


alternating_words = [word for word in words if alternates(word) and len(word) > 2]
left_alt_words = [word for word in alternating_words if word[0] in left]
right_alt_words = [word for word in alternating_words if word[0] in right]

with open('alternating-words.txt', 'w') as f:
    f.write('\n'.join(alternating_words) + '\n')

with open('left-words.txt', 'w') as f:
    f.write('\n'.join(left_alt_words) + '\n')

with open('right-words.txt', 'w') as f:
    f.write('\n'.join(right_alt_words) + '\n')