import hashlib


def read_log_file(old_log_file_path):
    # I decided to use string here to write the result to file
    # in  one iteration
    lines = ""
    hash_set = set()
    with open(old_log_file_path) as file:
        for line in file:
            if line[0] == '(':
                ind = line.find(')')
                line = line[ind + 2:]
            hash_keeper = hashlib.md5()
            hash_keeper.update(line.encode('utf-8', 'strict'))
            current_digest = hash_keeper.digest()
            if current_digest not in hash_set:
                hash_set.add(current_digest)
                lines += line
    return lines


old_log_file_path = 'm:\Projects\PythonLearning\log_example.txt'
new_log_file_path = 'm:\Projects\PythonLearning\clean_log.txt'
with open(new_log_file_path, 'w') as the_file:
    the_file.write(read_log_file(old_log_file_path))
