import subprocess
import json


def run_pipeline():

    print("Starting Compliance Assessment Pipeline...")

    print("Parsing Documents...")

    subprocess.run(
        [
            "python",
            "-m",
            "run_assessment"
        ],
        check=True
    )

    print("Generating Embeddings...")

    subprocess.run(
        [
            "python",
            "-m",
            "src.embeddings.generate_embeddings"
        ],
        check=True
    )

    print("Running Compliance Assessment...")

    subprocess.run(
        [
            "python",
            "-m",
            "test_framework_assessment"
        ],
        check=True
    )

    with open(
        "data/assessments/framework_assessment.json",
        "r",
        encoding="utf-8"
    ) as file:

        results = json.load(file)

    return results