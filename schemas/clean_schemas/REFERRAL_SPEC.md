# REFERRAL_SPEC

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=REFERRAL_SPEC

## Description

This table contains information on the specialties for referring providers.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | REF |
| Release Version | Rel 2014 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| REFERRING_PROV_ID | VARCHAR (18) | The unique ID of the referring provider. |
| LINE | INTEGER | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| RFL_SPECIALTY_C | VARCHAR (66) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | REFERRING_PROV_ID | REFERRAL_SOURCE | REFERRING_PROV_ID | No | No | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | RFL_SPECIALTY_C | SPECIALTY_HCFA_CODE | SPECIALTY_C | Unknown | No | No |  |
| 5 | RFL_SPECIALTY_C | ZC_PREF_PCP_SPEC | PREF_PCP_SPEC_C | No | No | No |  |
| 5 | RFL_SPECIALTY_C | ZC_REQUESTED_SPEC | REQUESTED_SPEC_C | No | No | No |  |
| 5 | RFL_SPECIALTY_C | ZC_RFL_PROV_SPEC | PROV_SPEC_C | No | No | No |  |
| 5 | RFL_SPECIALTY_C | ZC_SPECIALTY | SPECIALTY_C | No | No | No |  |
