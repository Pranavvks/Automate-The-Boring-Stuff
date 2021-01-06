import pyinputplus as pyip
import  time
numberOfQuestions = 10
correctAnswers=0
for questionNumber in range (10):
    num1=questionNumber
    num2=questionNumber

    prompt='#%s:%s x %s= '%(questionNumber,num1,num2)
    try:
        pyip.inputStr(prompt,allowRegexes=['^%s$'%(num1*num2)],
        blockRegexes=[('.*'),'Incorrect!'],
        timeout=8 , limit=3 )
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')

    else:   
        print("Correct Answer")
        correctAnswers+=1
        time.sleep(1)


