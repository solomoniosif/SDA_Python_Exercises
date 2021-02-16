import logging

if __name__ == "__main__":
    logging.debug(f"{dir(logging)[:10]}")
    logging.info("An information")
    logging.warning("A warning")
    logging.error("An error")
    logging.critical("Something is very wrong!")
