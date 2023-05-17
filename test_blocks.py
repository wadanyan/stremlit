from barfi import Block

#dataの要素を変数名にしてfro文でnodeを作成
#あとは変数な変数の種類をまとめて関数にすればおけ
#必要な要素について
#pipeline、taskなどのmetadata
#param.name
#data = ['apple', 'banana' , 'pine']
process_blocks = []
process_blocks_names = []
def create_block(blockname: str, output_paramnamelist: list, input_paramnamelist: list):

    if not blockname in process_blocks:
        globals()[blockname] = Block(name=blockname)
        #globals()[blockname].add_output(name=blockname)
        for i in output_paramnamelist:
            globals()[blockname].add_output(name=' '+i)

        for i in input_paramnamelist:
            globals()[blockname].add_input(name=i)
    process_blocks_names.append(blockname)
    process_blocks.append(globals()[blockname])

#process_blocks = [feed, result, mixer, splitter]
#process_blocks = [apple, banana, pine]
process_blocks2 = []
