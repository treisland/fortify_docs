---
title: How to Install Fortify VSCode Extension
authors: [treprime]
date: 2023-11-06
categories:
    - IDE
---

Follow this guide to learn how to quickly install the Fortify extension for VSCode.
With this plugin you will be able to scan and review source code vulnerabilities.

<!-- more -->

Two plugins are available for VSCode

- **Fortify Remediation** - this allows a developer to review and audit vulnerabilities
- **Fortify Extensions for Visual Studio** - this allows a user to scan source code and publish scan results to a security dashboard

![Fortify Extensions](https://fortify-7xkpr9a3.s3.us-west-2.amazonaws.com/img/vscode_fortify_extensions.png?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMSJHMEUCIBc8i2zzgs%2Fo38fUTlo0rke9CtsE3rCw4gLdtpBYw%2FHeAiEAph%2BpIqYIDqvPv%2FFHArViBvze%2F%2FKiGySgKhnfKOusbJkqiAMIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARACGgw5OTk5ODA1NTM1MTMiDHjYQFgUtgPOmCogAyrcAgxAp%2BYSfqHLOMW16zFdyq%2BUZsMIZE14kNioKfZ4qdsNXhXkVhaFjxV4NCh1JyMC2AFZamD4prF2WAxbgIAZYTDl4cKwvrtToWo0SfM61d9ZnAzDwRgIfpWtfcBGVbzXGdqgI2G%2BI0Mig81g8A0MXcW23HvmUhNgefXvK7e548B6kN8FujCax%2Ffz8dyWGivBr%2BtBI9LlieVBkh0RYYQ%2FgYdt%2FIok%2FjDDB8y4mDEinUnc5S%2BrZ9BK1DZGGtfsUsBHIFHKyQ%2BiySAZAIWgXge6EXbDNT1EpSKeBMK%2F8JOphg0JzbvulszKFb5MYPQtkKDN%2Fgni7Ex%2F7GlU9MNj%2B53Rg0I2UywlBXAIP2LoUtJbengrYVVI%2FcBYPCHhKxKZeEwCDs2BG%2B6qllrM5bkOQk%2F9HSMcnaWuTzymUBoiLb9wk5Ql5oCYFC9TIQUHa2WrqlokRJ5gIveaWQR%2FOMVuNzDZ9a6qBjqzAkEo262MG8rW4sUgGz05gPA5Sr50kQrjTDHX83pddS4eJS365advrw7e3fULPm1DUrunYuZP2K0uPd8ofN1EMeBg6jOzMclK0%2BZ5SQ9JdACGo%2Bynb4gKizrxRe4tbucNM2UzeLZblziB%2Fbg15DbbA8PwBZD36ytOZYj38giZnGtANAZOnKIvyqdB36FCI3dMkwI0yJ5IGvDp8PtvuIdzdZjUcayPde%2FC%2FpZR8bhbaxZs5tzfMVRg33wqjdA4sSH8o3D%2F0kLdJhl4m4Y%2F%2FCtpeJz4pm%2BO%2BeSxeEX2Pykvo3Gn3QZCV8TepqFw1%2FUXS6ulDziwiQ0rs1S0IdRbJVK6%2BwmLeD%2BqLJg5CLfx2DpNE6D%2BDt0vllSprOmkiH9fQe5d7EeWWgMnlc7bw%2FikoVORS3V1f40%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231108T164954Z&X-Amz-SignedHeaders=host&X-Amz-Expires=299&X-Amz-Credential=ASIA6RU34KUUWWHD4WMO%2F20231108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=6527d5a597576c3ab332e46091735d29fe0354e8fb670eedf772499df3f0cb83)

## Installation Steps
1. Open VSCode and click on the **extensions** icon.
2. Search for **fortify** in the extensions search bar.
3. Click the **install** button either plugin.

![Alt text](https://fortify-7xkpr9a3.s3.us-west-2.amazonaws.com/img/vscode_fortify_extension_icons.png?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMSJHMEUCIBc8i2zzgs%2Fo38fUTlo0rke9CtsE3rCw4gLdtpBYw%2FHeAiEAph%2BpIqYIDqvPv%2FFHArViBvze%2F%2FKiGySgKhnfKOusbJkqiAMIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARACGgw5OTk5ODA1NTM1MTMiDHjYQFgUtgPOmCogAyrcAgxAp%2BYSfqHLOMW16zFdyq%2BUZsMIZE14kNioKfZ4qdsNXhXkVhaFjxV4NCh1JyMC2AFZamD4prF2WAxbgIAZYTDl4cKwvrtToWo0SfM61d9ZnAzDwRgIfpWtfcBGVbzXGdqgI2G%2BI0Mig81g8A0MXcW23HvmUhNgefXvK7e548B6kN8FujCax%2Ffz8dyWGivBr%2BtBI9LlieVBkh0RYYQ%2FgYdt%2FIok%2FjDDB8y4mDEinUnc5S%2BrZ9BK1DZGGtfsUsBHIFHKyQ%2BiySAZAIWgXge6EXbDNT1EpSKeBMK%2F8JOphg0JzbvulszKFb5MYPQtkKDN%2Fgni7Ex%2F7GlU9MNj%2B53Rg0I2UywlBXAIP2LoUtJbengrYVVI%2FcBYPCHhKxKZeEwCDs2BG%2B6qllrM5bkOQk%2F9HSMcnaWuTzymUBoiLb9wk5Ql5oCYFC9TIQUHa2WrqlokRJ5gIveaWQR%2FOMVuNzDZ9a6qBjqzAkEo262MG8rW4sUgGz05gPA5Sr50kQrjTDHX83pddS4eJS365advrw7e3fULPm1DUrunYuZP2K0uPd8ofN1EMeBg6jOzMclK0%2BZ5SQ9JdACGo%2Bynb4gKizrxRe4tbucNM2UzeLZblziB%2Fbg15DbbA8PwBZD36ytOZYj38giZnGtANAZOnKIvyqdB36FCI3dMkwI0yJ5IGvDp8PtvuIdzdZjUcayPde%2FC%2FpZR8bhbaxZs5tzfMVRg33wqjdA4sSH8o3D%2F0kLdJhl4m4Y%2F%2FCtpeJz4pm%2BO%2BeSxeEX2Pykvo3Gn3QZCV8TepqFw1%2FUXS6ulDziwiQ0rs1S0IdRbJVK6%2BwmLeD%2BqLJg5CLfx2DpNE6D%2BDt0vllSprOmkiH9fQe5d7EeWWgMnlc7bw%2FikoVORS3V1f40%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231108T165019Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIA6RU34KUUWWHD4WMO%2F20231108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=122d05865d51cf02368f4e4e89c2695291fd43586a90e87f350b0ba5127be133)

!!! success "**CONGRATULATIONS! YOU'VE SUCCESSFULLY INSTALLED THE FORTIFY EXTENSION(S) FOR VISUAL STUDIO CODE**"