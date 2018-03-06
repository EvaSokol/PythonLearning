import hashlib


class HashLog(object):

    def create_set(self):
        lines = {"fred: I said something",
                    "bob: Oh I see",
                    "(10:30:28) fred: I said something",
                    "(10:30:29) bob: Oh I see",
                    "fred: Ah, the text was repeated",
                    "bob: yes it was",
                    "(Wed 26 10:30:28) bob: Hello Fred!",
                    "(Wed 26 10:30:28) fred: I said something",
                    "(Wed 26 10:30:29) bob: Oh I see",
                    "(Wed 26 10:31:20) fred: Ah, the text was repeated",
                    "(Wed 26 10:31:24) bob: yes it was"}
        return lines

    def read_file(self):
        lines = set()
        with open('m:\Projects\PythonLearning\log_example.txt') as file:
            for line in file:
                lines.add(line)
        # print(lines)
        return lines

    print("initialization")


hash_log = HashLog()
old_lines = hash_log.create_set()
set_of_hash = set()
# logfile=open(..... # you can fill this in
for line_of_text in old_lines:
    m = hashlib.md5()
    m.update(line_of_text.encode('utf-8', 'strict'))
    digest = m.digest()  # returns a string representation of the hash code
                # ... do something here?
    set_of_hash.add(digest)
print(set_of_hash)
print("set:", hash_log.read_file())


