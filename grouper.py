import config
import mapper


OUTPUT_DIR = '{0}/grouper'.format(config.OUTPUT_DIR)

def grouper():
    with open(mapper.OUTPUT_FILE, 'r') as f:
        for line in f:
            words = line.split(',')
            length = words[0]
            # remove newline, inserted by mapper
            word = words[1].replace('\n', '')

            output_file = '{0}/sheet-{1}.output'.format(OUTPUT_DIR, length)
            sheet = open(output_file, 'a+')
            sheet.write(word + ',')
            sheet.close()

if __name__ == '__main__':
    grouper()
