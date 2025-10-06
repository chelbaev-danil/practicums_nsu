sec = int(input())

hours = sec//(60*60)
minutes = (sec - hours*(60*60))//60
seconds = sec%60

print(f'{hours} часов {minutes} минут {seconds} секунд')

