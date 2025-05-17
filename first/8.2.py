import logging
import time

logging.basicConfig(
    filename ='log.log',
    level=logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)
def divide(a,b):
    logging.info('Divide:a={a},b={b}')
    try:
        result=a/b
        logging.info(f'result={result}')
        return result
    except ZeroDivisionError as e:
        logging.error('Division by zero',exc_info=True)
        return None

 def test_divide():
    assert divide(10,2) ==5
    assert divide(10,0) is None

if __name__ == '__main__':
    divide(12,4)
    divide(5,0)


