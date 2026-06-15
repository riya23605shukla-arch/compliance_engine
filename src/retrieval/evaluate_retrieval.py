import json

# Load ground truth data
with open(
    "data/evaluation/retrieval_ground_truth.json",
    "r",
    encoding="utf-8"
) as file:

    ground_truth = json.load(file)

# Example retrieved results
# Replace these later with actual retrieval outputs
retrieved_results = {
    "PR.AA-01": [
        "GPI_InformationSecurityPolicy (1).pdf",
        "ADITYA_BIRLA_GRASIM_information-security-policy.pdf",
        "clark_county_asset_management_policy.pdf",
        "Ohio_state_university_asset-management-policy.pdf",
        "INDEGENE_information-security-policy (1).pdf"
    ]
}

# Initialize metrics
total_hit_rate = 0
total_precision = 0
total_recall = 0
total_mrr = 0

num_controls = 0

# Evaluate each control
for item in ground_truth:

    control_id = item["control_id"]

    if control_id not in retrieved_results:
        continue

    relevant_docs = item["relevant_documents"]

    retrieved_docs = retrieved_results[control_id]

    num_controls += 1

 
    # Hit Rate@5
    
    hit = 0

    for doc in retrieved_docs:

        if doc in relevant_docs:
            hit = 1
            break

    total_hit_rate += hit

  
    # Precision@5
   
    relevant_retrieved = 0

    for doc in retrieved_docs:

        if doc in relevant_docs:
            relevant_retrieved += 1

    precision = relevant_retrieved / len(retrieved_docs)

    total_precision += precision

    
    # Recall@5
   
    recall = relevant_retrieved / len(relevant_docs)

    total_recall += recall

   
    # MRR

    reciprocal_rank = 0

    for rank, doc in enumerate(retrieved_docs, start=1):

        if doc in relevant_docs:

            reciprocal_rank = 1 / rank

            break

    total_mrr += reciprocal_rank

# Final Metrics
if num_controls > 0:

    print("\n===== Retrieval Metrics =====\n")

    print(
        "Hit Rate@5:",
        round(total_hit_rate / num_controls, 4)
    )

    print(
        "Precision@5:",
        round(total_precision / num_controls, 4)
    )

    print(
        "Recall@5:",
        round(total_recall / num_controls, 4)
    )

    print(
        "MRR:",
        round(total_mrr / num_controls, 4)
    )

else:

    print("No controls evaluated.")