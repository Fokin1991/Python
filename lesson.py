# Упражнение 1
# x=5
# y=6
# result=x<y
# print(result)


# Упражнение 2

#x = str("(3<6) and (6<8)")
#x=str(x)
#y = str("(6>9) and (7>8)")

#if str(x)==x:

#print(x)

#else:
#y= str("(6>9) and (7>8)")

#print(y)

#### Упражнение 3

#Weather = input('Какая сегодня погода ? (дождь/снег/солнце) ')
#if Weather == 'дождь':
#print('не забудь зонтик')

#elif Weather == 'снег':
#print('Не забудь варежки')
#else:
#print('Не забудь солнечные очки')

# Упражнение 4  на  возврат  номера и значения из списка

#Rockets_player=['Маша', 'Даша', 'Миша' ]

#print(Rockets_player[1])

#print(Rockets_player.index('Маша'))

##index=0
##hippos=5
##while index<hippos:
#index=index + 1
###print (hippos)





hippos = 0
print('Бегемотов в пирамиде:'+str(hippos))
input('добавить бегемота (д/н)')
answer='д'
while answer=='д':
    hippos=hippos+1
    print('Бегемотов в пирамиде:'+str(hippos))
    answer=input('добавить еще бегемотов(д/н)')

   
