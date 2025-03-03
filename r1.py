import random
from random import randint as rdi
from datetime import datetime as dt

#settings
run_time:int=100
option:int=3

log:list=[]
output_log:str=''
win_time=0
lose_time=0


def Get_log(mode:str='print'):
    n=0
    d=f'''Run times:{run_time}
Win times:{win_time}, Win Rate:{win_time/run_time*100:.2f}%
Lose times:{lose_time}, Lose Rate:{lose_time/run_time*100:.2f}%
'''
    d+='-'*100+'\n'
    title='{0:<6} {1:<10} {2:<10} {3:<10} {4:<10} {5:<10}'.format('No.','Result','Correct','Chosen','Opened','New Chosen')
    for i in log:
        output='{0:<6} {1:<10} {2:<10} {3:<10} {4:<10} {5:<10}'.format(n,log[n][0],log[n][1],log[n][2],log[n][3],log[n][4])
        if mode=='print':
            print(d+title) if n==0 else ''
            print(output)
        elif mode=='output':
            global output_log
            output_log+=output+'\n'
        n+=1
    if mode=='output':
        return d+'\n'+output_log
    return 0

def Output_log(file_path:str='log',time=dt.now().strftime('%Y-%m-%d_%H-%M-%S')):
    global output_log
    with open(f'{file_path} {time}.txt','w') as f:
        f.write(Get_log('output'))
        print(f'Log has been saved to {file_path} {time}.txt')
    return 0

############################################################################################################

def Get_opened(correct,chosen):
    opened=rdi(1,option)
    while opened==correct or opened==chosen:
        opened=rdi(1,option)
    return opened

def Get_new_chosen(chosen,opened):
    new_chosen=rdi(1,option)
    while new_chosen==chosen or new_chosen==opened:
        new_chosen=rdi(1,option)    
    return new_chosen

def main(mode):
    for i in range(run_time):
        global win_time,lose_time

        correct=rdi(1,option)
        chosen=rdi(1,option)
        opened=Get_opened(correct,chosen)
        

        if mode==1:
            if rdi(0,1):
                new_chosen=Get_new_chosen(chosen,opened)
            else:
                new_chosen=chosen
        elif mode==2:
            new_chosen=Get_new_chosen(chosen,opened)
        
        if new_chosen==correct:
            win_time+=1
        else:
            lose_time+=1

        log.append(['Win' if new_chosen==correct else 'Lose',correct,chosen,opened,new_chosen])
    
main(2)    
Get_log()
Output_log()

while input()!='':
    pass
exit()
