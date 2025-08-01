# 🔐 Cloud Security CI/CD Pipeline

A GitHub Actions pipeline that scans your code and Infrastructure-as-Code (Terraform) for common security risks before deploying to the cloud.

This project is built for **Cloud Security Engineers**, **DevSecOps professionals**, and anyone who wants to shift security left in their CI/CD process.

---

## 📦 What This Pipeline Does

✅ Scans for hardcoded secrets and credentials using **Gitleaks**  
✅ Performs static analysis on **Terraform code** using **tfsec** and **checkov**  
✅ Detects insecure patterns in Python code using **Semgrep**  
✅ (Optional) Sends Slack notifications when scans complete

---

## 📂 Project Structure

```
.
├── .github/workflows/security-scan.yml   # CI/CD pipeline
├── .semgrep.yml                          # Custom Semgrep rules
├── example.py                            # Sample code with security flaws
├── terraform/
│   └── main.tf                           # Sample Terraform with insecure config
└── README.md
```

---

## 🚀 Getting Started

1. **Fork this repository**
2. Make any changes or add your own code and Terraform files
3. Push to any branch – the pipeline runs automatically via GitHub Actions

---

## 🧪 Included Tools

| Tool       | Purpose                                      |
|------------|----------------------------------------------|
| `Gitleaks` | Detects secrets and credentials in code      |
| `tfsec`    | Scans Terraform for insecure configurations  |
| `checkov`  | Advanced policy-as-code scanning for IaC     |
| `Semgrep`  | Static code analysis for Python (custom rules) |

---

## 📄 Example Findings

- AWS Access Keys exposed in code
- `subprocess.call(..., shell=True)` vulnerability
- S3 bucket with `public-read` ACL
- Disabled versioning on Terraform resources

---

## 📢 Optional: Slack Notifications

You can enable Slack alerts by adding your webhook to the repo’s secrets:

```bash
Settings → Secrets → Actions → New Repository Secret:
Name: SLACK_WEBHOOK_URL
Value: [Your Slack webhook URL]
```

---

## ⚠️ Warning

The files `example.py` and `terraform/main.tf` are intentionally insecure and should **never** be used in production.  
They are included **only for demonstrating how the security pipeline detects issues.**

---

## 🌟 Star this repo if you find it useful!

Made with 💻 by a Cloud Security Engineer, for Cloud Security Engineers.

----

## 👨‍💻 Author

[Abdullrahman Wasfi](https://www.linkedin.com/in/abdullrahmanwasfi)

Made with ❤️ using GitHub Actions, Terraform, checkov, Gitleaks and Semgrep

---

## 📄 License

MIT License
