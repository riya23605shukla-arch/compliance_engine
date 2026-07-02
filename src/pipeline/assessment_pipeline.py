"""
Master Assessment Pipeline

This file connects the entire compliance engine.

Workflow:

Upload PDF
↓

Parse Document
↓

Generate Chunks
↓

Generate Embeddings
↓

Retrieve Evidence
↓

Assess Framework
↓

Generate Reports
"""

from src.assessment.framework_assessor import assess_framework
from src.assessment.save_assessment import save_assessments
from src.assessment.report_generator import generate_framework_report
from src.assessment.traceability_logger import save_traceability_log


def run_complete_assessment(retrieved_chunks):
    """
    Run complete compliance assessment.
    """

    print("=" * 60)
    print("Starting Compliance Assessment Pipeline")
    print("=" * 60)

    print("\nStep 1 : Assessing Framework")

    results = assess_framework(
        retrieved_chunks
    )

    print("✓ Assessment Completed")

    print("\nStep 2 : Saving Assessments")

    save_assessments(results)

    print("✓ Assessments Saved")

    print("\nStep 3 : Generating Report")

    generate_framework_report(results)

    print("✓ Report Generated")

    print("\nStep 4 : Saving Traceability")

    for item in results:

        save_traceability_log(item)

    print("✓ Traceability Logs Saved")

    print("\nPipeline Completed Successfully")

    return results