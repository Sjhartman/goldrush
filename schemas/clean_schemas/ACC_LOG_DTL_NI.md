# ACC_LOG_DTL_NI

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ACC_LOG_DTL_NI

## Description

The ACC_LOG_DTL_NI table contains the supplementary information of the activities which were recorded in the ACCESS_LOG table, such as pairs of mnemonics and their responding values for non-indexed items.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | APPEND |
| Load Frequency | AUDIT |
| Chronicles INI | N/A |
| Release Version | MU13 - MAY 2001 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| ACCESS_INSTANT | No | The UTC instant when this access history event was logged into the system. This value may be on or after the time the event actually occurred, which is stored in ACCESS_LOG.ACCESS_TIME. |
| PROCESS_ID | No | The unique ID of the Cach? process for the Hyperspace connection to Chronicles. |
| DATA_MNEMONIC_ID | No | The unique ID of the single value data mnemonic corresponding to this access history event. This mnemonic and the corresponding INTEGER_VALUE or STRING_VALUE columns provide additional information about the access history event. |
| STRING_VALUE | No | The string value that qualifies the data mnemonic. For example, a data mnemonic of PROVIDER (Provider ID) could have a string value of 'EPIC123'.  This field will be populated for both numeric and non-numeric values. |
| INTEGER_VALUE | No | The integer value that qualifies the data mnemonic. For example, a data mnemonic of ACCOUNT (Guarantor Account ID) could have an integer value of 12345.  If the corresponding data contains non-numeric characters, this field will be null. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | DATA_MNEMONIC_ID | ACCESS_LOG_MNEM | DATA_MNEMONIC_ID | Unknown | Unknown | Yes |  |
