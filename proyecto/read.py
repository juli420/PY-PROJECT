import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter= ',')
        header = next(reader)
        data = []
        print(header)
        for row in reader:
          iterable = zip(header, row)
          year_dict = {key: value for key, value in iterable}
          data.append(year_dict)
        return data
    
if __name__ == '__main__':
    data = read_csv('./proyecto/data.csv')
    print(data[0])