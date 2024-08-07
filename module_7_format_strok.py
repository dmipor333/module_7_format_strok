team1_num = 5
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'
# использование %:
print('В команде Мастера кода участников: %s !' % team1_num)
print('Итого сегодня в командах учвстников: %d и %d !' % (team1_num, team2_num))
# использование format():
print('Команда Волшебники данных решила задач: {} !'.format(score2))
print('Волшебники данных решили задачи за: {} c !'.format(team1_time))
# использование f-строк:
print(f'Команды решили {score1} и {score2} задач.')
if score1 > score2 or score1 == score2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    result = f'{challenge_result}'
else:
    result = 'Ничья!'
print(result)
x = (team1_time + team2_time) / (score1 + score2)
x = float('{:.1f}'.format(x))
print(f'Сегодня было решено  {score1 + score2} задач,'
      f' в среднем по {x} секунды за задачу!')


