# HSP_ISOLATION

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=HSP_ISOLATION

## Description

*** Deprecated *** This view is deprecated in favor of the ISOLATIONS table as that now includes all isolations. ****** The HSP_ISOLATION view contains information on documented patient isolations. This is a continuity view supporting a data conversion of isolations from the patient masterfile to a new isolation masterfile. Each row is a documented isolation for a patient. The data is stored in tables HSP_ISOLATION_REPL, which is a copy of the original HSP_ISOLATION table, and ISOLATIONS, which stores the converted data. Isolations are de-duplicated between the source tables so they only appear once in the view. This continuity view will be deprecated in the Aug 23 version. Reports should be migrated to use the ISOLATIONS table.

## Metadata

| Property | Value |
| --- | --- |
| Type | View |
| Release Version | EPIC 2000 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PAT_ID | .1 | The ID of the patient with this isolation. |
| PAT_ENC_DATE_REAL | FLOAT | This is a numeric representation of the date of this contact in your system. The integer portion of the number specifies the date of the contact. The digits after the decimal point indicate multiple contacts on one day. |
| LINE | No | The line number of the isolation for the patient. To preserve a unique CSN/line number pair in the view, this will be the isolation ID for data from ISOLATIONS, and the negative line number for data from HSP_ISOLATION_REPL. |
| ISOLATION_C | 10370 |  |
| ISO_ADDED_TIME | 10471 | The date and time the isolation was added for the patient. |
| ISO_ADDED_USER_ID | 10472 | The ID of the employee who added the isolation for the patient. |
| ISO_RMVD_TIME | 10473 | The date and time the isolation was removed from the patient. |
| ISO_RMVD_USER_ID | 10474 | The ID of the employee who removed the isolation for the patient. |
| ISO_ORDER_ID | 10475 | The ID of the order diagnosis of the isolation for the patient. |
| ISO_CMNT | 10479 | User-entered comments about the isolation for the patient. |
| CM_CT_OWNER_ID | VARCHAR (25) | ID of the deployment owner for this contact. |
| PAT_ENC_CSN_ID | 8 | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
