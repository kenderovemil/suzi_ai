# Contributing to Suzi AI

Thank you for your interest in contributing to Suzi AI! This guide will help you set up your development environment and contribute to the project.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+**
- **Git**
- GitHub account with proper authentication configured

---

## 🔐 GitHub Authentication Setup

GitHub no longer accepts passwords for Git operations over HTTPS. You must use either **SSH keys** or **Personal Access Tokens (PAT)**.

### Option 1: Using SSH (Recommended)

#### Step 1: Check if you have SSH keys
```bash
ls -al ~/.ssh
```

Look for files like `id_rsa.pub`, `id_ecdsa.pub`, or `id_ed25519.pub`.

#### Step 2: Generate SSH key (if you don't have one)
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Press Enter to accept the default file location and optionally set a passphrase.

#### Step 3: Add SSH key to ssh-agent
```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

#### Step 4: Add SSH key to your GitHub account
1. Copy your public key:
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```
2. Go to GitHub → Settings → SSH and GPG keys → New SSH key
3. Paste your key and save

#### Step 5: Configure your repository to use SSH
```bash
cd /path/to/suzi_ai
git remote -v  # Check current remote
git remote set-url origin git@github.com:kenderovemil/suzi_ai.git
```

#### Step 6: Test your connection
```bash
ssh -T git@github.com
```

You should see: "Hi username! You've successfully authenticated..."

---

### Option 2: Using Personal Access Token (PAT)

#### Step 1: Create a Personal Access Token
1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a descriptive name (e.g., "Suzi AI Development")
4. Select scopes: `repo` (full control of private repositories)
5. Click "Generate token"
6. **IMPORTANT**: Copy the token immediately (you won't see it again)

#### Step 2: Configure your repository to use HTTPS
```bash
cd /path/to/suzi_ai
git remote set-url origin https://github.com/kenderovemil/suzi_ai.git
```

#### Step 3: Use the token when pushing
When Git asks for your password, use your **Personal Access Token** instead:
```bash
git push -u origin main
Username: your_github_username
Password: your_personal_access_token
```

#### Step 4: Cache your credentials (optional)
To avoid entering credentials every time:
```bash
git config --global credential.helper store
```

**Note**: This stores credentials in plain text. For better security, use SSH or a credential manager.

---

## 🛠️ Troubleshooting Common Issues

### ❌ Error: "Permission to kenderovemil/suzi_ai.git denied" (403)

This error occurs when GitHub authentication fails. Here's how to fix it:

#### Problem: Using password instead of PAT
**Solution**: GitHub no longer accepts passwords. Use a Personal Access Token (see Option 2 above).

#### Problem: SSH key not configured
**Solution**: If your remote URL is `git@github.com:...`, you need SSH keys configured (see Option 1 above).

#### Problem: Cached incorrect credentials
**Solution**: Clear cached credentials and re-authenticate:

**On Linux/Mac:**
```bash
git credential-cache exit
# or
git config --global --unset credential.helper
rm ~/.git-credentials
```

**On Windows:**
```bash
git credential-manager uninstall
git credential-manager install
```

#### Problem: Wrong remote URL
**Solution**: Check and update your remote URL:
```bash
# Check current remote
git remote -v

# For SSH (if you have SSH keys):
git remote set-url origin git@github.com:kenderovemil/suzi_ai.git

# For HTTPS (if you have a PAT):
git remote set-url origin https://github.com/kenderovemil/suzi_ai.git
```

#### Problem: Using both SSH and HTTPS
**Solution**: Make sure your remote URL matches your authentication method:
- If you have SSH keys configured, use: `git@github.com:kenderovemil/suzi_ai.git`
- If you're using PAT, use: `https://github.com/kenderovemil/suzi_ai.git`

---

## 🔧 PyCharm Git Configuration

If you're using PyCharm:

1. **Settings → Version Control → Git**: Verify Git executable path
2. **Settings → Appearance & Behavior → System Settings → Passwords**: Choose credential storage
3. **VCS → Git → Remotes**: Verify remote URL is correct
4. **Test**: VCS → Git → Push (Ctrl+Shift+K)

### PyCharm with SSH:
- Make sure SSH agent is running and key is added
- PyCharm will use system SSH configuration

### PyCharm with HTTPS + PAT:
- When prompted for password, enter your Personal Access Token
- Check "Remember" to save credentials

---

## 📦 Development Setup

### 1. Clone the repository

**With SSH:**
```bash
git clone git@github.com:kenderovemil/suzi_ai.git
cd suzi_ai
```

**With HTTPS:**
```bash
git clone https://github.com/kenderovemil/suzi_ai.git
cd suzi_ai
```

### 2. Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a feature branch
```bash
git checkout -b feature/your-feature-name
```

### 5. Make your changes
- Follow Python PEP 8 style guidelines
- Add tests for new functionality
- Update documentation as needed

### 6. Commit and push
```bash
git add .
git commit -m "Description of your changes"
git push -u origin feature/your-feature-name
```

### 7. Create a Pull Request
Go to GitHub and create a Pull Request from your branch to `main`.

---

## 📝 Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small

---

## 🧪 Testing

Before submitting a pull request:
1. Ensure all existing tests pass
2. Add tests for new functionality
3. Test your changes manually

---

## 📧 Questions?

If you have questions or need help:
- Open an issue on GitHub
- Check existing issues for similar problems
- Refer to the troubleshooting section above for authentication issues

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the same MIT License that covers this project.
