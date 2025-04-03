import boto3
import pandas as pd
import time

def tag_ec2_resources(excel_file):
    """
    Reads an Excel file with EC2 instance IDs, regions, tag keys, and values, 
    then tags each instance and its associated resources.
    
    Excel format (with headers):
    - Instance ID (Column 1)
    - Region (Column 2)
    - Key Name (Column 3)
    - Key Value (Column 4)

    :param excel_file: Path to the Excel file containing instance details.
    """

    print("\n🚀 Starting EC2 Tagging Process...\n")

    # Read Excel file (with headers)
    df = pd.read_excel(excel_file)

    # Validate required columns
    required_columns = {"Instance ID", "Region", "Key Name", "Key Value"}
    if not required_columns.issubset(df.columns):
        print(f"❌ Missing required columns. Expected: {required_columns}")
        return

    for _, row in df.iterrows():
        instance_id = str(row["Instance ID"]).strip()
        region = str(row["Region"]).strip()
        tag_key = str(row["Key Name"]).strip()
        tag_value = str(row["Key Value"]).strip()

        if not instance_id or not region or not tag_key or not tag_value:
            print(f"⚠️ Skipping invalid row: {row}")
            continue

        print(f"\n🔍 Processing Instance: {instance_id} in {region} with {tag_key}: {tag_value}")

        ec2 = boto3.client('ec2', region_name=region)

        try:
            # Fetch instance details
            instance = ec2.describe_instances(InstanceIds=[instance_id])['Reservations'][0]['Instances'][0]

            # Get associated resources
            volume_ids = [vol['Ebs']['VolumeId'] for vol in instance.get('BlockDeviceMappings', [])]
            eni_ids = [eni['NetworkInterfaceId'] for eni in instance.get('NetworkInterfaces', [])]

            # Find snapshots linked to instance volumes
            snapshot_ids = []
            if volume_ids:
                snapshots = ec2.describe_snapshots(Filters=[{'Name': 'volume-id', 'Values': volume_ids}])['Snapshots']
                snapshot_ids = [snap['SnapshotId'] for snap in snapshots]

            # Find security groups linked to the instance
            security_group_ids = [sg['GroupId'] for sg in instance['SecurityGroups']]

            # Find AMIs created from this instance
            ami_ids = []
            try:
                amis = ec2.describe_images(Filters=[{'Name': 'block-device-mapping.snapshot-id', 'Values': snapshot_ids}])['Images']
                ami_ids = [ami['ImageId'] for ami in amis]
            except Exception as e:
                print(f"⚠️ No AMIs found for instance {instance_id}: {e}")

            # Aggregate all resources
            resources_to_tag = [instance_id] + volume_ids + eni_ids + snapshot_ids + security_group_ids + ami_ids
            resources_to_tag = list(set(resources_to_tag))  # Remove duplicates

            # Apply tags
            for resource in resources_to_tag:
                ec2.create_tags(Resources=[resource], Tags=[{'Key': tag_key, 'Value': tag_value}])
                print(f"✅ Tagged {resource} with {tag_key}: {tag_value}")
                  # AWS API rate limit delay

        except Exception as e:
            print(f"❌ Error processing instance {instance_id}: {e}")

    print("\n✅ Tagging process completed successfully!\n")
    time.sleep(4)

# Example Usage
if __name__ == "__main__":
    excel_file_path = "ec2-list.xlsx"  # Replace with your Excel file path
    tag_ec2_resources(excel_file_path)
