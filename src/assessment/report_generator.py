import csv
import os


def generate_report(results):

    os.makedirs(
        "data/reports",
        exist_ok=True
    )

    with open(
        "data/reports/framework_report.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Control ID",
            "Status",
            "Confidence"
        ])

        for result in results:

            writer.writerow([
                result["control_id"],
                result["status"],
                result["confidence"]
            ])

    print(
        "Framework Report Generated"
    )