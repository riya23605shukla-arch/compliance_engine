import json
import os


def save_assessments(
    results
):

    os.makedirs(

        "data/assessments",

        exist_ok=True
    )

    with open(

        "data/assessments/framework_assessment.json",

        "w",

        encoding="utf-8"
    ) as file:

        json.dump(

            results,

            file,

            indent=4
        )

    print(
        "Assessments Saved Successfully"
    )