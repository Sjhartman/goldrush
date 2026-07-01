# UAL_LOGIN_EVENTS

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=UAL_LOGIN_EVENTS

## Description

This table stores user action log data about login events. Each row represents a login event.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | APPEND |
| Load Frequency | INCREMENTAL |
| Chronicles INI | N/A |
| Release Version | Rel February 2019 |
| May contain EHI? | No |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| UAL_LOGIN_EVENT_KEY | No | Surrogate key used to uniquely identify the user action log login event. |
| USER_ID | No | The unique ID of the user associated with the login event. This column is frequently used to link to the CLARITY_EMP table. |
| CM_PHY_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| CM_LOG_OWNER_ID | VARCHAR (25) | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| WORKSTATION_ID | No | The unique identifier of the workstation record associated with the login event. |
| LOGIN_ACTION_DTTM | No | The instant of the login event using the time zone of the workstation record. |
| LOGIN_ACTION_UTC_DTTM | No | The UTC instant of the login event. |
| LOGIN_TYPE_C | No | The category ID for the type of login event. This is usually the same as the internal ID. If you use Intraconnect, this is the Community ID (CID). |
| CLIENT_APP_TARGET_C | No | The client application from which the user completed the login event. |
| DEPARTMENT_ID | No | The unique ID of the department associated with the login event. This column is frequently used to link to the CLARITY_DEP table. |
| OS_USER_NAME | No | The operating system login name used by the user when signing into Epic. This column is not populated for mobile data. |
| IS_NURSE_YN | No | Flag to indicate if login user was working as a nurse at time of login. 'Y' indicates the user was a nurse at time of login. 'N' indicates the user was not a nurse at the time of login. NULL indicates the login precedes the existence of this column. |
| IS_PHYSICIAN_YN | No | Flag to indicate if login user was working as a physician at time of login. 'Y' indicates the user was a physician at time of login. 'N' indicates the user was not a physician at the time of login. NULL indicates the login precedes the existence of this column. |
| IS_SURGEON_YN | No | Flag to indicate if login user was working as a surgeon at time of login. 'Y' indicates the user was a surgeon at time of login. 'N' indicates the user was not a surgeon at the time of login. NULL indicates the login precedes the existence of this column. |
| IS_ANESTHESIOLOGIST_YN | No | Flag to indicate if login user was working as an anesthesiologist at time of login. 'Y' indicates the user was an anesthesiologist at time of login. 'N' indicates the user was not an anesthesiologist at the time of login. NULL indicates the login precedes the existence of this column. |
| IS_RESIDENT_YN | No | Flag to indicate if login user was working as a resident at time of login. 'Y' indicates the user was a resident at time of login. 'N' indicates the user was not a resident at the time of login. NULL indicates the login precedes the existence of this column. |
| IS_APP_YN | No | Flag to indicate if login user was working as an advanced practice provider (APP) at time of login. 'Y' indicates the user was an APP at time of login. 'N' indicates the user was not an APP at the time of login. NULL indicates the login precedes the existence of this column. |
| IS_DENTIST_YN | No | Flag to indicate if login user was working as a dentist at time of login. 'Y' indicates the user was a dentist at time of login. 'N' indicates the user was not a dentist at the time of login. NULL indicates the login precedes the existence of this column. |
| IS_MEDICAL_ASSISTANT_YN | No | Flag to indicate if login user was working as a medical assistant (MA) at time of login. 'Y' indicates the user was an MA at time of login. 'N' indicates the user was not an MA at the time of login. NULL indicates the login precedes the existence of this column. |
| IS_PHYSICAL_THERAPIST_YN | No | Flag to indicate if login user was working as a physical therapist (PT) at time of login. 'Y' indicates the user was a PT at time of login. 'N' indicates the user was not a PT at the time of login. NULL indicates the login precedes the existence of this column. |
| IS_OCCUPATIONAL_THERAPIST_YN | No | Flag to indicate if login user was working as an occupational therapist (OT) at time of login. 'Y' indicates the user was an OT at time of login. 'N' indicates the user was not an OT at the time of login. NULL indicates the login precedes the existence of this column. |
| IS_SPEECH_LANG_PATHOLOGIST_YN | No | Flag to indicate if login user was working as a speech language pathologist (SLP) at time of login. 'Y' indicates the user was an SLP at time of login. 'N' indicates the user was not an SLP at the time of login. NULL indicates the login precedes the existence of this column. |
| IS_THERAPIST_YN | No | Flag to indicate if login user was working as a therapist at time of login. 'Y' indicates the user was a therapist at time of login. 'N' indicates the user was not a therapist at the time of login. NULL indicates the login precedes the existence of this column. |
| IS_RESPIRATORY_THERAPIST_YN | No | Flag to indicate if login user was working as a respiratory therapist (RT) at time of login. 'Y' indicates the user was a RT at time of login. 'N' indicates the user was not a RT at the time of login. NULL indicates the login precedes the existence of this column. |
| IS_PHLEBOTOMIST_YN | No | Flag to indicate if login user was working as a phlebotomist at time of login. 'Y' indicates the user was a phlebotomist at time of login. 'N' indicates the user was not a phlebotomist at the time of login. NULL indicates the login precedes the existence of this column. |
| IS_PAT_CARE_TECH_YN | No | Flag to indicate if login user was working as a patient care tech (PCT) at time of login. 'Y' indicates the user was a PCT at time of login. 'N' indicates the user was not a PCT at the time of login. NULL indicates the login precedes the existence of this column. |
| IS_NON_CLINICAL_USER_YN | No | Flag to indicate if login user was labeled as a non-clinical user at time of login. 'Y' indicates the user was a non-clinical user at time of login. 'N' indicates the user was not a non-clinical user at the time of login. NULL indicates the login precedes the existence of this column.  An example of a non-clinical user is an analyst. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | USER_ID | CLARITY_EMP | USER_ID | Unknown | Yes | No |  |
| 2 | USER_ID | CLARITY_EMP_2 | USER_ID | Unknown | Yes | No |  |
| 2 | USER_ID | CLARITY_EMP_3 | USER_ID | Unknown | Yes | No |  |
| 2 | USER_ID | CLARITY_EMP_4 | USER_ID | No | Yes | No |  |
| 2 | USER_ID | CLARITY_EMP_DEMO | USER_ID | No | Yes | No |  |
| 2 | USER_ID | EMP_BASIC_INFO | USER_ID | No | Yes | No |  |
| 2 | USER_ID | EMP_DOC_SETTINGS | USER_NUMBER_ID | No | Yes | No |  |
| 2 | USER_ID | F_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 2 | USER_ID | IB_MESSAGE_SETTINGS | USER_ID | No | Yes | No |  |
| 2 | USER_ID | LOGIN_INFO | USER_NUMBER_ID | No | Yes | No |  |
| 2 | USER_ID | QC_RESULTS_REVIEW | USER_NUMBER_ID | No | Yes | No |  |
| 2 | USER_ID | USER_SIDEBAR_RPT | USER_NUMBER_ID | Unknown | Yes | No |  |
| 2 | USER_ID | V_CUBE_D_USER | USER_ID | Unknown | Unknown | No |  |
| 2 | USER_ID | V_CUBE_RX_USER | USER_ID | Unknown | Unknown | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | Yes | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | Yes | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | Yes | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | Yes | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | Yes | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | Yes | No |  |
| 5 | WORKSTATION_ID | CLARITY_LWS | WORKSTATION_ID | No | Yes | No |  |
| 5 | WORKSTATION_ID | CLARITY_LWS_2 | WORKSTATION_ID | No | Yes | No |  |
| 5 | WORKSTATION_ID | CLARITY_LWS_3 | WORK_STATION_2_ID | No | Yes | No |  |
| 5 | WORKSTATION_ID | CLARITY_LWS_4 | WORKSTATION_ID | No | Yes | No |  |
| 5 | WORKSTATION_ID | WS_DEFINITION | WORKSTATION_ID | No | Yes | No |  |
| 8 | LOGIN_TYPE_C | ZC_LOGIN_TYPE | LOGIN_TYPE_C | No | Yes | No |  |
| 9 | CLIENT_APP_TARGET_C | ZC_CLIENT_APP_TARGET | CLIENT_APP_TARGET_C | No | Yes | No |  |
| 10 | DEPARTMENT_ID | BH_DEP | DEPARTMENT_ID | No | Yes | No |  |
| 10 | DEPARTMENT_ID | CLARITY_DEP | DEPARTMENT_ID | No | Yes | No |  |
| 10 | DEPARTMENT_ID | CLARITY_DEP_2 | DEPARTMENT_ID | No | Yes | No |  |

_(45 total; showing first 30)_
