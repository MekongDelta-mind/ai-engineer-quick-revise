
'''
THe general format for try-except
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong") 
finally:
  print("The 'try except' is finished") 

Check out the website below to under more about logging error
https://calmcode.io/course/logging/error


'''

# number = int(input("Enter a number: " ))
# print(number)


# ## Simple try except for the program

# try:
#     number = int(input("Enter a number: " ))
# except BaseException as ex:
#     print(ex.with_traceback())

'''

From the Official doc:
https://docs.python.org/3/tutorial/errors.html

try:

    raise Exception('spam', 'eggs')

except Exception as inst:

    print(type(inst))    # the exception type

    print(inst.args)     # arguments stored in .args

    print(inst)          # __str__ allows args to be printed directly,

                         # but may be overridden in exception subclasses

    x, y = inst.args     # unpack args

    print('x =', x)

    print('y =', y)
'''


import sys

import logging as logging 

import logging
import datetime as dt
# initializing logger and saving them in the code
logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

current_datetime = dt.datetime.now()
logger.debug(f'{current_datetime}------------------------------')
logger.debug(f'{current_datetime}\t \t This message should go to the log file')
logger.info(f'{current_datetime}\t \t So should this')
logger.warning(f'{current_datetime}\t \t And this, too')
logger.error(f'{current_datetime}\t \t And non-ASCII stuff, too, like Øresund and Malmö')


if __name__ == "__main__":
    logger.debug("Program started.")
    try:
        number = int(input("Enter a number: " ))
        print(f'The number you added is {number}')
        logger.debug("Program ended with success.")
    except BaseException as base_ex:
        logger.error(base_ex, exc_info=True)
        print("===ERR===\n", base_ex)
        print("===ARGS===\n", base_ex.args)
        print("===TRACEBACK===")
        print(base_ex.with_traceback())


'''
POINTS TO REMEMBER
1. always use try and except in your program expecially the python files.
2. add the exceptions which you incur whie creating the program should be add to the except block.
3. Logging is very much impoortant with the time stamp. This is the most professional way of creating the software.
    Python logging template: https://gist.github.com/MekongDelta-mind/3d95ac3546b8ee89485f07d381817bae
    you can checkout out better logging template.
'''