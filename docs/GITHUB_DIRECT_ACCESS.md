# TQFA Best Practices - GitHub Direct Access Guide

## 🌐 **Access Best Practices Directly from GitHub**

**Repository**: `https://github.com/Texas-Quantitative/tqfa-development-best-practices`

### **📚 Core Documentation Links**

**Main Entry Point**:
- **[README.md](https://raw.githubusercontent.com/Texas-Quantitative/tqfa-development-best-practices/master/README.md)** - Complete overview and quick start

**Best Practices Guides**:
- **[Best Practices README](https://raw.githubusercontent.com/Texas-Quantitative/tqfa-development-best-practices/master/docs/best-practices/README.md)** - Navigation and overview
- **[Docker Deployment](https://raw.githubusercontent.com/Texas-Quantitative/tqfa-development-best-practices/master/docs/best-practices/docker-deployment.md)** - Azure Container Apps guidance
- **[Scripts & Tools](https://raw.githubusercontent.com/Texas-Quantitative/tqfa-development-best-practices/master/docs/best-practices/scripts-and-tools.md)** - Production scripts
- **[Troubleshooting](https://raw.githubusercontent.com/Texas-Quantitative/tqfa-development-best-practices/master/docs/best-practices/troubleshooting.md)** - Common issues

**Templates**:
- **[Copilot Instructions](https://raw.githubusercontent.com/Texas-Quantitative/tqfa-development-best-practices/master/docs/templates/copilot-instructions-template.md)** - AI agent guidance template

### **🛠️ Scripts (Download & Use)**

```bash
# Download specific scripts directly
curl -O https://raw.githubusercontent.com/Texas-Quantitative/tqfa-development-best-practices/master/scripts/bump_version.py
curl -O https://raw.githubusercontent.com/Texas-Quantitative/tqfa-development-best-practices/master/scripts/check_deployment.py
curl -O https://raw.githubusercontent.com/Texas-Quantitative/tqfa-development-best-practices/master/scripts/promote_healthy_revision.py
```

### **📋 For Project Copilot Instructions**

Add this to your `.github/copilot-instructions.md`:

```markdown
## 📚 **BEST PRACTICES REFERENCE**

**Primary Documentation**: Reference TQFA Best Practices directly from GitHub:

- **[Main Guide](https://raw.githubusercontent.com/Texas-Quantitative/tqfa-development-best-practices/master/README.md)** - Complete overview and quick start
- **[Best Practices](https://raw.githubusercontent.com/Texas-Quantitative/tqfa-development-best-practices/master/docs/best-practices/README.md)** - Detailed guides navigation
- **[Deployment Issues](https://raw.githubusercontent.com/Texas-Quantitative/tqfa-development-best-practices/master/docs/best-practices/docker-deployment.md)** - Azure Container Apps fixes
- **[Troubleshooting](https://raw.githubusercontent.com/Texas-Quantitative/tqfa-development-best-practices/master/docs/best-practices/troubleshooting.md)** - Common problems & solutions

**When to Reference**:
- Deployment issues → docker-deployment.md
- Production scripts needed → scripts-and-tools.md  
- Architecture decisions → README.md core principles
- Agent collaboration → README.md agent instructions
```

### **🔄 Verification Commands**

Check if best practices are accessible:

```bash
# Test GitHub access (PowerShell)
Invoke-RestMethod -Uri "https://api.github.com/repos/Texas-Quantitative/tqfa-development-best-practices/commits/master" | Select-Object sha,commit

# Get latest commit info
curl -s https://api.github.com/repos/Texas-Quantitative/tqfa-development-best-practices/commits/master | jq '.sha,.commit.message'
```

### **✅ Advantages of GitHub Direct Access**

- **Always Current**: No sync scripts needed
- **Zero Setup**: Works immediately on any machine
- **Version Controlled**: Can reference specific commits if needed
- **Fast**: GitHub CDN delivers content quickly
- **Reliable**: Better uptime than local file systems
- **Cross-Platform**: Works on Windows, Mac, Linux equally

### **🎯 Agent Instructions for GitHub Access**

When referencing best practices:
1. **Use raw.githubusercontent.com links** for direct content access
2. **Reference latest master branch** for most current practices  
3. **Cache locally if needed** during active development sessions
4. **Check GitHub API** to verify repo accessibility if links fail

### **📖 Example Agent Workflow**

```bash
# Agent workflow for accessing best practices
1. Check if GitHub is accessible
2. Fetch relevant best practice document(s)
3. Apply guidance to current project
4. Reference specific solutions from troubleshooting guide
# No local files to maintain or sync!
```