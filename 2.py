with open('Вокзал.txt', 'r') as f:
    lines = f.readlines()

valid_days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
target_day = input("Введите день недели: ")
while target_day.lower() not in valid_days:
    print("Некорректный ввод дня недели. Попробуйте еще раз.")
    target_day = input("Введите день недели: ")

print("Поезда, отправляющиеся в", target_day + ":")
for line in lines:
    train_info = line.split()
    train_day = train_info[2]
    if train_day == target_day:
        print(line.strip())

max_price = 0
max_price_train = ""
for line in lines:
    train_info = line.split()
    ticket_price = int(train_info[4])
    if ticket_price > max_price:
        max_price = ticket_price
        max_price_train = line

print("Поезд с максимальной стоимостью билета:")
print(max_price_train.strip())