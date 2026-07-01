# F_MYC_SESSIONS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=F_MYC_SESSIONS

## Description

This table contains one row per user session that occurs in MyChart. We define this as the set of all events in the MyChart audit trail (MYC_PT_USER_ACCSS) with the same combination of UA_WHO_ACCESSED and UA_SESSION_NUM. In the future, MyChart Bedside is expected to use the same column combination to allow for aggregation by session. The third column in the primary key, SESSION_TYPE, exists to account for this future change in behavior. In typical reporting cases, a report will need either MyChart or MyChart Bedside usage information but probably not both. Reports based on this derived table should have an explicit filter on the SESSION_TYPE column so that reports do not change unexpectedly when the Bedside application makes this change. Reporting content should typically query the V_MYC_SESSIONS view and not this derived table because it provides this filtering automatically and provides additional columns to make report queries simpler. This table can be joined to MYC_PT_USER_ACCSS for detailed information about what the user did during their MyChart session by using queries of the form outlined below. SELECT * FROM F_MYC_SESSIONS INNER JOIN MYC_PT_USER_ACCSS ON MYC_PT_USER_ACCSS.UA_WHO_ACCESSED = F_MYC_SESSIONS.MYPT_ID AND MYC_PT_USER_ACCSS.UA_SESSION_NUM = F_MYC_SESSIONS.UA_SESSION_NUM

## Metadata

| Property | Value |
| --- | --- |
| Type | Derived Table |
| Load Frequency | INCREMENTAL |
| Release Version | Rel 2017 |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| MYPT_ID | VARCHAR (18) | If a patient accessed their own account, then this field stores that person's WPR ID (WPR .1). It may be the patient or another person who has proxy access to the patient's account. |
| UA_SESSION_NUM | NUMERIC (18,0) | The session number for a MyChart user for the MyChart user access audit trail. Useful for grouping MyChart audit trail data by session. The session number is generated during the login event as the number of seconds since 1850 in UTC. |
| SESSION_TYPE | No | This column contains '24' if it is a MyChart session and '96' if it is a bedside session. At the time of authorship, all rows are expected to be MyChart sessions but this will likely change in the future. |
| UPDATE_DATE | No | Timestamp indicating when the row was populated. |
| START_DTTM | No | The time the session started. This can include events before login, such as interactions with the terms and conditions screen or with two factor authentication. |
| MYC_END_DTTM_NO_TIMEOUT | No | The time that the session ends, excluding the session timeout event. This column should be used for calculating the amount of time that a user actively engages with MyChart. |
| END_DTTM | No | The timestamp of the last audited event in the session. This column can be used to calculate the total amount of time that a user was logged into MyChart. This can include events corresponding to a session expiring, so this column may not always reflect the time that the user actively engaged with MyChart. |
| START_DATE | No | This is a date only version of the START_DTTM column. Filtering on a date only column can improve the performance of certain types of reporting content like the Automatic SQL metric framework |
| MYC_ACTIVE_DURATION_SECONDS | No | The time between the START_DTTM and MYC_END_DTTM_NO_TIMEOUT columns in seconds. This is the amount of time that a user actively spends using MyChart because session timeout events are excluded. Use the TOTAL_DURATION_SECONDS column to report on the total amount of time a user was logged in. |
| TOTAL_DURATION_SECONDS | No | The difference between the START_DTTM and END_DTTM columns in seconds. Because this can include a timeout event, this does not necessarily equal the amount of time the user actively used MyChart. Use the ACTIVATION_DURATION_SECONDS column to get the amount of time the user actively used MyChart. |
| UA_USER_AGENT | VARCHAR (508) | This audit item stores the HTTP user agent string. |
| USER_ID | VARCHAR (18) | If an administrator accessed a MyChart account using the universal login functionality , then this field stores that person's unique user ID (EMP .1). |
| MYC_LOGIN_BOOL | No | If this session contains a login event (MYC_UA_TYPE_C=1) then this column is equal to 1. This will typically be used in filtering along with MYC_LOGIN_ORGANIZATION_ID to exclude sessions without a login event or to separate local logins from remote initiated logins.  See MYC_LOGIN_ORGANIZATION_ID for more information about filtering. |
| MYC_REMOTE_ACCESS_BOOL | No | If this session contains a remote authorization event (WPR 530=191) then the user viewed information in an external system. This will typically be used in filtering along with MYC_LOGIN_ORGANIZATION_ID to report on sessions that are remote only. Ie, the patient did not have full access to MyChart but interacted with MyChart in a limited way on a remote portal.  See MYC_LOGIN_ORGANIZATION_ID for more information about filtering. |
| MYC_LOGIN_ORGANIZATION_ID | NUMERIC (18,0) | This column indicates that the session was initiated by an external source. If the session is created by an external source then this contains the Care Everywhere Organization (DXO) ID of that organization.   If this column is NULL, then the session was not generated externally. The user directly accessed MyChart at this organization.  If this column is not NULL and MYC_LOGIN_BOOL=1, the user logged into MyChart from a web portal hosted remotely. They had full access to MyChart but were first interacting with a portal on the organization associated with the DXO ID in this column.   If this column is not NULL and MYC_REMOTE_ACCESS_BOOL=1, then the user did not fully login to MyChart locally, but accessed information from the local MyChart on an external system. |
| MYC_REMOTE_TARGET_BOOL | No | This column equals 1 if the user viewed information from a remote system during their MyChart. If the column equals 0 then the patient only saw local data during their session.  This column can be used in filtering and to quickly answer questions of the form "In how many sessions did a MyChart user access data from an external organization?"  To get more detailed information on the exact organizations and features interacted with remotely this table must be joined to MYC_PT_USER_ACCSS as described in the table description. |
| MYC_LOCALE_AT_LOGIN | VARCHAR (18) | The locale stored in the login event. Can be used to get a general sense of which locales users typically use in MyChart and to segment the user base by their commonly used locales.   The LOCALE_SWITCH_BOOL column can be used to determine if the user switched locales during the session.  For specific details on locale switching this table can be joined to MYC_PT_USER_ACCSS as described in the table description. |
| LOCALE_SWITCH_BOOL | No | This column is equal to 1 if the user used more than 1 distinct locale in their session.   For specific details on locale switching this table can be joined to MYC_PT_USER_ACCSS as described in the table description. |
| PROXY_ACCESS_BOOL | No | This column is equal to 1 if the user who logged into MyChart accessed information about another MyChart user (proxy subject) during the session.  Join this table to D_BR_MYC_SESSION_USERS on F_MYC_SESSIONS.MYPT_ID = D_BR_MYC_SESSION_USERS.ACCESSING_MYPT_ID and F_MYC_SESSIONS.UA_SESSION_NUM = D_BR_MYC_SESSION_USERS.UA_SESSION_NUM to get results on the proxy subject(s) accessed during the session. For more detailed information, D_BR_MYC_SESSION_USERS can be joined back to MYC_PT_USER_ACCSS. |
| MYC_LOGOUT_BOOL | No | This column contains a 1 if the session contains a logout (MYC_UA_TYPE_C=20). |
| MYC_LOGOUT_XINFO | No | This column contains extra information about the logout event. This is not expected to be particularly useful in a reporting context except to expose the logic used to drive the duration columns. A string here equal to "Session Timed Out" indicates that the session timed out rather than the user explictitly logging out. So rows where this column is equal to "Session Timed Out" are where we would expect the ACTIVE_DURATION_SECONDS and TOTAL_DURATION_SECONDS columns to diverge. |
| MYC_TERMS_PRESENTED_BOOL | No | This column is equal to 1 if the user was presented with terms and conditions in MyChart.  This occurs when MYC_UA_TYPE_C=22 and UA_EXTENDED_INFO='View'. |
| MYC_TERMS_ACCEPTED_BOOL | No | This column is equal to 1 if the user accepts terms and conditions in MyChart.  This occurs when MYC_UA_TYPE_C=22 and UA_EXTENDED_INFO='Accept'. |
| MYC_TERMS_DECLINED_BOOL | No | This column is equal to 1 if the user explicitly declines terms and conditions.  This occurs when MYC_UA_TYPE_C=22 and UA_EXTENDED_INFO='Decline'. |
| MYC_TWO_FACTOR_BOOL | No | This column is equal to 1 if two factor authentication was used before login. (MYC_UA_TYPE_C=154) |
| UA_DEVICE | VARCHAR (254) | The device ID associated with the session. |
| MYC_DEVICE_RECONCILE_BOOL | No | If this session had a device reconciliation occur (332-Known Device Used or 333-Unknown Device Used), then this will be set to 1. A device reconciliation generally occurs after login, and validates a browser's device ID. Sessions for users with device tracking enabled will have this set to 1, and set to 0 when disabled. |
| LOCALE_AT_END | VARCHAR (18) | The locale stored in the last event of the session. Can be used to get a general sense of which locales users typically use in MyChart and to segment the user base by their commonly used locales.   The LOCALE_SWITCH_BOOL column can be used to determine if the user switched locales during the session.  For specific details on locale switching this table can be joined to MYC_PT_USER_ACCSS as described in the table description. |
| SESS_REMOTE_ACCESS_C | No | The type of remote access from one organization to another using Happy Together in a MyChart session. |
| UA_SESSION_IDENTIFIER | VARCHAR (50) | The identifier that uniquely identifies a user session, including across redirects between load-balanced servers. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | MYPT_ID | MYC_ACCT_DELETION | MYPT_ID | No | Unknown | No |  |
| 1 | MYPT_ID | MYC_MRG_AUD_TRL | MYPT_ID | No | Unknown | No |  |
| 1 | MYPT_ID | MYC_PATIENT | MYPT_ID | No | Unknown | No |  |
| 1 | MYPT_ID | MYC_PATIENT_2 | MYPT_ID | No | Unknown | No |  |
| 1 | MYPT_ID | V_MYC_TEST_PAT | MYPT_ID | Unknown | Unknown | No |  |
| 3 | SESSION_TYPE | APP_INFO | APPLICATION_ID | No | Unknown | No |  |
| 12 | USER_ID | CLARITY_EMP | USER_ID | Unknown | Unknown | No |  |
| 12 | USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | Unknown | No |  |
| 12 | USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | Unknown | No |  |
| 12 | USER_ID | CLARITY_EMP_4 | USER_ID | No | Unknown | No |  |
| 12 | USER_ID | CLARITY_EMP_DEMO | USER_ID | No | Unknown | No |  |
| 12 | USER_ID | EMP_BASIC_INFO | USER_ID | No | Unknown | No |  |
| 12 | USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | Unknown | No |  |
| 12 | USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 12 | USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | Unknown | No |  |
| 12 | USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | Unknown | No |  |
| 12 | USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | Unknown | No |  |
| 12 | USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | Unknown | No |  |
| 12 | USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 12 | USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 15 | MYC_LOGIN_ORGANIZATION_ID | ORG_DETAILS | ORGANIZATION_ID | No | Unknown | No |  |
| 15 | MYC_LOGIN_ORGANIZATION_ID | ORG_DETAILS_COSMOS | ORGANIZATION_ID | No | Unknown | No |  |
| 15 | MYC_LOGIN_ORGANIZATION_ID | ORG_E_RX_NETWORK | ORGANIZATION_ID | No | Unknown | No |  |
| 29 | SESS_REMOTE_ACCESS_C | ZC_SESS_REMOTE_ACCESS | SESS_REMOTE_ACCESS_C | No | Unknown | No |  |
