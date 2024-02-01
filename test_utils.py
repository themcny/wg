import sys
import os
from flask import jsonify
from utils import *

def test_set_work_dir():
    assert set_work_dir("files/no/trailing/slash") == "files/no/trailing/slash/", "Should add trailing slash if none in given path"
    assert set_work_dir("files/has/trailing/slash/") == "files/has/trailing/slash/", "Should not modifypath with trailing slash"

LS_DATA = ["total 16", "drwxr-xr-x  4 owner  staff   128B Jan 28 16:06 bar", "-rw-r--r--  1 owner  staff    13B Jan 28 15:58 foo1.txt", "-rw-r--r--  1 owner  staff    15B Jan 28 16:06 foo2.txt"]
LS_DATA_RESPONSE = [{"file_name":"bar","file_owner":"owner","file_size":"128B","file_type":"folder"},{"file_name":"foo1.txt","file_owner":"owner","file_size":"13B","file_type":".txt"},{"file_name":"foo2.txt","file_owner":"owner","file_size":"15B","file_type":".txt"}]
CAT_LS_DATA = ["-rw-r--r--  1 owner  staff    13B Jan 28 15:58 /Users/owner/testroot/foo1.txt"]
CAT_LS_DATA_RESPONSE = [{"file_owner":"owner","file_size":"13B","file_type":".txt"}]
CAT_FILE_DATA = "foo number 1\n"
CAT_DATA_RESPONSE = [{"file_contents":"foo number 1\n","file_owner":"owner","file_size":"13B","file_type":".txt"}]

def test_create_ls_data_json():
    assert create_ls_data_json(LS_DATA) == LS_DATA_RESPONSE
    assert create_ls_data_json(CAT_LS_DATA) == CAT_LS_DATA_RESPONSE

def test_create_cat_data_json():
    assert create_cat_data_json(CAT_LS_DATA_RESPONSE, CAT_FILE_DATA) == CAT_DATA_RESPONSE

if __name__ == "__main__":
    test_set_work_dir()
    test_create_ls_data_json()
    test_create_cat_data_json()
    print("Everything passed")

