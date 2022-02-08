import requests
import logging
import time
import sys


def login():
    start = time.time()
    resp = requests.get(sys.argv[0])
    end = time.time()

    if resp.status_code != 200:
        logging.error(
            f"Failed: {resp.status_code}, {resp.content}, {end - start} seconds")
    if resp.status_code == 200:
        logging.info(f"Works!, {end - start} seconds")


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ])
    logging.info('Started')
    while True:
        login()
        time.sleep(0.5)
    logging.info('Finished')


if __name__ == '__main__':
    main()
