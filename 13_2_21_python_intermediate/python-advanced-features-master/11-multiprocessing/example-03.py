import multiprocessing


def echo(pipe):
    query = pipe.recv()
    while query is not None:
        pipe.send(f"Echo: {query}")
        query = pipe.recv()


if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()
    proc = multiprocessing.Process(target=echo, args=(child_conn,))
    proc.start()
    parent_conn.send("Hello")
    print(parent_conn.recv())
    parent_conn.send("Hello!")
    print(parent_conn.recv())
    parent_conn.send(None)
    proc.join()
