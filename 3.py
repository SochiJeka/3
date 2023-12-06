subject_dict = {}

with open('subjects.txt', 'w') as file:
    file.write('Информатика: 100(л) 50(пр) 20(лаб)\n')
    file.write('Физика: 30(л) 10(лаб)\n')
    file.write('Физкультура: 30(пр)\n')

with open('subjects.txt', 'r') as file:
    for line in file:
        subject_data = line.strip().split(':')
        subject_name = subject_data[0].strip()
        lesson_data = subject_data[1].split()
        total_lessons = sum(int(data.split('(')[0]) for data in lesson_data if '(' in data)
        subject_dict[subject_name] = total_lessons

print(subject_dict)