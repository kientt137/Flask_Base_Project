def on_starting(server):
    print("Server has started",  flush=True)


def when_ready(server):
    print("Server has ready")

def on_reload(server):
    """
     Do something on reload
    """
    print("Server has reloaded")


def post_worker_init(worker):
    """
    Do something on worker initialization
    """
    print("Worker has been initialized. Worker Process id -->", worker.pid)
