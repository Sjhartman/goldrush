# ORDER_RES_PATH

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ORDER_RES_PATH

## Description

Stores the pathology codes and malignancy types attached to a pathology result on an order.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | RES |
| Release Version | SUMMER 2005 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| FINDING_ID | NUMERIC (18,0) | The unique ID of the finding record corresponding to this result. |
| LINE | No | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this Chronicles record. This is populated only if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this Chronicles record was extracted. This is populated only if you use IntraConnect. |
| PATH_CODES_C | INTEGER |  |
| MALIGNANCY_TYPE_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FINDING_ID | ANATOMY_NOADD | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | AUDIOGRAM_METADATA | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | AUDIOLOGY_ORDER_LINK | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | DENTAL_FINDING_NOADD | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | DENTAL_HB_ESTIMATES | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | DENTAL_PROC_NOADD | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | DENTAL_VOUCHER_FEES | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | DERM_SKINEXAM_FINDING | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | HOMUNCULUS_INP_EXAM_DATA | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | ORDER_RES | FINDING_ID | Unknown | No | No |  |
| 1 | FINDING_ID | ORDER_RES_2 | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | ORDER_RES_3 | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | ORDER_RES_CV_ORD | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | ORDER_RES_CV_RRT_ORDER | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | ORDER_RES_FOLLOWUP | FINDING_ID | Unknown | No | No |  |
| 1 | FINDING_ID | ORDER_RES_LOG | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | ORD_CV_FINDING | CV_FINDING_ID | Unknown | No | No |  |
| 1 | FINDING_ID | ORD_IOL | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | ORD_RES_BLOOD | FINDING_ID | Unknown | No | No |  |
| 1 | FINDING_ID | RES_FETALWEIGHT | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | RES_MAMMO_CUI_VALS | FINDING_ID | No | No | No |  |
| 1 | FINDING_ID | V_FINDINGS_ALL | FINDING_ID | Unknown | Unknown | No |  |
| 1 | FINDING_ID | V_ORDER_RES_IMG_STATUS | FINDING_ID | Unknown | Unknown | No |  |
| 1 | FINDING_ID | V_RIS_LESION | LESION_ID | Unknown | Unknown | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |

_(32 total; showing first 30)_
