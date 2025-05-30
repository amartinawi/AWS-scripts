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
ammar@WSL:~$ cat ec2
ec2.sh                 ec22.sh                ec2_delete_disable.sh
ammar@WSL:~$ cat ec2_delete_disable.sh
#!/bin/bash

regions=$(aws ec2 describe-regions --query "Regions[].RegionName" --output text)

for region in $regions; do
  echo "▶️ Processing region: $region"

  instance_ids=$(aws ec2 describe-instances \
    --region "$region" \
    --query "Reservations[].Instances[?State.Name!='terminated'].InstanceId" \
    --output text)

  for instance_id in $instance_ids; do
    aws ec2 modify-instance-attribute \
      --instance-id "$instance_id" \
      --no-disable-api-termination \
      --region "$region" > /dev/null 2>&1 &
    wait
    aws ec2 modify-instance-attribute \
      --instance-id "$instance_id" \
      --no-disable-api-stop \
      --region "$region" > /dev/null 2>&1 &
    wait
  done

  wait

  if [ -n "$instance_ids" ]; then
    aws ec2 terminate-instances \
      --instance-ids $instance_ids \
      --region "$region" > /dev/null 2>&1 &
  fi

  volume_ids=$(aws ec2 describe-volumes \
    --region "$region" \
    --filters Name=status,Values=available \
    --query "Volumes[].VolumeId" \
    --output text)

  for volume_id in $volume_ids; do
    aws ec2 delete-volume \
      --volume-id "$volume_id" \
      --region "$region" > /dev/null 2>&1 &
  done

  wait

  echo "✅ Done with region: $region"
done
