from prefect import flow


@flow
def my_flow():
    return "Hello, world!"

