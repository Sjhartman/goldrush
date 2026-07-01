# AUDIT_SESSION

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=AUDIT_SESSION

## Description

The AUDIT_SESSION table contains the basic information of each audit session common to all audit sessions.  Additional information is stored in platform specific tables based on the platform of the audit session.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | APPEND |
| Load Frequency | AUDIT |
| Chronicles INI | N/A |
| Release Version | Rel 2015 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| AUDIT_SESSION_ID | No | The unique ID of the audit session. |
| AUDIT_PLATFORM_C | No | The platform used to access the system for the audit session.  This determines which additional tables if any will have more information about the audit session. |
| SESSION_START_UTC_DTTM | No | The moment the audit session was created |
| SESSION_UPDATE_UTC_DTTM | No | The moment the audit session was last updated |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | AUDIT_PLATFORM_C | ZC_AUDIT_PLATFORM | AUDIT_PLATFORM_C | No | Yes | No |  |
