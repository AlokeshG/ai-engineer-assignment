# Part 3 – CI/CD and Deployment

## CI/CD Pipeline

The GitHub Actions workflow automates the basic development lifecycle.

### On Every Push

- Checkout the repository
- Set up Python 3.11
- Install project dependencies
- Run linting
- Run tests

This helps detect issues before deployment.

---

## Staging Deployment

When changes are merged into the `main` branch, the deployment job is triggered.

For this assignment, the deployment step is simulated using GitHub Actions. In a production environment, this step could deploy the application to platforms such as:

- Render
- Railway
- AWS
- Azure
- Google Cloud

---

## Secrets Management

Sensitive information should never be stored directly in the source code or committed to Git.

Examples of secrets:

- OpenAI API Key
- Anthropic API Key
- Database Password
- JWT Secret
- AWS Access Keys

Instead, GitHub Actions Secrets should be used.

Example:

```
Settings
→ Secrets and Variables
→ Actions
→ New Repository Secret
```

The workflow can access these secrets using:

```yaml
env:
  OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

This keeps credentials secure and prevents accidental exposure.

---

## Rollback Strategy

If a production deployment fails, my first five minutes would focus on restoring service quickly.

### Step 1

Pause further deployments.

### Step 2

Check:

- Application logs
- Deployment logs
- Error rate
- Health endpoints

### Step 3

Rollback to the previous stable deployment.

### Step 4

Verify:

- Application health
- API responses
- Database connectivity

### Step 5

Notify the development team and begin investigating the root cause while the stable version remains online.

---

## Conclusion

Using GitHub Actions with automated testing, secure secrets management, and a clear rollback strategy improves deployment reliability and reduces production risk.