# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они 
# сделали S журавликов. Сколько журавликов сделал каждый
#  ребенок, если известно, что Петя и Сережа сделали 
# одинаковое количество журавликов, а Катя сделала в два раза 
# больше журавликов, чем Петя и Сережа вместе?

s = int(input("Сколько всего журавликов сделали: "))
a = s // 6
print(f"Катя сделала {a*4} журавликов, Петя и Серёжа по {a}")
