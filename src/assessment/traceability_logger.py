import json
import os


def save_traceability_log(results):

    os.makedirs(
        "data/logs",
        exist_ok=True
    )

    with open(
        "data/logs/traceability_log.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            results,
            file,
            indent=4
        )

    print(
        "Traceability Log Saved"
    )