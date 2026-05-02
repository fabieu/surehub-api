# Security Policy

## Supported Versions

Only the latest release receives security fixes. Older versions are not actively patched.

| Version  | Supported |
|----------|-----------|
| Latest   | Yes       |
| < Latest | No        |

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Report vulnerabilities privately
via [GitHub Security Advisories](https://github.com/fabieu/surehub-api/security/advisories/new).

Include as much of the following as possible:

- Type of vulnerability (e.g., credential exposure, injection, SSRF)
- Steps to reproduce or a proof-of-concept
- Affected component and version
- Potential impact

## Response Timeline

| Milestone          | Target                |
|--------------------|-----------------------|
| Acknowledgement    | Within 48 hours       |
| Initial assessment | Within 7 days         |
| Fix or mitigation  | Dependent on severity |

You will be credited in the release notes unless you request otherwise.

## Scope

This project proxies requests to the Sure Petcare API using credentials supplied by the user. Keep in mind:

- Credentials (`SUREHUB_EMAIL`, `SUREHUB_PASSWORD`) are passed as environment variables — never commit them to version
  control.
- CORS is disabled by default; enabling `SUREHUB_CORS=*` broadens the attack surface.
- This API is intended for local or trusted-network use. Exposing it publicly without authentication is not recommended.
