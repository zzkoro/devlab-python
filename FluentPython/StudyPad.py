import logging

def dangerous_call():
    print("dangerous_call")

def after_call(): 
    print("after_call")

# logging sample
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)s] >> %(message)s'))

logger.addHandler(ch)

my_list = []
"""
for item in my_list:
    if item.flavor == 'banana':
        break
else:
    raise ValueError('No banana flavor found')
"""
try:
    dangerous_call()
except OSError:
    logger.debug('OSError...')
else:
    after_call()
    logger.debug('Else: Success')
finally:
    logger.debug('Finally:')

with open('mirror.py') as fp:
    src = fp.read(60)

