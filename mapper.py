from main import TARGET_FILE, OUTPUT_DIR
from re import sub
from os import remove

PATTERN = r'[^a-zA-Z]+'
OUTPUT_FILE = '{0}/mapper.output'.format(OUTPUT_DIR)


def mapper():
    with open(TARGET_FILE, 'r') as f:
        words = f.read()
        clean_words = sub(PATTERN, ' ', words)

        output = open(OUTPUT_FILE, 'a+')
        for word in clean_words.split(' '):
            if len(word) > 0:
                string = '{0},{1}\n'.format(len(word), word)
                output.write(string)
        
        output.close()

if __name__ == '__main__':
    mapper()
