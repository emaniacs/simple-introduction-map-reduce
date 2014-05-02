from main import TARGET_FILE, OUTPUT_DIR
from re import sub
from os import remove

PATTERN = r'[^a-zA-Z]+'
OUTPUT_FILE = '{0}/mapper.output'.format(OUTPUT_DIR)


def main():
    with open(TARGET_FILE, 'r') as f:
        words = f.read()
        clean_words = sub(PATTERN, ' ', words)
        for word in clean_words.split(' '):
            map_it (word)

def map_it(word):
    if len(word) > 0:
        with open(OUTPUT_FILE, 'a+') as f:
            string = '{0},{1}\n'.format(len(word), word)
            f.write(string)

if __name__ == '__main__':
    try:
        # remove output if exists
        remove(OUTPUT_FILE)
    except:
        pass

    main()
