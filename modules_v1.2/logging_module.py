# use for debugging

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')


# basicConfig()         # Spacify the record in given format

def factorial(n):
    logging.info(f'Start of factorial({n})')
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.critical(f'i is {i}, total is {total}')
    logging.error(f'End of factorial{n}')
    return total

print(factorial(5))
logging.warning('End of program')

#  2019-10-03 02:09:20,406 - INFO- Start of factorial(5)
#  2019-10-03 02:09:20,407 - CRITICAL- i is 1, total is 1
#  2019-10-03 02:09:20,408 - CRITICAL- i is 2, total is 2
#  2019-10-03 02:09:20,409 - CRITICAL- i is 3, total is 6
#  2019-10-03 02:09:20,409 - CRITICAL- i is 4, total is 24
#  2019-10-03 02:09:20,409 - CRITICAL- i is 5, total is 120
#  2019-10-03 02:09:20,410 - ERROR- End of factorial5 120
#  2019-10-03 02:09:20,410 - WARNING- End of program

#  ##########Error Level

#  LEVEL                     Logging function                    Description
# DEBUG                    logging.debug()              The lowest level. Used for small details.
                                                                        #  Usually you care about these messages
                                                                        #  only when diagnosing problems.
	
# INFO                        logging.info()                Used to record information on general 
                                                                        # events in your program or confirm that 
                                                                        # things are working at their point in the program.
	
# WARNING               logging.warning()       Used to indicate a potential problem that
                                                                        #  doesn’t prevent the program from working
                                                                        #  but might do so in the future.
	
# ERROR                     logging.error()             Used to record an error that caused the program
                                                                        #  to fail to do something.
	
# CRITICAL                  logging.critical()          The highest level. Used to indicate a fatal error 
                                                                        # that has caused or is about to cause the 
                                                                        # program to stop running entirely.
	








