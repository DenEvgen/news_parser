from urllib import request
import file
from parser import Parser
from file import File

if __name__ == '__main__':
    can_not_do_it = True
    while can_not_do_it:
        can_not_do_it = False
        try:
            url = input("Enter your link:  ").strip()
            content = request.urlopen(url)
            my_parser = Parser(content)
            header = my_parser.parse_header()
            paragraphs = my_parser.parse_paragraphs()
            new_file = File(url)
            path = new_file.create_file_path()
            file.write_to_file(path, header, paragraphs)
        except ValueError:
            print("You entered an invalid url.\nPlease repeat...")
            can_not_do_it = True


