📌 AWS EC2 Bulk Tagging Automation Script
🚀 Automate tagging for EC2 instances and all associated AWS resources across multiple regions!

🔹 Features
✅ Tags EC2 instances, volumes, snapshots, AMIs, security groups, and network interfaces
✅ Multi-region support – Detects the correct region from the Excel file
✅ Bulk processing – Reads from an Excel file and applies tags automatically
✅ 4-second delay – Prevents hitting AWS rate limits
✅ Fully automated – Just upload the Excel file & run the script

📥 Installation
1️⃣ Clone the repository

2️⃣ Install dependencies
pip install boto3 pandas openpyxl

3️⃣ Set up AWS credentials
Ensure you have AWS CLI configured:
aws configure

📄 Excel File Format
The script reads an Excel file with the following format:

📄 Excel File Format
The script reads an Excel file with the following format:

Instance ID          Region	            Key Name	              Key Value


✅ Supports multiple regions
✅ Allows custom tag keys and values



🚀 Usage
Run the script by specifying the Excel file path:
python3 tag_ec2_resources.py ec2_tags.xlsx


🛠 How It Works
🔹 Reads the EC2 instance ID, region, tag key, and value from the Excel file
🔹 Finds related resources (volumes, snapshots, AMIs, security groups, network interfaces)
🔹 Tags all associated resources with the specified key-value pair
🔹 Adds a 4-second wait time between API calls to prevent AWS rate limits






