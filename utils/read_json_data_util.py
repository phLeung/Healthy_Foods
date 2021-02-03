#!/usr/bin/python3
import json
import os
import errno

class InvalidDataErrorHandler(Exception):
    #Raised when an invalid json data has been caught
    """
    json_data -- input  json data which caused the error
    message -- explanation of error
    """
    def __init__(self,json_data,message="JSON data is invalid or not properly formatted"):
        self.json_data = json_data
        self.message = message
        super().__init__(self.message)


#function to read json file
def read_from_file(json_name):
    #add the data directory containing json data to the utils directory
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','data')
    #normalize path to data directory containing json data
    json_path_normalized = os.path.normpath(json_path)
    return json_path_normalized + '/' + json_name + '.json'


def get_json_data(data_name):
    data_map = {}
    if data_name not in data_map:
        data = read_from_file(data_name)
        data_map[data_name] = data
    return data_map[data_name]

"""
param: json file name
parse json file
"""
def parse_json_data(file_name):
    if not os.path.exists(file_name):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT),file_name)
    with open(file_name,'r') as json_data:
        try:
            data = json.load(json_data)#parse json data from file
        except InvalidDataErrorHandler as invalid_data:
            print(invalid_data) #invalid json data
        else:
            return data #valid json data

def validate_json(json_data):
    if not os.path.exists(json_data):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENt),json_data)
    with open(json_data,'r') as data:
        try:
            json.load(json_data)
        except ValueError as error:
            return False
        else:
            return True

def json_validator(json_name):
    json_data = get_json_data(data_name)
    return validate_json(json_data)

def read_json_data(data_name):
    json_file = get_json_data(data_name)
    return parse_json_data(json_file)
