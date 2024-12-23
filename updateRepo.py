import sys
import json
import time

plugin_name = sys.argv[1].strip()
new_version = sys.argv[2].strip()
repo_json = []

with open('repo.json') as repo_data:
    repo_json = json.load(repo_data)
    repo_data.close()

for plugin in repo_json:
    if plugin['InternalName'] == plugin_name:
        if plugin['AssemblyVersion'] == plugin_json['AssemblyVersion']:
            print('You forgot to update the version number!')
            exit(1)
        else:
            plugin['AssemblyVersion'] = new_version
            plugin['LastUpdate'] = int(time.time())
        
with open('repo.json', 'w') as save_data:
    json.dump(repo_json, save_data, indent=4)
    
print("Updated %s to version %s" % (plugin['InternalName'], plugin_json['AssemblyVersion']))
