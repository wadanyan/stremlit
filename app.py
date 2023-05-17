from barfi import st_barfi, barfi_schemas
import streamlit as st
from test_blocks import process_blocks
from test_blocks import process_blocks_names
from test_blocks import create_block
from create_schema import read_yamlfile
import pickle
from typing import Dict

from barfi import Block
import ast
import json
import glob
import yaml
from pathlib import Path

def app():

    def get_yamlefile():

        filenames = []
        path = Path('/src/yamlsample/')
        for file in path.glob("*.yaml"):
            filenames.append(file)
            #filenames.append(file.name)
        create_schema(filenames)
        read_yamlfile(filenames)
        
    def create_schema(filenames: list):
        for i in filenames:
            #data = yaml.safe_load('src/yamlsample/' + i)
            with open(i) as f:
                paramnamelist = []
                kind_names = []
                block_name = ''
                #st.code(f.read(), language="yaml")
                data = yaml.safe_load(f)

                for param in data['spec']['params']:  
                    paramnamelist.append(param['name'])


                if  data['kind'] not in kind_names:
                    kind_names.append(data['kind'])


                try:
                    if not data['metadata']['name'] in process_blocks_names:
                        st.write('run')
                        block_name = data['metadata']['name']
                        if data['kind'] == 'Task':
                            create_block(block_name, [], paramnamelist)
                        else:
                            create_block(block_name, paramnamelist, paramnamelist)
                except:
                    pass
            
                try:
                    if not data['metadata']['generateName'] in process_blocks_names:
                        st.write('run')
                        block_name = data['metadata']['generateName']
                        create_block(block_name, paramnamelist, [])
                except:
                    pass

    def save_schema(schema_name: str, schema_data: Dict):

        with open('schemas.barfi', 'wb') as handle_write:
            
            with open('new_schema.txt','r') as hr1:
                output = hr1.read()

                pickle.dump(json.loads(output), handle_write, protocol=pickle.HIGHEST_PROTOCOL)
    
    save_schema(schema_name='schema-2',schema_data='startschemas.barfi')
    get_yamlefile()

    barfi_schema_name = st.selectbox(
        'Select a saved schema to load:', barfi_schemas())

    compute_engine = st.checkbox('Activate barfi compute engine', value=False)


    process_blocks_split = 0
    st.write(st_barfi(base_blocks=process_blocks, compute_engine=compute_engine, load_schema=barfi_schema_name))
        #schemanameを表示する。
    
    if 'count' not in st.session_state:
        st.session_state["count"] = 0
  
    if st.button("カウント"):
        st.session_state["count"] += 1
        
    
    st.write("カウント", st.session_state["count"])
        


def load_schemas():
    try:
        with open('schemas.barfi', 'rb') as handle_read:
            schemas = pickle.load(handle_read)
    except FileNotFoundError:
        chemas = {}

    schema_names = list(schemas.keys())
    return {'schema_names': schema_names, 'schemas': schemas}        
