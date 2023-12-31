from random import randint
import time

def main():
    print('''Time to test your reflexes and see if you are the fastest
draw in the west!
When you see "DRAW", you have 0.3 seconds to press Enter.
But you lose if you press Enter before "DRAW" appears.''')
    input('Press Enter to begin...')
    while True:
        rand = randint(2,7)
        print('It is high noon...')
        time.sleep(rand)
        print('Draw')
        start_time = time.time()
        ans = input()
        end_time = time.time()
        time_taken = round(end_time-start_time,4)
        if time_taken<0.01:
            print('You drew before "DRAW" appeared! You lose.')
        elif time_taken<0.3:
            print(f'You took {time_taken} seconds to draw')
            print('You are the fastest draw in the west! You win!')
        else:
            print(f'You took {time_taken} seconds to draw. Too slow!')    
        if input('\nEnter (Q)UIT to stop, or press Enter to play again.').lower().startswith('q'):
            print('Thank you for Playing')
            break

main()
