from prefect import task, flow


@task
def say_hi(user_name: str):
    print(f"Hi {user_name}!")


@flow(log_prints=True)
def hello(user: str = "world"):
    say_hi(user)


if __name__ == "__main__":
    hello(user="from QA flow")
