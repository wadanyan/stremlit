import streamlit as st
import json
import yaml
from pathlib import Path


def read_yamlfile(filenames: list):
    for filename in filenames:
        with open(filename, 'r') as r:
            data = yaml.safe_load(r)
            paramnamelist = []
            for param in data['spec']['params']:  
                paramnamelist.append(param['name'])
            
            
            if 'name' in data['metadata']:
                st.write(data['metadata']['name'])
                st.write('input: ' + str(paramnamelist))

                if 'tasks' in data['spec']:
                    st.write('output: ' + str(paramnamelist))

            elif 'generateName' in data['metadata']:
                st.write(data['metadata']['generateName'])
                st.write('output : ' + str(paramnamelist))
    """ with open("schematemplete/sample.txt", 'a')as w:
        path = Path('/src/schematemplete/')
        for file in path.glob("*.txt"):
            with open(file , 'r') as r:
                test = r.readlines()
                test.insert(3, 'dfs/n')
                st.write(test)
                w.writelines(test) """

            
def create_schema():
    with open('schemas.barfi', 'wb') as handle_write:
            
            with open('new_schema.txt','r') as hr1:
                output = hr1.read()

                pickle.dump(json.loads(output), handle_write, protocol=pickle.HIGHEST_PROTOCOL)