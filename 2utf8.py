import os
import codecs
import chardet

# Function to detect the encoding of a file
def detect_encoding(filename):
    with open(filename, 'rb') as file:
        contents = file.read()
    result = chardet.detect(contents)
    return result['encoding']

# Function to convert a file to UTF-8 encoding
def convert_encoding(filename, new_encoding='UTF-8'):
    current_encoding = detect_encoding(filename)
    with codecs.open(filename, 'r', current_encoding, errors='ignore') as file:
        file_content = file.read()
    with codecs.open(filename, 'w', new_encoding) as file:
        file.write(file_content)
    return

# Convert all LRC files in a directory
def convert_lrc_files_in_dir(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.lrc'):
                filename = os.path.join(root, file)
                convert_encoding(filename)
    return

# Usage example
convert_lrc_files_in_dir('G:\\Music')
convert_lrc_files_in_dir('G:\\Music\\VipSongsDownload')
