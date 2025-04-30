# Python script to parse CISI.ALL and generate JSON
import json

def parse_cisi(file_path):
    documents = []
    with open(file_path, 'r') as file:
        doc = {}
        for line in file:
            line = line.strip()
            if line.startswith('.I'):
                if doc:
                    documents.append(doc)
                doc = {'ID': line[2:].strip(), 'Title': '', 'Author': '', 'Abstract': '', 'CrossRefs': []}
            elif line.startswith('.T'):
                section = 'Title'
            elif line.startswith('.A'):
                section = 'Author'
            elif line.startswith('.W'):
                section = 'Abstract'
            elif line.startswith('.X'):
                section = 'CrossRefs'
            else:
                if section == 'CrossRefs':
                    # Parse the .X section into structured data
                    parts = line.split()
                    if len(parts) == 3:
                        doc['CrossRefs'].append({
                            'ReferencedID': int(parts[0]),
                            'Weight': int(parts[1]),
                            'Score': int(parts[2])
                        })
                elif section in doc:
                    doc[section] += line + ' '                
        if doc:
            documents.append(doc)
    return documents

# Save parsed data to JSON
file_path = 'datasets/CISI/CISI.ALL'
parsed_data = parse_cisi(file_path)
with open('cisi_data.json', 'w') as json_file:
    json.dump(parsed_data, json_file, indent=4)