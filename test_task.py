import csv

def read_csv(goods_list : list) :
    with open('test.csv') as file :
        file_reader = csv.DictReader(file)
        name_indexer = dict((d['good_name'], i) for i, d in enumerate(goods_list))
        
        for row in file_reader :
            if not any(d.get('good_name') == row.get('good_name') for d in goods_list) :
                row['cost'] = int(row['cost'])*int(row['quantity'])
                row['quantity'] = int(row['quantity'])
                goods_list.append(row)
            else :
                index = name_indexer.get(row.get('good_name'), -1)
                goods_list[index]['quantity'] += int(row.get('quantity'))
                goods_list[index]['cost'] += int(row['cost'])*int(row['quantity'])
                
    return goods_list

    
goods = read_csv([])

for item in goods :
    print(item['good_name'] + ' ' + str(item['quantity']) + ' ' + str(item['cost']))
