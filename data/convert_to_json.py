import csv
import json
import os

def convert_tsv_to_json(tsv_file_path):
    json_file_path = os.path.splitext(tsv_file_path)[0] + '.json'
    
    with open(tsv_file_path, 'r', newline='') as tsv_file:
        #the tsv file does not have headers
        tsv_reader = csv.reader(tsv_file, delimiter='\t')
        data = []
        
        for row in tsv_reader:
            data.append({
                'source': row[0],
                'target': row[1]
            })
        
    with open(json_file_path, 'w') as json_file:
        #We only are interested in the first two columns, the third one is not needed
        json.dump(data, json_file, indent=4)
    
        
    

if __name__ == "__main__":
    convert_tsv_to_json('./deu.txt')
    convert_tsv_to_json('./fra.txt')
    convert_tsv_to_json('./spa.txt')
