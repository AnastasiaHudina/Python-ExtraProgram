numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25] #исходный список
# TODO заменить значение пропущенного элемента средним арифметическим
numbers1 = numbers[0:4]+numbers[5:] #создаем список без пропущенного элемента
average = sum(numbers1)/len(numbers) #среднее арифметическое
numbers[4]=average #заменяем пропуск на среднее арифметическое
print("Измененный список:", numbers) #выводим новый список
