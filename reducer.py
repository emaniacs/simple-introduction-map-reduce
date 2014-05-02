import grouper, config
import os, sys

OUTPUT_FILE = '{0}/reducer.output'.format(config.OUTPUT_DIR)

def reducer():
    ret = True

    try:
        output = open(OUTPUT_FILE, 'a+')

        for fl in os.listdir(grouper.OUTPUT_DIR):
            if fl.endswith('.output'):
                total = 0
                with open(grouper.OUTPUT_DIR+'/'+fl) as f:
                    words = f.read()
                    words_split = words.split(',')

                    # remove list with empty string
                    total = len(filter(None, words_split))
                # print(fl + ' has ' + str(total))
                output.write('({0}): There are {1} word(s) that have {2} characters.\n'.format(fl, total, len(words_split[0])))

        output.close()
    except Exception as e:
        print(e)
        ret = False

    return ret

if __name__ == '__main__':
    sys.exit(reducer())
