def replace_words_in_binary_file(file_path, word_list, replace_with):
    with open(file_path, 'rb') as file:
        file_content = file.read()
    for word in word_list:
        file_content = file_content.replace(word.encode(), replace_with.encode())
    with open(file_path, 'wb') as file:
        file.write(file_content)