from prefect import task, flow


@task
def say_word(user_name: str):
    print(f"Word {user_name}!")


@flow(log_prints=True)
def word_flow(user: str = "world"):
    say_word(user)


if __name__ == "__main__":
    word_flow.serve(name="word flow", cron="* * * * *")
