#!python3

import time,pprint,pyperclip

print('Press Enter to begin , Afterward press Enter to click the stopwatch')
input() # Press Enter to begin
print('Started')

startTime = time.time()
lastTime  = startTime
lapNum    =   1 
copy1=[]
final=''
try:
    while True:
        input()
        lapTime = round(time.time()-lastTime,2)
        totalTime = round(time.time()-startTime,2)
        copy2 =   ("Lap #" + str(lapNum).rjust(10))
        copy2 += (str(lapTime).rjust(10))
        copy2 +=  (str((totalTime)).rjust(3))
        copy1.append(copy2)
        print((str('Lap #%s: %s(%s)'%((str(lapNum)) ,(str (totalTime)) , (str(lapTime).rjust(5))))))
        pyperclip.copy(copy1)
        lapNum+=1
        lastTime=time.time()
        

except KeyboardInterrupt:
    print('\n Done')
    for x in copy1:
        final += str(x) + '\n'
        print(final)
    pyperclip.copy(final)

    
