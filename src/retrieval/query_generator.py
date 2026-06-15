import json

# Load NIST controls
with open(
    "frameworks/nist_csf_2_mvp.json",
    "r",
    encoding="utf-8"
) as file:

    controls = json.load(file)

# Example control
control_id = "PR.AA-01"

# Find matching control
for control in controls:

    if control["control_id"] == control_id:

        print("\nControl Found\n")

        print(
            "Control ID:",
            control["control_id"]
        )

        print(
            "Category:",
            control["category"]
        )

        print(
            "Subcategory:",
            control["subcategory"]
        )

        # Build retrieval query
        
        query = " ".join([
            control["subcategory"],
            " ".join(control["expected_evidence"]),
            " ".join(control["keywords"]),
            " ".join(control["assessment_questions"])
        ])

        print("\nGenerated Query:\n")

        print(query)

        break