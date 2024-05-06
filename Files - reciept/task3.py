folder_name = 'task3 files' # имя папки с файлами
files_count = 3 # известное количество файлов

file_lines_data = {}
for i in range(files_count):
    filename = str(i+1) + '.txt' # имя файла = число + .txt
    # открываем файл из папки
    with open(folder_name + '/' + filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    file_lines_data[filename] = lines
with open('result.txt', 'w', encoding='utf-8') as f:
    while file_lines_data: # пока слвоварь не опустее
        # выбираем файл с минимальным количеством строк
        min_key = None
        min_length = float('inf')
        for k,v in file_lines_data.items():
            if len(v) < min_length: # просмотр по длинам списка строк
                min_length = len(v)
                min_key = k
        min_value = file_lines_data.pop(min_key) # извлекаем запись из словаря
        # запись в результирующий файл
        f.write(min_key + '\n')
        f.write(str(len(min_value)) + '\n')
        for line in min_value:
            f.write(line)
        f.write('\n')