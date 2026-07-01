# ZC_DISP_ENC_TYPE

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ZC_DISP_ENC_TYPE

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | EPIC 2002 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| DISP_ENC_TYPE_C | VARCHAR (66) |  |
| NAME | VARCHAR (254) |  |
| TITLE | VARCHAR (254) |  |
| ABBR | VARCHAR (254) |  |
| INTERNAL_ID | VARCHAR (66) |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DISP_ENC_TYPE_C | D_MYC_ENC_TYPES_F2F | ENC_TYPE_C | Unknown | Unknown | No |  |
