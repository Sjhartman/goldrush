# DOCUMENT_OCR

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=DOCUMENT_OCR

## Description

This table contains textual information for a media file that has been accumulated through optical character recognition.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | DCS |
| Release Version | Rel November 2020 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| DOCUMENT_ID | VARCHAR (18) | The unique ID of the scaned document for this row. |
| LINE | INTEGER | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| OCR_WORD | VARCHAR (450) | A word found within the scanned document. |
| OCR_WORD_PAGE | INTEGER | The page number the word was found on. |
| OCR_WORD_X_POS | INTEGER | The x-coordinate for the top left corner of the word in pixels. |
| OCR_WORD_Y_POS | INTEGER | The y-coordinate for the top left corner of the word in pixels. |
| OCR_WORD_WIDTH | INTEGER | The width of the word in pixels. |
| OCR_WORD_HEIGHT | INTEGER | The height of the word in pixels. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DOCUMENT_ID | AWM_IMAGE_DATA | DOCUMENT_ID | No | No | No |  |
| 1 | DOCUMENT_ID | DOC_INFORMATION | DOC_INFO_ID | No | No | No |  |
| 1 | DOCUMENT_ID | DOC_INFORMATION_2 | DOCUMENT_ID | No | No | No |  |
| 1 | DOCUMENT_ID | DOC_INFORMATION_3 | DOCUMENT_ID | No | No | No |  |
| 1 | DOCUMENT_ID | DOC_INFORMATION_4 | DOC_INFO_ID | No | No | No |  |
| 1 | DOCUMENT_ID | DOC_INFO_DICOM | DOCUMENT_ID | No | No | No |  |
| 1 | DOCUMENT_ID | DOC_MC_BROKER_EOP | DOCUMENT_ID | No | No | No |  |
| 1 | DOCUMENT_ID | IMG_ANNOT_SRC | DOCUMENT_ID | No | No | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
