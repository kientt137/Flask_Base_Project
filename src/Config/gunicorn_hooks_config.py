def on_starting(server):
    # monkey patching before import other package
    # https://github.com/gevent/gevent/issues/1016
    # issue when download file from S3
    try:
        import gevent.monkey
        gevent.monkey.patch_all(thread=False)
    except ImportError:
        pass
    print("Server has started")

def when_ready(server):
    from src import app
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
