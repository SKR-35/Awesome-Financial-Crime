# Changelog

All notable changes to this project will be documented in this file.

## [v1.4.0] - 2026-10-04

### Changed

- Redesigned resource links using compact inline badges to improve readability and reduce README length.
- Standardized website links using consistent `Website | Link` badges.
- Standardized GitHub repository links using consistent `Code | GitHub` badges.
- Added labeled badge variants for resources containing multiple repositories or multiple external links.
- Standardized mixed multi-link resources while preserving clear identification of individual destinations.
- Standardized pull request link formatting to align with the repository's updated link presentation.
- Consolidated resource descriptions and links onto single lines where practical, improving information density and scanability.
- Corrected resource URLs identified during the badge migration.

### CI / Quality

- Verified the redesigned badge links with the existing automated README link-check workflow.
- Confirmed the updated README passes link validation after the badge migration.

## [v1.3.0] - 2026-08-29

### Added

- Expanded technical resources for transaction monitoring, including Apache Flink, Drools, Apache Kafka and Apache Spark.
- Expanded trade surveillance resources with TimescaleDB, QuestDB, Apache Kafka and Polars.
- Expanded KYC/KYB resources with Great Expectations, OpenSanctions, Splink and RapidFuzz.
- Added a substantially expanded **Regulations, Standards & Guidance** section covering:
  - Global AML/CFT standards and guidance.
  - Banking and industry guidance.
  - Sanctions.
  - Market abuse.
  - Anti-bribery and corruption.
  - Financial intelligence.
- Added an automated README link-check workflow using Lychee.
- Added a Python-based release document builder for reproducible Markdown → XeLaTeX → PDF generation.
- Added pytest coverage for the release document builder.
- Added a dedicated GitHub Actions workflow for Python tests.
- Added `.gitignore` rules for generated documentation artifacts and Python cache files.

### Changed

- Renamed the project from **Awesome FCC** to **Awesome Financial Crime** to provide clearer and broader domain positioning.
- Improved repository terminology and branding to align with the new project name.
- Improved the generated release document layout with a native Contents section and a page break before the main content.
- Updated and corrected resource links identified during automated link validation.

### CI / Quality

- Added automated link validation for README resources.
- Added automated Python unit testing for release-document tooling.
- Added a targeted exclusion for FATF URLs that reject automated link-check clients with HTTP 403 responses.
- Validated the release document builder with 5 passing pytest tests.
- Confirmed GitHub Actions workflows are green for the v1.3.0 release.

### Release Artifacts

- Added reproducible XeLaTeX source generation for release documentation.
- Added PDF generation from the generated XeLaTeX source.
- Prepared both `.tex` and `.pdf` documentation artifacts for the v1.3.0 GitHub Release.