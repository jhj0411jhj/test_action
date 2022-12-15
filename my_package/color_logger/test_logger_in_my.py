import logging

try:
    import my_package
except ModuleNotFoundError as e:
    print('my_package is not installed. Use the local code instead.')
    import os, sys
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_package import logger


def test_logger():
    logger.critical('This is a message using console logger before manual init.')

    logger.init(name='name', level='DEBUG', stream=True, logdir='logs/')

    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')
    try:
        raise ValueError('haha')
    except ValueError:
        logger.exception('exception')

    logger.init('new name', level='INFO', logdir=None, force_init=True)
    logger.info('info! this should not be logged to file')

    logger.init('new name', level='INFO', logdir=None, stream=False, force_init=True)
    logger.info('info! this should not be logged to file or stdout')

    # Caution: logging information will not be saved to file if using `logging.getLogger`
    logging.setLoggerClass(logger.ColorLogger)
    log = logging.getLogger('main')
    log.info('info from main using logging.getLogger')
    raise ValueError('This file is in my_package. It should not be tested. Please specify test dir.')
