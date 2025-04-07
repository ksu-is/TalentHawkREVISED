# Setting Up TalentHawk on GitHub

This guide provides instructions for setting up the TalentHawk repository on GitHub.

## Creating a New GitHub Repository

1. Go to [GitHub](https://github.com/) and sign in to your account.

2. Click on the "+" icon in the top-right corner and select "New repository."

3. Enter "talenthawk" as the repository name.

4. Add a description: "A soccer talent scouting and analytics platform."

5. Choose if you want your repository to be public or private.

6. Do NOT initialize the repository with a README, .gitignore, or license since we already have these files.

7. Click "Create repository."

## Uploading Your Local Repository to GitHub

After creating the repository on GitHub, run the following commands in your local TalentHawk directory:

```bash
# Add the remote GitHub repository
git remote add origin https://github.com/YOUR_USERNAME/talenthawk.git

# Push the repository to GitHub
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

## Setting Up GitHub Pages (Optional)

If you want to showcase the project with a simple website:

1. Go to the repository settings on GitHub.

2. Scroll down to the "GitHub Pages" section.

3. In the "Source" dropdown, select "main" branch and "/docs" folder.

4. Click "Save."

5. Your site will be published at `https://YOUR_USERNAME.github.io/talenthawk/`.

## Setting Up GitHub Actions (Optional)

To set up automated testing and deployment:

1. Create a `.github/workflows` directory in your repository.

2. Create a file named `python-tests.yml` in that directory with the following content:

```yaml
name: Python Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, '3.10']

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
        pip install -e .
    - name: Lint with flake8
      run: |
        flake8 talenthawk tests
    - name: Test with pytest
      run: |
        pytest
```

3. Push these changes to your GitHub repository:

```bash
git add .github/workflows/python-tests.yml
git commit -m "Add GitHub Actions workflow for testing"
git push
```

## Next Steps

- Add collaborators to your repository if you're working in a team.
- Set up project boards to track development tasks.
- Configure branch protection rules for the main branch.
- Consider adding a CODE_OF_CONDUCT.md and CONTRIBUTING.md for community guidelines. 