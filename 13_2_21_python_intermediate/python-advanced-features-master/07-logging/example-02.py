import logging
import tempfile

if __name__ == "__main__":
    l = logging.getLogger()
    l.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter("%(levelname)-8s (%(asctime)s): %(message)s")
    )
    l.addHandler(console_handler)

    file_handler = logging.FileHandler("example-02.log", mode="w+")
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(
        logging.Formatter("%(levelname)-8s in %(filename)s: %(message)s")
    )
    l.addHandler(file_handler)

    logging.debug(f"{dir(logging)[:10]}")
    logging.info("An information")
    logging.warning("A warning")
    logging.error("An error")
    logging.critical("Something is very wrong!")

    print("\nexample-02.log contents:".ljust(50, "-"))
    with open("example-02.log") as f:
        for l in f:
            print(l, end="")
