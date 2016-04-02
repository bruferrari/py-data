import os

def extract_entity_name(filename):
    return filename.split('.')[0]

def read_lines(filename):
    _file = open(os.path.join('data/meta-data', filename), 'rt')
    data = _file.read().split('\n')
    _file.close()
    return data

def read_metadata(filename):
    metadata = []
    for column in read_lines(filename):
        if column:
            metadata.append(tuple(column.split('\t')[:3]))
    return metadata

def prompt():
    print('\nWhat do you looking for?')
    print('(l) List entities')
    print('(a) Show attributes of an entity')
    print('(r) Show references about entity')
    print('(x) Exit')
    return input()

def main():
    # dict entity name -> attrb
    meta = {}
    # dict id -> entity name
    keys = {}
    # dict of relationships between entities
    relationships = {}

    for meta_file in os.listdir('data/meta-data'):
        table_name = extract_entity_name(meta_file)
        attrb = read_metadata(meta_file)
        identifier = attrb[0][0]

        meta[table_name] = attrb
        keys[identifier] = table_name

    for key, val in meta.items():
        for col in val:
            if col[0] in keys:
                if not col[0] == meta[key][0][0]:
                    relationships[key] = keys[col[0]]

    option = prompt()
    while option !=  'x':
        if option == 'l':
            for entity_name in meta.keys():
                print(entity_name)
        elif option == 'a':
            entity_name = input('Give the name of entity: ')
            for col in meta[entity_name]:
                print(col)
        elif option == 'r':
            entity_name = input('Give the name of entity: ')
            try:
                print(relationships[entity_name])
            except KeyError as error:
                print('Key {} have no relationships'.format(error))
        else:
            print('not exists!\n')
        option = prompt()

if __name__ == '__main__':
    main()
