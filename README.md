# Low Code laboratory records

Records prepared for the Insurance Claim Management application, 19 October 2026.

## Completion status

PDF availability does not mean that every practical exercise has passed its live acceptance tests. Each record states its evidence boundary.

| Experiment | Record | Practical status |
| --- | --- | --- |
| 6 | Workflow automation | Earlier focused live tests documented. Payout integration remains paused. |
| 7 | Zoho service integration | Procedure and Deluge example prepared. OAuth authorization and successful API call pending. |
| 8 | Users and RBAC | Proposed role matrix plus existing Blueprint permission evidence. Exact role assignments and independent-user tests pending. |
| 9 | Zia and analytics | Exploration documents observed Zia failure and existing chart evidence. Successful new AI generation is unverified. |
| 10 | Performance optimization | Procedure and tested local algorithm illustration. Creator timings, subform migration and backend indexing pending. |
| 11 | Development to Production | Release procedure and tests prepared. Native Stage/Production publication pending. |
| 12 | Security and governance | Existing guards and custom audit evidence documented. Native Audit Trail, separate-user tests and restore test pending. |
| 13 | Low-code limitations | Hypothetical enterprise case study completed. |
| 14 | Pro-code extension | Custom-function route uses existing direct-execution and Blueprint evidence. Catalyst deployment is outside this route. |
| 15 | Careers and future | Literature-based report and eight-slide presentation completed. |

The records contain aims, procedures, design tables, validation or discussion, results and official documentation links. Cover pages contain the experiment heading only. Screenshots are existing captured evidence and are labelled accordingly. Illustrative code is not represented as a newly deployed function.

## Experiment 15 presentation

- `EXP-15-Career-Presentation.pptx`: editable slides and speaker notes with references.
- `EXP-15-Career-Presentation.pdf`: visual slide companion.

## Local performance illustration

`support/exp10_lookup_benchmark.py` reproduces the Python lookup comparison. The JSON contains the measured run used in the record. These are local algorithm timings, not Zoho Creator measurements. Dictionary construction is excluded from the timed lookup comparison.

No real payout, additional email send, new connection authorization or native production deployment was performed during this record-preparation session.
