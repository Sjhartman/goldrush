# FEE_BILLING_SETTINGS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=FEE_BILLING_SETTINGS

## Description

This table is used to specify processing fees for outpatient pharmacy work requests.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | PHR |
| Release Version | Rel May 2020 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| PHARMACY_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the pharmacy record. |
| LINE | INTEGER | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| FEE_TYPE_C | INTEGER |  |
| FEE_ITEM_ID | VARCHAR (18) | This item specifies the fee record ID in a pharmacy fee configuration entry. |
| DELIVERY_METHOD_C | INTEGER |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PHARMACY_ID | RX_PHARMACY_SETTINGS | PHARMACY_ID | No | No | No |  |
| 1 | PHARMACY_ID | RX_PHR | PHARMACY_ID | No | No | No |  |
| 1 | PHARMACY_ID | RX_PHR_2 | PHARMACY_ID | No | No | No |  |
| 1 | PHARMACY_ID | RX_PHR_3 | PHARMACY_ID | No | No | No |  |
| 1 | PHARMACY_ID | RX_PHR_CENTRAL_FILL | PHARMACY_ID | No | No | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | FEE_TYPE_C | ZC_FEE_TYPE | FEE_TYPE_C | No | No | No |  |
| 6 | FEE_ITEM_ID | OR_SPLY | SUPPLY_ID | No | No | No |  |
| 6 | FEE_ITEM_ID | V_CUBE_D_SUPPLY | SUPPLY_ID | Unknown | Unknown | No |  |
| 7 | DELIVERY_METHOD_C | ZC_DELIVERY_METHOD | DELIVERY_METHOD_C | No | No | No |  |
