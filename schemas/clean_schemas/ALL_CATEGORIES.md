# ALL_CATEGORIES

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=ALL_CATEGORIES

## Description

This table contains information from all category items. Use this table to get the name, title, or abbreviation of any category list value given the corresponding INI and ITEM for the category list. Shared category lists will have a row for each category value (VALUE_C) from the source INI and ITEM, and those rows will be duplicated for each INI and ITEM combination that points to the same category list. For example, the category list for I ORD 30 is shared with I OTP 30. Category 999-Medications will appear once in this table for INI='ORD', ITEM=30; and will appear once in this table for INI='OTP', ITEM=30.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | Rel 2018 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| INI | No | The INI of the master file which contains the item that either stores or references the category list. |
| ITEM | No | The item number in the master file (INI) which either stores or references the category list. |
| VALUE_C | No | The category value. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| NAME | No | The name of the category value. |
| TITLE | No | The title of the category value. This is the name in all caps. |
| ABBR | No | The abbreviation for the category value. |
| INTERNAL_ID | No | The internal ID of the category value. |
| IS_ACTIVE_YN | No | Indicates whether the category value is active. Displays "Y" if the value is active. Displays "N" if the value is inactive. |
