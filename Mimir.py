import urllib.request
import xml.etree.ElementTree


def remove_tags(text):
    return ''.join(xml.etree.ElementTree.fromstring(text).itertext())


def find_solution(state_string):
    """Searches local server for correct solution to presented state string and returns solution move-set as a list"""
    p = 'http://127.0.0.1:8080/' + state_string
    with urllib.request.urlopen(p) as solution_url:
        read_data = solution_url.read()

    read_data = remove_tags(read_data)

    print(read_data)

    solution_move_set = read_data.split(' ')

    solution_move_set = [s for s in solution_move_set if len(s) == 2]

    return solution_move_set
