import constants
import os
import re
import subprocess
from errors import *


def set_work_dir(work_dir=os.environ["WORK_DIR"]):
    if not work_dir.endswith('/'):
        work_dir = work_dir + '/'

    return work_dir


def parse_ls_result(path):
    ls_result = subprocess.run(['ls', '-lh', path],
                               capture_output=True,
                               text=True)
    if ls_result.stderr:
        raise APIError(ls_result.stderr)

    ls_string = ls_result.stdout
    ls_parts = ls_string.split('\n')

    return create_ls_data_json(ls_parts)

def create_ls_data_json(ls_response_lines):
    file_info_dictionaries = []
    for line in ls_response_lines:
        file_info_dict = {}

        if re.search(constants.FILE_SIZE_REGEX, line):
            file_info_dict["file_size"] = re.search(constants.FILE_SIZE_REGEX,
                                                    line).group(1)

        if re.search(constants.FILE_OWNER_REGEX, line):
            file_info_dict["file_owner"] = re.search(constants.FILE_OWNER_REGEX,
                                                     line).group(1)

        if re.search(constants.FILE_NAME_REGEX, line):
            file_info_dict["file_name"] = re.search(constants.FILE_NAME_REGEX,
                                                    line).group(1)

        if re.search(constants.FILE_TYPE_REGEX, line):
            file_info_dict["file_type"] = re.search(constants.FILE_TYPE_REGEX,
                                                    line).group(1)
        else:
            if bool(file_info_dict):
                file_info_dict["file_type"] = 'folder'

        if bool(file_info_dict):
            file_info_dictionaries.append(file_info_dict)

    return file_info_dictionaries

def parse_file_information(path):
    file_contents = subprocess.run(['cat', path],
                                   capture_output=True,
                                   text=True)
    if file_contents.stderr:
        return parse_ls_result(path)
    else:
        files_info_array = parse_ls_result(path)
        return create_cat_data_json(files_info_array, file_contents.stdout)

def create_cat_data_json(files_info_array, file_stdout):
    files_dict = files_info_array[0]
    files_dict["file_contents"] = file_stdout
    return [files_dict]
