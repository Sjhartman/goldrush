# CHILD_NOTE_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CHILD_NOTE_INFO

## Description

The CHILD_NOTE_INFO table contains information about child notes that are linked to clinical notes. Each row represents one child note and contains information such as the user that created the link, when the link was created, and what type of link it is.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | HNO |
| Release Version | Rel 2014 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| NOTE_ID | VARCHAR (254) | The unique identifier for the note record. |
| LINE | INTEGER | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| TEXT_NOTE_CSN_ID | NUMERIC (18,0) | This holds the note contact serial number (CSN) pointer to the record where the child note's text can be found. Any workflow that links a child note to a clinical note must populate this item with the pointer to the child note contact. |
| LINK_TYPE_C | INTEGER |  |
| LINK_USER_ID | VARCHAR (18) | Contains the user ID of the user who added the corresponding child note. Any workflow that links a child note to a clinical note must specify the user adding the link in this item. |
| LINK_UTC | DATETIME (UTC) | Holds the instant, in UTC format, that the child note was added to the note. Any workflow that links a child note to a clinical note must populate this item with the UTC timestamp of when the link was added. |
| SOURCE_NOTE_CSN_ID | NUMERIC (18,0) | Contains the note contact serial number (CSN) of the source contact the child note was originally added to. Any workflow that links a child note to a clinical note must specify which contact on the parent clinical note the child note applies to. |
| LINK_DTTM | DATETIME (Local) | Holds the instant, in local time zone format, that the child note was added to the note. This item is automatically calculated based on the Child Note - Instant (UTC) item (I HNO 34253). |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | NOTE_ID | ABN_NOTES | ABN_NOTE_ID | Unknown | No | No |  |
| 1 | NOTE_ID | ABN_NOTE_INFO | NOTE_ID | No | No | No |  |
| 1 | NOTE_ID | CODING_CLA_NOTES | NOTE_ID | Unknown | No | No |  |
| 1 | NOTE_ID | FA_NOTES_QUERY | NOTE_ID | No | No | No |  |
| 1 | NOTE_ID | FIN_ASST_LETTER | NOTE_ID | No | No | No |  |
| 1 | NOTE_ID | FIN_ASST_NOTE | NOTE_ID | No | No | No |  |
| 1 | NOTE_ID | HNO_CVG_REQUEST | NOTE_ID | Unknown | No | No |  |
| 1 | NOTE_ID | HNO_INFO | NOTE_ID | No | No | No |  |
| 1 | NOTE_ID | HNO_INFO_2 | NOTE_ID | No | No | No |  |
| 1 | NOTE_ID | HNO_MYC_LET_INFO | NOTE_ID | No | No | No |  |
| 1 | NOTE_ID | HSP_ACCT_LETTERS | NOTE_ID | Unknown | No | No |  |
| 1 | NOTE_ID | HSP_ACCT_NOTES | NOTE_ID | Unknown | No | No |  |
| 1 | NOTE_ID | LETTER_EXTERNAL_INFO | NOTE_ID | No | No | No |  |
| 1 | NOTE_ID | NOTES_ACCT | NOTE_ID | Unknown | No | No |  |
| 1 | NOTE_ID | NOTES_LAB | NOTE_ID | Unknown | No | No |  |
| 1 | NOTE_ID | NOTES_MC_CLM | NOTE_ID | Unknown | Unknown | No |  |
| 1 | NOTE_ID | NOTES_MC_PBA | NOTE_ID | No | No | No |  |
| 1 | NOTE_ID | NOTES_MC_SER | NOTE_ID | Unknown | Unknown | No |  |
| 1 | NOTE_ID | NOTE_PARENT_NOTE | NOTE_ID | No | No | No |  |
| 1 | NOTE_ID | PATIENT_FYI_FLAGS | NOTE_ID | Unknown | No | No |  |
| 1 | NOTE_ID | REG_HX_NOTES | NOTE_ID | Unknown | No | No |  |
| 1 | NOTE_ID | SAVED_LETTER_HNO | NOTE_ID | Unknown | No | No |  |
| 1 | NOTE_ID | V_EHI_PBA_NOTES_MC_PBA | NOTE_ID | Unknown | Unknown | No |  |
| 1 | NOTE_ID | V_NOTE_CHARACTERISTICS | NOTE_ID | Unknown | Unknown | No |  |
| 1 | NOTE_ID | V_NOTE_SHARE_W_PAT_INFO | NOTE_ID | Unknown | Unknown | No |  |
| 1 | NOTE_ID | V_NOTE_VIEW_INFO | NOTE_ID | Unknown | Unknown | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |

_(55 total; showing first 30)_
