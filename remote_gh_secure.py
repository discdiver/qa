from prefect import serve
from prefect.deployments import remote_flow_to_deployment
from prefect.blocks.system import Secret

if __name__ == "__main__":
    serve(
        remote_flow_to_deployment(
            url="https://github.com/discdiver/qa.git",
            access_token=Secret.load("gh-token").get(),
            entrypoint="basic_flow.py:my_flow",
            name="test-remote1",
        )
    )
