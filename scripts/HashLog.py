import hashlib


def read_log_file(old_log_file_path, new_log_file_path):
    with open(new_log_file_path, 'w') as new_file:
        hash_set = set()
        with open(old_log_file_path, 'rt', 1) as old_file:
            for line in old_file:
                temp_line = ""
                if line[0] == '(':
                    ind = line.find(')')
                    temp_line = line[ind + 2:]
                hash_keeper = hashlib.md5()
                hash_keeper.update(temp_line.encode('utf-8', 'strict'))
                current_digest = hash_keeper.digest()
                if current_digest not in hash_set:
                    hash_set.add(current_digest)
                    new_file.write(line)


old_log_file_path = 'm:\Projects\PythonLearning\log_example.txt'
new_log_file_path = 'm:\Projects\PythonLearning\clean_log.txt'
read_log_file(old_log_file_path, new_log_file_path)
