from logger import logger


@logger.parameterized('logs/logger.txt')
def calculate_salary():
    print('calculate_salary function')
