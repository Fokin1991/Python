# Упражвевие 1
# x=5
# y=6
# result=x<y
# print(result)


# Упражвевие 2

#x = str("(3<6) and (6<8)")
#x=str(x)
#y = str("(6>9) and (7>8)")

#if str(x)==x:

#print(x)

#else:
#y= str("(6>9) and (7>8)")

#print(y)

#### Упражвевие 3

#Weather = input('Какая сегодвя погода ? (дождь/свег/солвце) ')
#if Weather == 'дождь':
#print('ве забудь зовтик')

#elif Weather == 'свег':
#print('ве забудь варежки')
#else:
#print('ве забудь солвечвые очки')

# Упражвевие 4  ва  возврат  вомера и звачевия из списка

#Rockets_player=['Маша', 'Даша', 'Миша' ]

#print(Rockets_player[1])

#print(Rockets_player.index('Маша'))

##index=0
##product=5
##while index<product:
#index=index + 1
###print (product)





product = 0
print('Продуктов в корзине ' +str(product))
answer=input('добавить  (д/н) ')

if answer=='д':
    product=product+1
    print('Фруктов в корзине ' +str(product))
    answer=input('добавить еще фруктов/убрать продукты/выйти из корзины (д/у/в)')
while answer=='д':
    product=product+1
    print('Фруктов в корзине ' +str(product))
    answer=input('добавить еще фруктов/убрать продукты/выйти из корзины (д/у/в)')
if answer=='у':
     product=product-1
     print('Продуктов в корзине ' +str(product))
     answer=input('добавить еще фруктов/убрать продукты/выйти из корзины (д/у/в)')
     
else:
    print('Продуктов в корзине ' +str(product))



   
