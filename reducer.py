import grouper, config
import os

OUTPUT_FILE = '{0}/reducer.output'.format(config.OUTPUT_DIR)

def reducer():
    output = open(OUTPUT_FILE, 'a+')

    for fl in os.listdir(grouper.OUTPUT_DIR):
        if fl.endswith('.output'):
            total = 0
            with open(grouper.OUTPUT_DIR+'/'+fl) as f:
                words = f.read()
                # remove list with empty string
                total = len(filter(None, words.split(',')))
            # print(fl + ' has ' + str(total))
            output.write('{0} has {1} word(s)\n'.format(fl, total))

    output.close()

if __name__ == '__main__':
    reducer()
