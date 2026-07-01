# COVERAGE_MEMBER_LIST

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=COVERAGE_MEMBER_LIST

## Description

The COVERAGE_MEMBER_LIST table contains information about the members associated with each coverage record. Since one coverage record can have multiple members, each row in the table corresponds to one member and is noted by the coverage ID and the line number.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | REQ |
| Load Frequency | INCREMENTAL |
| Chronicles INI | CVG |
| Release Version | Rel 2018 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| COVERAGE_ID | NUMERIC (18,0) | The unique identifier for the coverage record. |
| LINE | INTEGER | The line number used to identify each member of a coverage record. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record. Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record. Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| PAT_ID | VARCHAR (18) | The unique ID assigned to the patient record (EPT .1). |
| MEM_COVERED_YN | VARCHAR (1) |  |
| MEM_REL_TO_SUB_C | INTEGER |  |
| MEM_REL_TO_GUAR_C | INTEGER |  |
| DEPENDENT_TYPE_C | INTEGER |  |
| COURT_DECREE_C | INTEGER |  |
| CUSTODY_C | INTEGER |  |
| MEM_PAYOR_NAME | VARCHAR (254) | Stores the patient name as known to the Payor. This item is used to keep the name that is stored in the Patient master file separate from the name that the Payor is expecting. |
| MEM_VERIFICATION_ID | NUMERIC (18,0) | The verification record for the coverage member. |
| MEM_NUMBER | VARCHAR (192) | The identification number assigned to the member for the coverage. |
| MEM_PERSON_CODE | VARCHAR (254) | This contains the person code for a member ID on a coverage. For a member ID of 12345-01, the person code would be "01". |
| ELIGIBILITY_CLAR_C | INTEGER |  |
| MEM_APP_DATE | DATETIME | The date on which the member applied for coverage. |
| MEM_APP_TIME | DATETIME (Local) | The time on which the member applied for coverage. |
| MEM_EFF_FROM_DATE | DATETIME | The date on which the coverage goes into effect for the member. |
| MEM_STUDENT_YN | VARCHAR (1) | If the member is a full time student this column contains the value ?Y?. If the member is not a full time student, as determined by the member?s Employment Status, this column contains the value ?N?. |
| MEM_MEDICARE_NUM | VARCHAR (254) | Stores the patient's Medicare number from the patient record, if applicable. This stored value may be a HICN or a MBI.  This data is used primarily for Registration and will match PATIENT_4.LEGACY_HICN. However, it may be different from MEM_MEDICARE_NUM_COVERAGE, which is maintained through Enrollment and Eligibility infrastructure (preferred for managed care scenarios). |
| MEM_ENROLL_RSN_C | INTEGER |  |
| HIX_EN_ADDL_MAINT_RSN_C | INTEGER |  |
| MEM_EFF_TO_DATE | DATETIME | The date after which the coverage is no longer in effect for the member and the member becomes ineligible for benefits. |
| MEM_TERM_REASON_C | INTEGER |  |
| MEM_SCHED_DISCON_DT | DATETIME | The member scheduled discontinuation date. |
| MEM_EDI_UPDATE_DT | DATETIME | The date the coverage record was last updated through an eligibility load. |
| MEM_LATE_ENROLL_YN | VARCHAR (1) |  |
| MEM_VERIF_STAT_C | VARCHAR (66) |  |
| LAST_VERIF_DATE | DATETIME | The date the member on the coverage was last verified. |
| APCLM_MEM_VER_DATE | DATETIME | Stores the date when the member on the coverage was last verified. This data is only intended to be used when VRX verification is used in an AP Claims instance, otherwise it will be NULL and COVERAGE_MEMBER_LIST.LAST_VERIF_DATE should be used. |
| PCN_OVERRIDE | VARCHAR (10) | The processor control number (PCN) for this member. This PCN overrides the PCN at the plan or payor level for this member only. |
| MEMBER_VERF_USER_ID | VARCHAR (18) | The ID of the user who last verified this member's status. |
| MEMBER_ID_FROM_FILE | VARCHAR (192) | The member ID received on the source file for the member on the coverage. |
| CARRIER_IDENTIFIER | VARCHAR (10) | Used for prescription adjudication in ambulatory pharmacy. Carrier code assigned in Workers' Compensation Program (327-CR). |
| CLAIM_IDENTIFIER | VARCHAR (30) | Used for prescription adjudication in ambulatory pharmacy. Identifies the claim number assigned by Workers' Compensation Program (435-DZ). |
| FACILITY_IDENTIFIER | VARCHAR (10) | Used for prescription adjudication in ambulatory pharmacy. ID assigned to the patient's clinic/host party (336-8C). |
| HOME_PLAN | VARCHAR (3) | Used for prescription adjudication in ambulatory pharmacy. Code identifying the Blue Cross or Blue Shield plan ID which indicates where the member's coverage has been designated. Usually where the member lives or purchased their coverage (314-CE). |
| PLAN_IDENTIFIER | VARCHAR (8) | Used for prescription adjudication in ambulatory pharmacy. Assigned by the processor to identify a set of parameters, benefits, or coverage criteria used to adjudicate a claim (524-FO). |
| RX_BILLING_INFO_ID | INTEGER | Contains the default prescription billing information on this coverage like default values to send during claim adjudication. |
| MEM_CVG_ATTR *(deprecated)* | VARCHAR (254) |  |
| HIX_APP_ID | VARCHAR (50) | The application ID of exchange coverages. |
| HIX_ORIGIN | VARCHAR (254) | The origin type of exchange coverages. |
| MEM_MAIL_CITY | VARCHAR (254) | The member's mailing city. |
| MEM_MAIL_STATE_C | VARCHAR (66) |  |
| MEM_MAIL_ZIP | VARCHAR (40) | The member's mailing ZIP code. |
| MEM_MAIL_COUNTY_C | VARCHAR (66) |  |
| MEM_MAIL_COUNTRY_C | VARCHAR (66) |  |
| MEM_MAIL_ADDR_LN_1 | VARCHAR (254) | This item contains line one of the member's mailing address (the entirety of which is stored in CVG-18930). The purpose of this item is to provide the ability for reporting administrators to retrieve line one of the address without having to join the member address table. |
| MEM_MAIL_ADDR_LN_2 | VARCHAR (254) | This item contains line two of the member's mailing address (the entirety of which is stored in CVG-18930). The purpose of this item is to provide the ability for reporting administrators to retrieve line two of the address without having to join the member address table. |
| MEM_CUSTO_NAME | VARCHAR (254) | The name of the member's custodial parent. |
| MEM_CUSTO_SSN | VARCHAR (80) | The SSN of the member's custodial parent. |
| MEM_CUSTO_CITY | VARCHAR (254) | The city of the member's custodial parent. |
| MEM_CUSTO_STATE_C | VARCHAR (66) |  |
| MEM_CUSTO_ZIP | VARCHAR (40) | The ZIP code of the member's custodial parent. |
| MEM_CUSTO_COUNTY_C | VARCHAR (66) |  |
| MEM_CUSTO_COUNTRY_C | VARCHAR (66) |  |
| MEM_CUSTO_EMAIL | VARCHAR (254) | The e-mail address of the member's custodial parent. |
| MEM_CUSTO_ADDR_LN_1 | VARCHAR (254) | This item contains line one of the member's custodial parent address (the entirety of which is stored in CVG-18962). The purpose of this item is to provide the ability for reporting administrators to retrieve line one of the address without having to join the member custodial parent address table. |
| MEM_CUSTO_ADDR_LN_2 | VARCHAR (254) | This item contains line two of the member's custodial parent address (the entirety of which is stored in CVG-18962). The purpose of this item is to provide the ability for reporting administrators to retrieve line two of the address without having to join the member custodial parent address table. |
| MEM_COVERED_C | INTEGER |  |
| MEM_APPL_DTTM | 318 | The date and time on which the member applied for coverage. |
| MEM_PAYOR_SEX_C | VARCHAR (66) |  |
| MEM_MEDICARE_NUM_COVERAGE | VARCHAR (50) | Stores the member's Medicare number from the coverage, if applicable. This stored value may be a HICN or a MBI.  This data is maintained through the standard Enrollment and Eligibility infrastructure (i.e. should be accurate for managed care scenarios). The number stored on the patient's record (MEM_MEDICARE_NUM or PATIENT.MEDICARE_NUM) may be different since it is used primarily for Registration. |
| MEM_LEGACY_HICN_COVERAGE | VARCHAR (50) | If there is a HICN available for the member (e.g. known prior to receiving their MBI), this column stores the HICN from the coverage.  This data is maintained through the standard Enrollment and Eligibility infrastructure (i.e. should be accurate for managed care scenarios). The number stored on the patient's record (PATIENT_4.LEGACY_HICN) may be different since it is used primarily for Registration. |
| MEM_MAIL_HOUSE_NUM | VARCHAR (20) | The house number of the member's mailing address. |
| MEM_MAIL_DISTRICT_C | INTEGER |  |
| MEM_CUSTO_HOUSE_NUM | VARCHAR (20) | The house number of the member's custodial parent's address. |
| MEM_CUSTO_DISTRICT_C | INTEGER |  |
| MEM_MAIL_ADDR_IS_VALID_C | INTEGER |  |
| MEM_MAIL_ADDR_VALID_MTHD_C | INTEGER |  |
| MEM_MAIL_ADDR_VALID_UTC_DTTM | DATETIME (UTC) | The UTC date and time when the member's mailing address was last validated. |
| MEM_MAIL_ADDR_VALID_USER_ID | VARCHAR (18) | The unique ID of the end user that last validated the member's mailing address. |
| MEM_CUSTO_ADDR_IS_VALID_C | INTEGER |  |
| MEM_CUSTO_ADDR_VALID_MTHD_C | INTEGER |  |
| MEM_CUSTO_ADDR_VALID_UTC_DTTM | DATETIME (UTC) | The UTC date and time when the custodial parent address was last validated. |
| MEM_CUSTO_ADDR_VALID_USER_ID | VARCHAR (18) | The unique ID of the end user that last validated the custodial parent address. |
| MEM_MAIL_ADDR_VALID_DTTM | DATETIME (Local) | The local date and time when the member's mailing address was last validated. |
| MEM_CUSTO_ADDR_VALID_DTTM | DATETIME (Local) | The local date and time when the custodial parent address was last validated. |
| MEM_ADDR_IS_UNDELIV_YN | VARCHAR (1) |  |
| MEM_MEDICAID_NUM | VARCHAR (40) | The Medicaid Number for a member on a given coverage. |
| MEM_EFF_DT_CHNG_RSN_C | INTEGER |  |
| MEMBER_PAYER_BIRTH_DATE | DATETIME | This item stores the member's date of birth as it is recorded in the payer's system. |
| MEM_ALT_IDENT | VARCHAR (93) | The alternate card identification number assigned to the member for the coverage. |

## Indexes

| Type | Name | Column Name | Ordinal Position | Enabled | Key Column |  |
| --- | --- | --- | --- | --- | --- | --- |
| B-TREE INDEX | EIX_CVG_MEMBER_LIST_PAID | PAT_ID | 1 | Yes | Yes |  |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | COVERAGE_ID | COVERAGE | COVERAGE_ID | Unknown | No | No |  |
| 1 | COVERAGE_ID | COVERAGE_2 | CVG_ID | Unknown | No | No |  |
| 1 | COVERAGE_ID | COVERAGE_3 | CVG_ID | Unknown | No | No |  |
| 1 | COVERAGE_ID | COVERAGE_4 | CVG_ID | Unknown | No | No |  |
| 1 | COVERAGE_ID | COVERAGE_5 | CVG_ID | No | No | No |  |
| 1 | COVERAGE_ID | COVERAGE_6 | COVERAGE_ID | No | No | No |  |
| 1 | COVERAGE_ID | COVERAGE_MISC_COMMENTS | COVERAGE_ID | No | No | No |  |
| 1 | COVERAGE_ID | CVG_AP_CLAIMS | COVERAGE_ID | Unknown | No | No |  |
| 1 | COVERAGE_ID | V_EHI_COVERAGE_SUBS | COVERAGE_ID | Unknown | Unknown | No |  |
| 3 | CM_PHY_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 3 | CM_PHY_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 4 | CM_LOG_OWNER_ID | CL_COMMUNTY_INSTNC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_BASIC | INSTANCE_ID | Unknown | No | No |  |
| 4 | CM_LOG_OWNER_ID | ECI_COS_HOST | INSTANCE_ID | No | No | No |  |
| 5 | PAT_ID | ANTICOAG_SELF_REGULATING | PAT_ID | No | No | No |  |
| 5 | PAT_ID | CARE_COORDINATION | PAT_ID | Unknown | No | No |  |
| 5 | PAT_ID | CLAIMS_DERIVE_PAT_FLAGS | PAT_ID | No | No | No |  |
| 5 | PAT_ID | COMMUNITY_RESRC_REVIEWED | PAT_ID | No | No | No |  |
| 5 | PAT_ID | D_PAT_GEOGRAPHIC_CLASS | PAT_ID | Unknown | Unknown | No |  |
| 5 | PAT_ID | EPT_MEM_INFO | PAT_ID | No | No | No |  |
| 5 | PAT_ID | EXT_DATA_LAST_DONE | PAT_ID | No | No | No |  |
| 5 | PAT_ID | F_IBD_ADULT_FORM_PAT | PAT_ID | Unknown | Unknown | No |  |
| 5 | PAT_ID | HH_PAT_INFO | PAT_ID | Unknown | No | No |  |
| 5 | PAT_ID | HM_STATUS_UPD | PAT_ID | No | No | No |  |
| 5 | PAT_ID | IMMNZTN_LAST_REVIEW | PAT_ID | No | No | No |  |
| 5 | PAT_ID | PATIENT | PAT_ID | No | No | No |  |
| 5 | PAT_ID | PATIENT_2 | PAT_ID | No | No | No |  |
| 5 | PAT_ID | PATIENT_3 | PAT_ID | No | No | No |  |
| 5 | PAT_ID | PATIENT_4 | PAT_ID | No | No | No |  |

_(142 total; showing first 30)_
