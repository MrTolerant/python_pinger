import requests
import logging
import time
import sys


def login():
    try:
        start = time.time()
        resp = requests.get(sys.argv[1])
        end = time.time()

        respTime = round((end - start) * 1000)
        if resp.status_code != 200:
            logging.error(
                f"Failed: {resp.status_code}, {resp.content}, {respTime} ms")
        if (resp.status_code == 200) and (respTime < 150):
            logging.info(f"Ok, {respTime} ms")

        if (resp.status_code == 200) and (respTime >= 150):
            logging.warning(f"Bad, {respTime} ms")

    except Exception as exception:
        logging.error(
            f"Exception: {exception.__class__.__name__}")


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
