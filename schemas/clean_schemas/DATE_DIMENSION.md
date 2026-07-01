# DATE_DIMENSION

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=DATE_DIMENSION

## Description

This table is similar to a typical Data Warehouse "Date Dimension". Link your dates to this table to avoid processing date functions on the reporting server. When you use your reporting tool's date functions to do filtering, all rows will usually be returned to your reporting tool and stored in memory while the tool runs date functions to eliminate rows that don't meet your criteria. This can be very slow. This table helps eliminate that necessity and helps you treat your Clarity database like a data warehouse.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | ON DEMAND |
| Chronicles INI | N/A |
| Release Version | SPRING 2008 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| CALENDAR_DT | No | The date in normal date format. |
| DAY_OF_WEEK | No | Monday, Tuesday, etc. |
| WEEK_NUMBER | No | The number of the week in the year. Depends on the locale definition. |
| WEEK_ENDING_DT | No | The last day of the week in normal date format. Depends on the locale definition. |
| LAST_FRIDAY_DT | No | The last occurrence that month of the last business day of the week.  This may or may not be a Friday, depending on the locale definition.  Used to help determine the last full business week of the month. |
| MONTH_END_DT | No | This is the last day of the month. For example, 02/28/2007. |
| DAY_OF_MONTH | No | This is the "day" part of the date only. For example, if the date is May 13, this column contains "13". |
| MONTH_NAME | No | The month name in long form. For example, "February". |
| MONTH_NUMBER | No | The month in integer form. For example, February will be "2". |
| QUARTER_NUMBER | No | This column contains the yearly quarter number in integer form. For example, February is in Quarter 1 while November is in Quarter 4. |
| DAY_OF_YEAR | No | This column contains the Nth day of the year. For example, January 1 will be day 1 and December 31 will normally be day 365. |
| EPIC_DTE | No | The OLTP database stores some dates in an internal integer format known as the DTE. The DTE increases as time goes on. This column contains the DTE. |
| EPIC_DAT | No | Much of the date information stored in the OLTP system is in an integer format known as DAT. The DAT is equal to 121531-DTE. The DAT decreases as time goes on. This column contains the DAT. |
| INSTANT_AT_MIDNIGHT | No | Much of the datetime information in the OLTP system is stored in a format that represents a numeric number of seconds called an Instant. This column contains the Instant of a particular day at 12AM. The ACCESS_LOG tables have an indexed (PK) column that is in this format. |
| YEAR | No | This column contains the four-digit year. |
| OCCURRENCE_IN_MONTH | No | This column tells you how many times a particular day of the week has occurred in the given month. Use this column to find--for example--the fourth Tuesday of the month. |
| TOMORROW_DT | No | This is the date of the next day. Use this column to help linking datetime values. For example, CONTACT_DATE>=CALENDAR_DT and CONTACT_DT<TOMORROW_DT |
| YEAR_MONTH | No | To help group by month, this column contains the month and year. The format is YYYYMM. |
| WEEKEND_YN | No | Contains "Y" for weekend days. Otherwise, contains "N". Depends on the locale definition. |
| QUARTER_BEGIN_DT | No | This date is the first day of the quarter. |
| QUARTER_END_DT | No | This date is the last day of the quarter. |
| SAME_DAY_YEAR_AGO | No | This column returns the date of a year ago. If CALENDAR_DT=2/24/2009, then this column will return 2/24/2008. If CALENDAR_DT is Feb. 29th, then this column returns nothing. |
| PREV_DAY_DT | No | This is the previous day's date. |
| LEAP_YEAR_YN | No | This column shows whether this year is a leap year. |
| DAY_OF_THE_WEEK_C | No | The category number of the day of the week. The values in this column start at 0 for Thursday and end at 6 for Wednesday. You can join to this column from day of the week columns based on ZC_DAY_OF_THE_WEEK, or with a Format INI of "SCH" and a Format Item of "130".   If the other column is based on ZC_WHICH_DAYS or has a Format INI of "ECT" and a Format Item of "710", use WHICH_DAYS_C instead. |
| YEAR_OF_THE_WEEK | No | The four-digit year that the WEEK_NUMBER corresponds to.  Depending on where in the week the new year starts and the locale definition, this may be the year before or after the actual date.  For instance, December 31st may be considered part of the first week of the following year. |
| YEAR_BEGIN_DT | No | The first day of the year for the date in datetime format. |
| MONTH_BEGIN_DT | No | The first day of the month for the date in datetime format. |
| YEAR_BEGIN_DT_STR | No | The first day of the year as a string, in the format 'YYYY-MM-DD'. |
| MONTH_BEGIN_DT_STR | No | The first day of the month as a string, in the format 'YYYY-MM-DD'. |
| CALENDAR_DT_STR | No | The date formatted as a string, in the format 'YYYY-MM-DD'. |
| QTR_BEGIN_DT_STR | No | The first day of the quarter formatted as a string, in the format 'YYYY-MM-DD'. |
| WEEK_BEGIN_DT | No | The first day of the week in datetime format. |
| WEEK_BEGIN_DT_STR | No | The first day of the week as a string, in the format 'YYYY-MM-DD'. |
| DAY_OF_WEEK_INDEX | No | Contains a number representing the day of the week in the current locale for the corresponding CALENDAR_DT. The first day of the week is 0 and the last day of the week is 6.  For example, Sunday is the first day of the week in the United States. So Sunday would be 0 and Saturday would be 6 in this column. |
| HOLIDAY_YN | No | Indicates whether the date is a holiday. "Y" represents that the date is a holiday, otherwise a value of "N" will appear. Depends on the locale definition. |
| MONTHNAME_YEAR | No | This column contains the month and year in 'MonthName YYYY' format. For example, if the CALENDAR_DT is 2012-01-31, this column would display 'January 2012'. |
| YEAR_QUARTER | No | This column contains the year and quarter information in the format 'YYYY Q#'. |
| YEAR_MONTH_STR | No | This column contains the year and month number as a string in the format 'YYYY-MM'. |
| QUARTER_STR | No | This column contains the quarter number as a string in the format 'Q#'. |
| BUS_DAY_CT | No | This column contains a number representing the number of business (non-weekend, non-holiday) days since 1850-01-01. This column will take into consideration holidays that are set at the Service Area or Location level, but not those set at the Department level. |
| WEEKDAY_CT | No | This column contains a number representing the number of weekdays since 1850-01-01. This column does not take holidays into consideration. |
| USA_FISCAL_YEAR_BEGIN_DT | No | This column contains the first date of the United States federal fiscal year.  The U.S. federal fiscal year currently begins on 1 October and ends on 30 September.  The current fiscal year went into effect on 1 October 1976; this column is not accurate for dates prior to 1 October 1976. |
| USA_FISCAL_YEAR_END_DT | No | This column contains the last date of the United States federal fiscal year.  The U.S. federal fiscal year currently begins on 1 October and ends on 30 September.  The current fiscal year went into effect on 1 October 1976; this column is not accurate for dates prior to 1 October 1976. |
| YEAR_END_DT | No | The last date of the year for the CALENDAR_DT. |
| WHICH_DAYS_C | No | The category number of the day of the week. The values in this column start at 1 for Sunday and end at 7 for Saturday. You can join to this column from day of the week columns based on ZC_WHICH_DAYS, or with a Format INI of "ECT" and a Format Item of "710".   If the other column is based on ZC_DAY_OF_THE_WEEK or has a Format INI of "SCH" and a Format Item of "130", use DAY_OF_THE_WEEK_C instead. |
| MONTH_END_YN | No | Indicates whether or not the date in this row is the last day of a month.  This is frequently used as a filter and should be used instead of comparing CALENDAR_DT to MONTH_END_DT. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| BITMAP INDEX | EIX_CALENDAR_WEEKEND | CALENDAR_DT | 1 | Yes | Yes |  |
| BITMAP INDEX | EIX_CALENDAR_WEEKEND | WEEKEND_YN | 2 | Yes | Yes |  |
| BITMAP INDEX | EIX_DATE_TODAY_TOMORROW | CALENDAR_DT | 1 | Yes | Yes |  |
| BITMAP INDEX | EIX_DATE_TODAY_TOMORROW | TOMORROW_DT | 2 | Yes | Yes |  |
| BITMAP INDEX | EIX_DATE_YEAR_MONTH | YEAR_MONTH | 1 | Yes | Yes |  |
| BITMAP INDEX | EIX_DTE | EPIC_DTE | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 25 | DAY_OF_THE_WEEK_C | ZC_DAY_OF_THE_WEEK | DAY_OF_THE_WEEK_C | No | No | No |  |
| 46 | WHICH_DAYS_C | ZC_WHICH_DAYS | WHICH_DAYS_C | No | No | No |  |
