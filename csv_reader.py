import csv
def formatResult(name, result):
    result_List =[]
    count = 3
    while count < len(result)-1:
      constituency = {
			  'name': name[count],
			  'first': {
				  'provisional': result[count]
				  },
			  'second': {
				  'provisional': result[count + 2],
				  'previous': result[count + 3]
			  }
        }      
      count += 4
      result_List.append(constituency)
    return result_List


def read_csv():    
 with open('btw17_kerg.csv','rt', encoding = 'utf-8') as db:
        reader = csv.reader(db, delimiter=';')
        columns = []
        states = []
        line_count_id = 0
        for row in reader:
           if reader.line_num == 3:
              columns = row
           elif reader.line_num >3 and row[0] != '':
            state = {
              'id': row[0],
              'name': row[1],
              'belongs_to': row[2],
              'parties': formatResult(columns, ro w)
            }
            states.append(state)
            line_count_id += 1
        return states

