## 📌 AWS EC2 Bulk Tagging Automation Script

🚀 **Automate tagging for EC2 instances and all associated AWS resources across multiple regions!**

---

## 🔹 Features

✅ Tags **EC2 instances, volumes, snapshots, AMIs, security groups, and network interfaces**  
✅ **Multi-region support** – Detects the correct region from the Excel file  
✅ **Bulk processing** – Reads from an Excel file and applies tags automatically  
✅ **4-second delay** – Prevents hitting AWS rate limits  
✅ **Fully automated** – Just upload the Excel file & run the script  

---

## 📥 Installation

1️⃣ **Clone the scritp**  
```sh
git clone https://github.com/ammarti/AWS-scripts.git
cd AWS-scripts/tagging/ec2/
```

2️⃣ **Install dependencies**  
```sh
pip install boto3 pandas openpyxl
```

3️⃣ **Set up AWS credentials**  
Ensure you have AWS CLI configured:  
```sh
aws configure
```

---

## 📄 Excel File Format

The script reads an **Excel file** with the following format:

| **Instance ID**      | **Region**  | **Key Name** | **Key Value**  |
|----------------------|------------|-------------|---------------|
| i-1234567890abcde1  | us-east-1  | App         | FinanceApp    |
| i-0987654321abcde2  | eu-central-1 | Owner      | HR Dept      |
| i-1111222233334444  | us-west-2  | Environment | Production   |


name the excel file as: ec2_tags.xlsx

✅ **Supports multiple regions**  
✅ **Allows custom tag keys and values**  

---

## 🚀 Usage

Run the script by specifying the Excel file path:  

```sh
python3 tag_ec2_resources.py ec2_tags.xlsx
```

---

## 🛠 How It Works

🔹 Reads the **EC2 instance ID, region, tag key, and value** from the Excel file  
🔹 **Finds related resources** (volumes, snapshots, AMIs, security groups, network interfaces)  
🔹 Tags **all associated resources** with the specified key-value pair  
🔹 Adds a **4-second wait time** between API calls to prevent AWS rate limits  

---

## 📌 Why Use This Instead of AWS Tag Editor?

| **Feature**          | **AWS Tag Editor** | **This Script** |
|----------------------|------------------|---------------|
| **Multi-region support** | ❌ No | ✅ Yes |
| **Tags associated resources automatically** | ❌ No | ✅ Yes |
| **Supports Excel input** | ❌ No | ✅ Yes |
| **API rate limit handling** | ❌ No | ✅ Yes |

---

## 🌟 Contribute

Feel free to **fork** this repo, submit **pull requests**, or report **issues**!  

---

## 📜 License

This project is licensed under the **MIT License**.
