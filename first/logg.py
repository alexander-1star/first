from logging import basicConfig, INFO, info
from datetime import datetime


basicConfig(
    filename='date.log',
    level=INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

current_date = datetime.now().strftime('%Y-%m-%d')

info(f'Today\'s dat is {current_date}')
