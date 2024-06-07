class FileUtils:

    @staticmethod
    def read_file(path: str, *encoding: str):
        with open(path, "r", encoding='utf-8') as f:
            return f.read()

    @staticmethod
    def read_line_file(path: str, *encoding: str):
        with open(path, "r", encoding='utf-8') as f:
            line = f.readline()
            while line:
                print(line)
                line = f.readline()

    @staticmethod
    def read_lines_file(path: str, *encoding: str):
        with open(path, "r", encoding='utf-8') as f:
            lines = f.readlines()
            print(lines)

    @staticmethod
    def write_sting_file(path: str, content: str, *encoding: str):
        with open(path, "w", encoding='utf-8') as f:
            f.write(content)

    @staticmethod
    def write_list_file(path: str, content: list, *encoding: str):
        with open(path, "w", encoding='utf-8') as f:
            for item in content:
                f.write(item)

    @staticmethod
    def append_file(path: str, content: str, *encoding: str):
        with open(path, 'a', encoding='utf-8') as f:
            f.writelines(content)


content_1 = FileUtils.read_file('test.txt')
print('1 output.-------------')
print(content_1)
print('\n2 output.-------------')
FileUtils.read_line_file('test.txt')
print('\n3 output.-------------')
FileUtils.read_lines_file('test.txt')
print('\n4 output.-------------')
FileUtils.append_file("test.txt", "\nNew text.")
FileUtils.read_line_file('test.txt')
print('\n5 output.-------------')
FileUtils.write_sting_file('test2.txt', 'Hello, test2.')
print(FileUtils.read_file('test2.txt'))
print('\n6 output.-------------')
FileUtils.write_list_file("test3.txt", ['first', '\nsecond', '\nthird'])
FileUtils.read_lines_file("test3.txt")