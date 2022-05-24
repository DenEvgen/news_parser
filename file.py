import re
import os
from pathlib import Path
from typing import List

from text_format import line_separator


def write_to_file(path_to_write: Path, header: List[str], paragraph: List[str]):
    candidate_to_txt = str(path_to_write) + "/" + header[0]
    with open(candidate_to_txt, 'w') as txt:
        for line in header:
            line_list = line_separator(line)
            for line in line_list:
                txt.write(line + '\n')

        for i in paragraph:
            txt.write('' + '\n')
            line_list = line_separator(i)
            for i in line_list:
                txt.write(i + '\n')


class File:
    def __init__(self, link):
        self.link = re.sub(r'http(.*?)//', '', link)

    def create_file_path(self):
        cur_dir = Path(os.getcwd())
        if self.link[-1] == "/":
            self.link = self.link[:-1]
        updated_link = '/'.join(self.link.split("/")[:-1])
        output_folder = updated_link
        final_dir = cur_dir.joinpath(output_folder)

        if not os.path.exists(final_dir):
            os.makedirs(final_dir)
        return final_dir


