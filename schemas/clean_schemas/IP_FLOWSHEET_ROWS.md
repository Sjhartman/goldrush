# IP_FLOWSHEET_ROWS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=IP_FLOWSHEET_ROWS

## Description

This table contains flowsheet row (FLO) data for an encounter. This table is a key table in tying LDA assessment row lines in flowsheet data records to the LDAs, and the necessary joins are: IP_FLOWSHEET_ROWS.IP_LDA_ID with IP_LDA_NOADDSINGLE.IP_LDA_ID IP_FLOWSHEET_ROWS.INPATIENT_DATA_ID with IP_FLWSHT_REC.INPATIENT_DATA_ID IP_FLOWSHEET_ROWS.LINE with IP_FLWSHT_MEAS.OCCURANCE IP_FLWSHT_REC.FSD_ID with IP_FLWSHT_MEAS.FSD_ID.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | INP |
| Release Version | EPIC 2002 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| INPATIENT_DATA_ID | VARCHAR (18) | The unique ID of the inpatient data store record. |
| LINE | INTEGER | The line count for the item. |
| FLO_MEAS_ID | VARCHAR (18) | The unique ID of the flowsheet group/row. |
| ROW_TEMPLATE *(deprecated)* | VARCHAR (254) | The flowsheet row templates. It is an up caret ('^') delimited list of IDs.  Note that this column does not contain data for any records in the table. Look to the IP_FS_ROW_TEMPLATE table instead. |
| ROW_VARIANCE_NAME *(deprecated)* | VARCHAR (50) |  |
| FLOWSHT_ROW_NAME | VARCHAR (510) | The flowsheet row name. Especially comes into play when a custom name is given to a duplicable row/group, either by a user typing it upon manually adding a row/group or from the order that fired the task template which added the duplicable row/group. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record.  Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record.  Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| ORDER_ID *(deprecated)* | VARCHAR (254) | Order IDs that were added to the patient's flowsheet row. It is an up caret ('^') delimited list of IDs.  This column has been deprecated. Use column IP_FS_ORD_IX_ID.IX_FLOW_RW_ORD_ID instead. |
| IP_LDA_ID | VARCHAR (18) | Stores the Lines/Drains/Airways (LDA) ID for the flowsheet group. |
| ROW_VARIANCE_C | INTEGER |  |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_FLOWSHEET_ROWS_LDA_ID | IP_LDA_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | INPATIENT_DATA_ID | IP_DATA_STORE | INPATIENT_DATA_ID | No | No | No |  |
| 3 | FLO_MEAS_ID | FLO_CNTX_INFO | ID | No | No | No |  |
| 3 | FLO_MEAS_ID | IP_FLO_GP_DATA | FLO_MEAS_ID | No | No | No |  |
| 3 | FLO_MEAS_ID | IP_FLO_GP_DATA_2 | FLO_MEAS_ID | No | No | No |  |
| 7 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 7 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 8 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 8 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 8 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 10 | IP_LDA_ID | IP_LDA_NOADDSINGLE | IP_LDA_ID | Unknown | No | No |  |
| 10 | IP_LDA_ID | LDA_SHARE_WITH_PAT | IP_LDA_ID | No | No | No |  |
| 10 | IP_LDA_ID | V_IP_PAT_CENT_LINE | IP_LDA_ID | Unknown | Unknown | No |  |
| 10 | IP_LDA_ID | V_IP_PAT_UMB_LINE | IP_LDA_ID | Unknown | Unknown | No |  |
| 10 | IP_LDA_ID | V_IP_PAT_URIN_CATH | IP_LDA_ID | Unknown | Unknown | No |  |
| 11 | ROW_VARIANCE_C | ZC_ROW_VARIANCE | ROW_VARIANCE_C | No | No | No |  |
