from prefect import serve
from prefect.deployments import remote_flow_to_deployment

if __name__ == "__main__":
    serve(
        remote_flow_to_deployment(
            url="https://github.com/discdiver/qa.git",
            entrypoint="basic_flow.py:my_flow",
            name="test-remote1",
        )
    )
