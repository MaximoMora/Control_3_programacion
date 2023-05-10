import csv


def read_csv(file_name):
  result = []
  with open(file_name) as file:
      reader = csv.reader(file)
      for i in reader:
        result.append(i)

  return result


def average_row(array):
  dict_row = {}
  array_len = len(array)
  for row in range(array_len):
    row_sum = 0
    for column in range(array_len):
      row_sum += float(array[row][column])
      
      
    
    row_sum = row_sum / array_len

    dict_row[row+1] = row_sum

  print(dict_row)  
  return dict_row


def average_column(array):
  dict_column = {}
  array_len = len(array)
  for column in range(array_len):
    sum_column = 0
    for row in range(array_len):
      sum_column += float(array[column][row])


    print(sum_column)

    sum_column = sum_column / array_len
      
    dict_column[column+1] =  sum_column

  return dict_column
  


#Leer el archivo C1.csv
result = read_csv("C1.csv")

#Promedio de cada fila
print(result)
row_average = average_row(result)
#print(f"row average",row_average)

#Promedio de cada columna
a = average_column(result)
print("average_colunm", a)

