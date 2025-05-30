#!/bin/bash

regions=$(aws ec2 describe-regions --query "Regions[].RegionName" --output text)

for region in $regions; do
  notebooks=$(aws sagemaker list-notebook-instances \
    --region "$region" \
    --query "NotebookInstances[].NotebookInstanceName" \
    --output text)

  for nb in $notebooks; do
    echo "🧹 Deleting notebook: $nb in region: $region"
    aws sagemaker delete-notebook-instance \
      --notebook-instance-name "$nb" \
      --region "$region" > /dev/null 2>&1 &
    wait
  done
done

wait
