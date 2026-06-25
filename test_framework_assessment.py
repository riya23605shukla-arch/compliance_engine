from src.assessment.framework_assessor import (
    assess_framework
)

from src.assessment.save_assessment import (
    save_assessments
)
from src.assessment.report_generator import (
    generate_report
)
from src.assessment.traceability_logger import (
    save_traceability_log
)
retrieved_chunks = [

    {

        "text":

        """
        Access control policy exists.

        Role based access control
        is implemented.

        Access review is conducted.

        Password requirements
        are enforced.

        Incident response plan
        exists.

        Asset inventory is maintained.

        Backup policy is documented.
        """
    }
]

results = assess_framework(
    retrieved_chunks
)

save_assessments(
    results
)

generate_report(results)
save_traceability_log(results)


for item in results:

    print(

        item["control_id"],

        item["status"],

        item["confidence"]
    )