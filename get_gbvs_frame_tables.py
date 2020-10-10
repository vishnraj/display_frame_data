import requests, sys, string, fileinput, json, argparse
from lxml import html
from bs4 import BeautifulSoup

domain_name = 'https://www.dustloop.com'
gbvs_wiki_path = '/wiki/?title=GBVS/'

current_roster = ['Gran', 'Katalina', 'Charlotta', 'Lancelot', 'Percival', 'Ladiva', 'Metera', 'Lowain', 'Ferry', 'Zeta', 'Vaseraga', 'Beelzebub', 'Narmaya', 'Djeeta']

columns = ['Version', 'Damage', 'Guard', 'Startup', 'Active', 'Recovery', 'On Block', 'On Hit', 'Attribute', 'Level', 'Blockstun', 'Hitstun', 'Untech', 'Hitstop', 'Invul']

character_to_frame_data = {}

def get_character_frame_data_table(character_name):
  url = domain_name + gbvs_wiki_path + character_name + '/Frame_Data'
  print('Getting ' + character_name + ' frame data table at ' + url)
  r = requests.get(url)
  soup = BeautifulSoup(r.content, 'html.parser')

  normal_moves = soup.find('span', {'id' : 'Normal_Moves'})
  moves_table = normal_moves.parent.findNext('table').findNext('tbody').findChildren()

  rows = []

  for e in moves_table:
    r = e.find('th', {'rowspan' : '2'}) 
    if (r != None):
      rows.append(r.parent)

  character_to_frame_data[character_name] = []
  combo = 1
  for r in rows:
    i = 0
    c = {}
    version = ''
    for e in r.find_all(recursive=False):
      text = ''
      if (i == 0):
        if e.string == None:
          text = 'Auto Combo ' + str(combo)
          combo += 1
        else:
          text = str(e.string)

        version = text.rstrip()
        c[version] = {}
      else:
        if (e.string == '-\n'):
          text = 'zzz'
        else:
          text = str(e.string)

        c[version][columns[i]] = text.rstrip()
      i += 1
      
    character_to_frame_data[character_name].append(c)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-o', '--outfile', help='json file to write data out to', type=str)
  args = parser.parse_args()

  for c in current_roster:
    get_character_frame_data_table(c)

  filename = args.outfile
  print('Writing to ' + filename)
  with open(filename, 'w') as file:
    json.dump(character_to_frame_data, file, indent=2)
