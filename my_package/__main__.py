from my_package import version, logger


def main():
    logger.info('this is the entry point of my_package')
    logger.info(f'version: {version}')


if __name__ == '__main__':
    import sys
    sys.exit(main())
