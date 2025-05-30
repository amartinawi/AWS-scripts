#!/bin/bash

regions=$(aws ec2 describe-regions --query "Regions[].RegionName" --output text)

for region in $regions; do
  clusters=$(aws ecs list-clusters --region "$region" --query "clusterArns[]" --output text)

  for cluster in $clusters; do
    # List all services in the cluster
    services=$(aws ecs list-services --cluster "$cluster" --region "$region" --query "serviceArns[]" --output text)

    # Force delete all services in parallel
    for service in $services; do
      echo "🧨 Deleting service: $service in cluster: $cluster (region: $region)"
      aws ecs delete-service --cluster "$cluster" --service "$service" --region "$region" --force > /dev/null 2>&1 &
    done

    # Wait for service deletions to complete
    wait

    # Now delete the cluster
    echo "🗑️ Deleting ECS cluster: $cluster in region: $region"
    aws ecs delete-cluster --cluster "$cluster" --region "$region" > /dev/null 2>&1 &
  done
done

wait
