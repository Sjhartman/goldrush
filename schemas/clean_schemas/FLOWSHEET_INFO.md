# FLOWSHEET_INFO

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=FLOWSHEET_INFO

## Description

This table contains details about the review flowsheet or synopsis records in your system, namely what kind of information a flowsheet row will display. This table also stores whether there is a custom header for the flowsheet and whether there is a maximum width for cells in the flowsheet.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | FSH |
| Release Version | Rel 2010 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| FLOWSHEET_ID | NUMERIC (18,0) | The unique identifier (.1 item) for the flowsheet record. |
| CONTACT_DATE_REAL | No | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| LINE | No | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| VERSION_DATE | DATETIME | The date of this contact in calendar format. |
| SOURCE_ID | NUMERIC (18,0) | This cloumn determines the kind of data that the flowsheet row will display, for example documentation flowsheet values, result component values, values from EPT items, etc. |
| WHAT | VARCHAR (254) | This item works in conjunction with item 200 (Source).  Once the source is defined, this coulumn specifically defines the data that will be displayed for the flowsheet row.  For example, if a source of documentation flowsheet values is chosen, this item would hold the specific documentation flowsheet row whose values should be displayed in the flowsheet. |
| HEADER_OVERRIDE | VARCHAR (254) | Allows you to set a custom header for your flowsheet row. |
| MAXIMUM_WIDTH | INTEGER | Specify the maximum width for a cell in this flowsheet row.  The number you enter is the number of average width characters to be shown in the cell.  Any truncated text can be viewed by double clicking the cell. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FLOWSHEET_ID | FLOWSHEET | FLOWSHEET_ID | No | No | No |  |
| 1 | FLOWSHEET_ID | FLOWSHEET_VERSIONS | FLOWSHEET_ID | No | No | No |  |
| 2 | CONTACT_DATE_REAL | VERSION_DATE_REAL |  |  |  |  |  |
| 5 | SOURCE_ID | FLOWSHEET_PART | PART_ID | No | No | No |  |
