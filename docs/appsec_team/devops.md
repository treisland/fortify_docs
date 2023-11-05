---
title: DevOps
---

# Bridge the Gap: The DevOps Engineer's Role in Application Security and Build Pipelines

A DevOps engineer plays a crucial role in integrating application security practices into the software development and deployment process. This is essential to ensure that the applications being developed are robust and secure from vulnerabilities. 

Below is a general outline for the responsibilities of a DevOps engineer in this context.

## Application Security

### Vulnerability Assessment

- **Integration**: The DevOps engineer integrates Fortify into the development process, ensuring that the application's source code is regularly scanned for security vulnerabilities.
- **Automated Scanning**: Configures automated scans at different stages of development (e.g., during code commits, pull requests, or continuous integration) to detect vulnerabilities early in the development lifecycle.

### Policy Compliance

- **Defining Policies**: Collaborates with security experts to establish security policies in Fortify that match the organization's security requirements.
- **Policy Enforcement**: Ensures that Fortify scans enforce these policies and flag violations in the code.

### Reporting and Feedback

- **Dashboard Setup**: Sets up dashboards to provide visibility into the security status of the application, making it easy for developers and stakeholders to understand and track security findings.
- **Feedback Loop**: Works with development teams to address and remediate identified security issues and vulnerabilities.

## Build Pipelines

### Continuous Integration/Continuous Deployment (CI/CD)
- **Integration with CI/CD Tools**: The DevOps engineer integrates Fortify into the CI/CD pipeline, enabling automatic security scanning as part of the build and deployment process.

### Automation
- **Automation Scripts**: Creates automation scripts to trigger Fortify scans, analyze results, and make pass/fail decisions within the build pipeline.
- **Integration Testing**: Ensures that security testing is an integral part of the testing and deployment process.

### Artifact Promotion and Deployment
- **Conditional Promotion**: Defines conditional promotion criteria to prevent insecure artifacts from progressing to higher environments (e.g., staging or production).
- **Deployment Gates**: Sets up gates in the deployment pipeline to halt or alert when critical security vulnerabilities are detected.

In summary, a DevOps engineer's role in application security and build pipelines is to bridge the gap between development and security by integrating security tools like Fortify into the development workflow. They ensure that security is not an afterthought but an integral part of the software development process. By doing so, they help to identify and remediate vulnerabilities early, reduce security risks, and enable the delivery of more secure software products.
