# Clarity Schema Index

Use this file to identify relevant tables, then load full schemas from `clean_schemas/<TABLE>.md`.

| Table | Description | Key Columns | Notes |
| --- | --- | --- | --- |
| ACCESS_LOG | The ACCESS_LOG table contains the basic access information of each activity, such as the time the event occurred and process ID.   | ACCESS_INSTANT, PROCESS_ID, ACCESS_TIME, METRIC_ID, USER_ID, WORKSTATION_ID, PAT_ID, CSN |  |
| ACCESS_LOG_2019 |  |  |  |
| ACCESS_LOG_2020 |  |  |  |
| ACCESS_LOG_2021 |  |  |  |
| ACCESS_LOG_2022 |  |  |  |
| ACCESS_LOG_2023 |  |  |  |
| ACCESS_LOG_2024 |  |  |  |
| ACCESS_LOG_2025 |  |  |  |
| ACCESS_LOG_2026 |  |  |  |
| ACCESS_LOG_ARCHIVED |  |  |  |
| ACCESS_LOG_METRIC | The ACCESS_LOG_METRIC table contains the detailed information of the metrics defined in the E1M master file. | METRIC_ID, METRIC_NAME, CNT_METRIC_EVNT_C, NORM_FACTOR, METRIC_DESC, METRIC_TYPE_C, METRIC_GROUP_C, METRIC_ACTION_C |  |
| ACCESS_LOG_MNEM | The ACCESS_LOG_MNEM table contains the detailed information of each mnemonic that should be recorded. | DATA_MNEMONIC_ID, DATA_DESC, DATA_INDEXED_C, DATA_INI_ITEM, VALUES_PER_EVNT_C, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| ACCESS_LOG_VW |  |  |  |
| ACCESS_WRKF_2023 |  |  |  |
| ACCESS_WRKF_2024 |  |  |  |
| ACC_LOG_DTL_IX | The ACC_LOG_DTL_IX table contains the supplementary information of the activities which were recorded in the ACCESS_LOG table, suc | ACCESS_INSTANT, PROCESS_ID, DATA_MNEMONIC_ID, STRING_VALUE, INTEGER_VALUE |  |
| ACC_LOG_DTL_IX_2022 |  |  |  |
| ACC_LOG_DTL_IX_2023 |  |  |  |
| ACC_LOG_DTL_IX_2024 |  |  |  |
| ACC_LOG_DTL_IX_2025 |  |  |  |
| ACC_LOG_DTL_IX_2026 |  |  |  |
| ACC_LOG_DTL_NI | The ACC_LOG_DTL_NI table contains the supplementary information of the activities which were recorded in the ACCESS_LOG table, suc | ACCESS_INSTANT, PROCESS_ID, DATA_MNEMONIC_ID, STRING_VALUE, INTEGER_VALUE |  |
| ACC_LOG_DTL_NI_2024 |  |  |  |
| ACC_LOG_DTL_NI_2025 |  |  |  |
| ACC_LOG_DTL_NI_2026 |  |  |  |
| ACC_LOG_MTLDTL_IX | The ACC_LOG_MTLDTL_IX table contains the supplementary information of the activities which were recorded in the ACCESS_LOG table,  | ACCESS_INSTANT, PROCESS_ID, DATA_MNEMONIC_ID, IDENTIFIER, STRING_VALUE, INTEGER_VALUE |  |
| ACC_LOG_MTLDTL_IX_2022 |  |  |  |
| ACC_WRKF_DTL_IX_2023 |  |  |  |
| ACC_WRKF_DTL_IX_2024 |  |  |  |
| ACUITY_CONFIG | This table contains the configuration information for the acuity systems. | ACUITY_SYSTEM_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ACUITY_SYSTEM_NAME, RECORD_STATUS_C, DISPLAY_NAME, DISPLAY_COLUMN_ID, DISCOL_ID_STOCK_TI |  |
| ACUITY_RULE_SCORE | Extracted table for rule-related data from scoring system data filed to RDI. | REGISTRY_DATA_ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, RULE_ID, RULE_SCORE, RULE_TYPE_C, SCORE_CALC_UTC_DTTM |  |
| ALERT | The ALERT table contains one record for every alert that was created in Hyperspace. Each record is based on the alert ID and conta | ALT_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ALERT_DESC, MED_ALERT_TYPE_C, PAT_ID, PAT_CSN, MED_VENDOR_C |  |
| ALERT_ACTION | This table contains details on the actions seen or taken by the alert. | ALERT_ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, ACTION_TYPE_C, ACTION_IDENT, ACTION_NAME, ACTION_PARENT_ROW |  |
| ALLERGY | The ALLERGY table contains information about the allergies noted in your patients' clinical system records. You would use this tab | ALLERGY_ID, PAT_ID, ALLERGEN_ID, DESCRIPTION, REACTION, DATE_NOTED, STATUS, ENTERED_DATE |  |
| ALLERGY_FLAG | This table holds data of whether the patient's allergies were marked as containing no drug allergies. | PAT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ALRGY_FLAG_YN, ALRGY_FLG_UPD_BY_ID, ALRGY_FLAG_UPD_DTTM |  |
| ALLERGY_REACTIONS | The ALLERGY_REACTIONS table contains the category values of the reactions associated with a given allergy. There may be multiple r | ALLERGY_ID, LINE, REACTION_C, UPDATE_DATE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| ALL_CATEGORIES | This table contains information from all category items. Use this table to get the name, title, or abbreviation of any category li | INI, ITEM, VALUE_C, NAME, TITLE, ABBR, INTERNAL_ID, IS_ACTIVE_YN |  |
| ALT_HISTORY | This table contains general history information for each type of medication warning or advisory. Since each warning could be trigg | ALT_ID, ALT_DATE_REAL, ALT_CSN_ID, CONTACT_DATE, CM_CT_OWNER_ID, USER_INTSET_CSN, SYS_INTSET_CSN, ALT_STATUS_C | **Primary table** in this group (101 cols). Overflow siblings joined on shared key: ALT_HISTORY_2 (98 cols), ALT_HISTORY |
| ALT_HISTORY_2 | This table contains general history information for each type of medication warning or advisory. Since each warning could be trigg | ALT_ID, ALT_CSN_ID, FILTEROUT_REASON_C, DUP_ALERT_ING_C, DUP_ALERT_GROUP_C, VENDOR_EXTERNAL_ID, BPA_ACK_LPP_ID, PAT_COND_CHK_SEV_C | **Overflow table** for ALT_HISTORY (101 cols). Contains additional columns for the same records — join on the shared pri |
| AN_HSB_LINK_INFO | This table stores Anesthesia episode-level information. | SUMMARY_BLOCK_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ANES_EPT_LINK_ID, ANES_EPT_CSN_LINK, AN_UNLINKED_FLAG_YN, ANES_PROC_ID, ANES_PROC_DATE |  |
| APPOINTMENT_PREDICT | This table contains information about the predicted no show likelihood for appointments. | PAT_ENC_CSN_ID, LINE, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, PROBABILITY_PERCENT, EVALUATION_UTC_DTTM |  |
| AP_CASE_TYPES | Use this table to report on anatomic pathology settings configured at the case type level. Refer to table LAB_AP_LAB_SETUP if you' | LAB_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ID_PIECE_FORMAT_C, DELIM_PREC_SLD, DELIM_PREC_SPEC, AP_WORKLIST_TYPE_C, CASE_TYPE_NAME |  |
| AP_SPECIMEN_DESC | Lab Anatomic Pathology case specimen descriptions. | SPECIMEN_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, AP_SPEC_DESCR_ID, AP_SPEC_DESCR_CMT |  |
| AUDIT_SESSION | The AUDIT_SESSION table contains the basic information of each audit session common to all audit sessions.  Additional information | AUDIT_SESSION_ID, AUDIT_PLATFORM_C, SESSION_START_UTC_DTTM, SESSION_UPDATE_UTC_DTTM |  |
| BILL_AREA | This table contains the extracted information of the Bill Area master file (BIL). | BILL_AREA_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RECORD_NAME, RECORD_STATUS_C, ABBR, GL_PREFIX, RPT_GRP_ONE |  |
| BLOCK | This table contains information about scheduling blocks. | BLOCK_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, BLOCK_NAME, BLOCK_TYPE_C, PROVIDER_ID, SURGEON_GROUP_ID, SURGICAL_SERVICE_C |  |
| BLOOD_ADMIN_INFO | This table holds the information for a blood unit associated with an order. The data includes the discrete information for the blo | ORDER_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, BLOOD_ADMIN_UNIT, BLOOD_ADMIN_REG, BLOOD_ADMIN_PROD, BLOOD_ADMIN_EXP_DTTM |  |
| BND_EPSD_INFO | This table contains information about bundled episodes. A bundled episode is used to link related encounters and services that can | EPISODE_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, BND_EPSD_BILL_STS_C, COVERAGE_ID, PAYOR_ID, SELF_PAY_YN, BPC_ID |  |
| CACHED_USER_TYPE | This table displays the cached user type data from a user's EMP record. | USER_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CACHED_USER_TYPE_C, DEPARTMENT_ID, TEMPLATE_ID, CACHE_DATE |  |
| CAREPLAN_INFO | Contains information about care plan template records. | CARE_INTG_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CAREPLAN_TYPE_C, PAT_ENC_CSN_ID, PATIENT_ID, LINKED_PAT_CAREPLAN_YN, RFL_INSTR_NOTE_ID |  |
| CAREPLAN_TEMPLATE | Contains information about Healthy Planet Care Plan templates. | CAREPLAN_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CAREPLAN_TEMPLATE_ID |  |
| CAREPLAN_TEMP_INFO | This table contains the basic no-add single items of Care plan template (LCE) records like record name, status, type, display name | TEMPLATE_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, TEMPLATE_NAME, RECORD_STATUS_C, DISPLAY_NAME, TEMPLATE_TYPE_C, ALLOW_SELECT_YN |  |
| CARE_INTG_ELEM | This table contains the problems associated with a Care Integrator record. | CARE_INTG_ID, LINE, PROBLEM_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| CARE_TEAM_EDIT_HX | This table holds information about how the patient care team was edited. A patient care team is a group of providers affiliated wi | PAT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CHANGE_DATETIME, CHANGE_USER_ID, CHANGE_TYPE_C, PROV_ID |  |
| CASE_AP_RELATED_ORDERS | The CASE_AP_RELATED_ORDERS table contains information about other orders related to the Anatomic Pathology case. This information  | REQUISITION_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ORDER_ID |  |
| CASE_AP_WORKLIST_NOTES | The CASE_AP_WORKLIST_NOTES table contains information about the worklist notes for the anatomic pathology case. | REQUISITION_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, NOTES |  |
| CHAT_ACCESS_LOG | Table containing log of when Secure Chat was accessed. | CONVERSATION_ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, READER_USER_ID, ACCESSED_INST_UTC_DTTM, ACCESSED_MSG_LN, READER_MYPT_ID |  |
| CHAT_CONVERSATIONS | Table containing Secure Chat conversation level items. | CONVERSATION_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RECORD_NAME, RECORD_STATUS_C, LST_UPDATE_UTC_DTTM, PURGE_MESSAGE_UTC_DTTM, PAT_ID |  |
| CHAT_MESSAGE | Table containing Secure Chat message info. | CONVERSATION_ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, INST_SENT_UTC_DTTM, MESSAGE_TYPE_C, MESSAGE_PRIORITY_C, SENDER_USER_ID |  |
| CHAT_MESSAGE_CONTENT | Table for PHI message contents sent in secure chat. | CONVERSATION_ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, MSG_TEXT, MEDIA_DOCUMENT_ID, LINK_CONTENT_TYPE_C, LINK_REPORT_INFO_ID |  |
| CHAT_PARTICIPANT | Table containing Secure Chat conversation participants. | CONVERSATION_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, USER_ID, USER_MYPT_ID, USER_ACTIVE_C, LST_READ_UTC_DTTM |  |
| CHILD_NOTE_INFO | The CHILD_NOTE_INFO table contains information about child notes that are linked to clinical notes. Each row represents one child  | NOTE_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, TEXT_NOTE_CSN_ID, LINK_TYPE_C, LINK_USER_ID, LINK_UTC |  |
| CLARITY_ADT | The CLARITY_ADT table is the master table for ADT event history information. This table contains several foreign keys for other AD | EVENT_ID, EVENT_TYPE_C, EVENT_SUBTYPE_C, DEPARTMENT_ID, ROOM_ID, ROOM_CSN_ID, BED_ID, BED_CSN_ID |  |
| CLARITY_BED | This table reflects the data in the Hospital Beds (BED) master file. | BED_CSN_ID, BED_ID, BED_CONT_DATE_REAL, BED_LABEL, RECORD_STATE, CONTACT_DATE, ROOM_ID, TELEPHONE_NUMBER |  |
| CLARITY_CER | The CLARITY_CER table contains information from the rule master file. | RULE_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RULE_NAME |  |
| CLARITY_COMPONENT | The CLARITY_COMPONENT table contains basic information about the standard result components that can constitute your procedures. F | COMPONENT_ID, NAME, ABBREVIATION, EXTERNAL_NAME, BASE_NAME, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, COMPONENT_TYPE_C |  |
| CLARITY_CONCEPT | The CLARITY_CONCEPT table contains information pertaining to SmartData elements and concepts. SmartData elements are discrete data | CONCEPT_ID, NAME, ABBREVIATION, DATA_TYPE_C, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, PARENT_CONCEPT, SNOMED_PART_IDENT_C |  |
| CLARITY_DEP | The CLARITY_DEP table contains high-level information about departments. | DEPARTMENT_ID, DEPARTMENT_NAME, DEPT_ABBREVIATION, SPECIALTY, REV_LOC_ID, DEP_GROUP, GL_PREFIX, RPT_GRP_ONE | **Primary table** in this group (110 cols). Overflow siblings joined on shared key: CLARITY_DEP_2 (100 cols), CLARITY_DE |
| CLARITY_DEP_2 | This table extends CLARITY_DEP, which contains high-level information about departments from the Department master file. | DEPARTMENT_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ADDRESS_CITY, ADDRESS_STATE_C, ADDRESS_ZIP_CODE, ADDRESS_COUNTY_C, ADDRESS_COUNTRY_C | **Overflow table** for CLARITY_DEP (110 cols). Contains additional columns for the same records — join on the shared pri |
| CLARITY_DRG | This table contains information for the DRG (Diagnosis Related Groups) master file. | DRG_ID, DRG_NAME, RECORD_STATE, DRG_NUMBER, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, NON_MPI_WEIGHT, NON_MPI_TRIM_PTS |  |
| CLARITY_EAP | The CLARITY_EAP table contains basic information about the procedure records in your system. This does include both A/R and clinic | PROC_ID, PROC_NAME, PROC_CODE, PROC_CAT, PROC_TYPE, DEBIT_CREDIT, IS_BAD_DEBT_ACCT, ACCOUNT_INS | **Primary table** in this group (149 cols). Overflow siblings joined on shared key: CLARITY_EAP_2 (101 cols), CLARITY_EA |
| CLARITY_EAP_2 | The CLARITY_EAP_2 table contains basic information about the procedure records in your system. This includes both A/R and clinical | PROC_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, SCREENING_PROC_YN, ABN_SPANISH_NAME, QTY_PER_BILL_CODE, QTY_PER_BC_UNITS_C, BILL_QTY_RND_FCTR | **Overflow table** for CLARITY_EAP (149 cols). Contains additional columns for the same records — join on the shared pri |
| CLARITY_EAP_3 | The CLARITY_EAP_3 table contains basic information about the procedure records in your system. This includes both A/R and clinical | PROC_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CONTRAST_REQ_C, PAT_FRIENDLY_DESC, TOMOSYNTHESIS_PROC_YN, PROC_SUBTYPE_C, CLINICALLY_ACTIVE_YN | **Overflow table** for CLARITY_EAP (149 cols). Contains additional columns for the same records — join on the shared pri |
| CLARITY_EAP_4 | The CLARITY_EAP_4 table contains basic information about the procedure records in your system. This includes both A/R and clinical | PROC_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, DENTAL_SURF_LOGIC_C, DENTAL_TOOTH_SET_C, DENTAL_ARCH_C, DEFAULT_EXPECTED_DATE_CMT_C, DEFAULT_FASTING_DURATION | **Overflow table** for CLARITY_EAP (149 cols). Contains additional columns for the same records — join on the shared pri |
| CLARITY_EAP_OT | The CLARITY_EAP_OT table contains over time information from the procedure master file. | PROC_ID, CONTACT_DATE_REAL, CONTACT_DATE, CONTACT_TYPE_C, CONTACT_COMMENT, RVU_WORK_COMPON, RVU_OVERHD_COMPON, RVU_MALPRAC_COMPON |  |
| CLARITY_ECL | This table contains information about security classes in the system. | ECL_ID, CLASSIFCTN_NAME, ECL_RECORD_STAT_C, CAD_INI_MENU, SEC_STRING, ENTRY_ACC_YN, VIEW_ACC_YN, OVRBK_ACC_YN | **Primary table** in this group (110 cols). Overflow siblings joined on shared key: CLARITY_ECL_2 (72 cols). Prefer this |
| CLARITY_EDG | The CLARITY_EDG table contains basic information about diagnoses. | DX_ID, DX_NAME, DX_STATUS, DX_GROUP, ICD9_CODE, PARENT_DX_ID, EC_INACTIVE_YN, SPEC_BILLING_YN |  |
| CLARITY_EEP | This table contains information about employer records from the EEP master file. | EMPLOYER_ID, EMPLOYER_NAME, ADDRESS1, ADDRESS2, CITY, STATE_C, ZIP, PHONE |  |
| CLARITY_EMP | This table contains high-level information about user records from the User master file. | USER_ID, NAME, PROV_ID, EPIC_EMP_ID, MC_DEPARTMENT_ID, CR_USER_NAME, PB_DEF_CLS_NM, CONF_SEC_CLS_NM | **Primary table** in this group (174 cols). Overflow siblings joined on shared key: CLARITY_EMP_2 (100 cols), CLARITY_EM |
| CLARITY_EMP_2 | This table extends CLARITY_EMP, which contains high-level information about user records from the User master file. | USER_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, BTLR_CONFIG_C, BTLR_SORTING_C, OVR_DSB_FROM_ROL_YN, EW_PAT_SEL_PREF_C, WEB_PT_HEADER_DEF | **Overflow table** for CLARITY_EMP (174 cols). Contains additional columns for the same records — join on the shared pri |
| CLARITY_EPM | The CLARITY_EPM table contains information about payer records. | PAYOR_ID, PAYOR_NAME, FINANCIAL_CLASS, PRODUCT_TYPE, GL_PREFIX, RPT_GRP_ONE, RPT_GRP_TWO, RPT_GRP_THREE | **Primary table** in this group (101 cols). Overflow siblings joined on shared key: CLARITY_EPM_2 (54 cols), CLARITY_EPM |
| CLARITY_EPP | The CLARITY_EPP table contains basic information about your benefit plans. | BENEFIT_PLAN_ID, BENEFIT_PLAN_NAME, PRODUCT_TYPE, RPT_GRP_ONE, RPT_GRP_TWO, RPT_GRP_THREE, RPT_GRP_FOUR, RPT_GRP_FIVE | **Primary table** in this group (114 cols). Overflow siblings joined on shared key: CLARITY_EPP_2 (86 cols), CLARITY_EPP |
| CLARITY_EPP_2 | The CLARITY_EPP_2 table contains additional information about your benefit plan records. | BENEFIT_PLAN_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, USE_ACCEL_SP_YN, DFLT_DRG_TYPE_ID, BDRG_TYP_REF_DT_C, MIXTURE_DISP_FEE, RPT_GRP_ELEVEN_C | **Overflow table** for CLARITY_EPP (114 cols). Contains additional columns for the same records — join on the shared pri |
| CLARITY_FC | Financial Class is actually a category list (HCT 50000) in your system; however, it is used so frequently in Accounts Receivable r | FINANCIAL_CLASS, FINANCIAL_CLASS_NAME, FIN_CLASS_TITLE, FINANCIAL_CLASS_ABBR, INTERNAL_ID |  |
| CLARITY_HIP | In Basket Registries store information to determine the recipients who can display and handle specific types of messages. This tab | REGISTRY_ID, REGISTRY_NAME, REGSTRY_STATUS_C, LOGICAL_OWNER, PHYSICAL_OWNER, REGISTRY_DESC, RECIP_MASTERFILE, SELECTION_INI |  |
| CLARITY_IMMUNZATN | The CLARITY_IMMUNZATN table contains high-level information about the immunizations providers can choose on the Immunization Admin | IMMUNZATN_ID, NAME, ABBREVIATION, RECORD_STATUS, IMMUN_TYPE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, NAME_MIXED_CASE |  |
| CLARITY_LLB | Interface laboratory general information. | RESULTING_LAB_ID, LLB_NAME, LLB_ABBR, LLB_STATUS_C, LLB_ADDR_LN1, LLB_ADDR_LN2, LLB_CITY, LLB_STATE_C |  |
| CLARITY_LOC | This table contains information about your location records. These include revenue locations and patients' primary clinics/locatio | LOC_ID, LOC_NAME, LOCATION_GROUP, DEFAULT_DEPT_ID, POS_TYPE, LOCATION_ABBR, LOC_IS_OUTSIDE, GL_PREFIX | **Primary table** in this group (100 cols). Overflow siblings joined on shared key: CLARITY_LOC_2 (74 cols). Prefer this |
| CLARITY_LPP | The CLARITY_LPP table contains information from the extension master file. | LPP_ID, LPP_NAME, LPP_TYPE_C, M_CODE, COMMENTS, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RECORD_STATE_C |  |
| CLARITY_LWS | The CLARITY_LWS table contains basic information about workstations used in your system. | WORKSTATION_ID, WORKSTATION_NAME, ROOM_IDENTIFIER, PRIM_DEPARTMENT_ID, SCREEN_NAME, WORKSTN_IDENTIFIER, WORKSTATION_TYPE_C, CM_LOG_OWNER_ID | **Primary table** in this group (101 cols). Overflow siblings joined on shared key: CLARITY_LWS_2 (100 cols), CLARITY_LW |
| CLARITY_MEDICATION | The CLARITY_MEDICATION table contains high-level information from all the medications for use in your facility. | MEDICATION_ID, NAME, THERA_CLASS_C, PHARM_CLASS_C, PHARM_SUBCLASS_C, SIMPLE_GENERIC_C, COST, GENERIC_NAME |  |
| CLARITY_MOD | This table contains masterfile information on billing modifiers. | MODIFIER_ID, MODIFIER_NAME, EXTERNAL_ID, PRICE_CHANGE_PCT, RVU_CHANGE_PCT, IS_NONPRICE_MOD_YN, IS_REPEATABLE_YN, AP_PRICE_CHG_PCT |  |
| CLARITY_NOTES |  |  |  |
| CLARITY_NOTES_SAMPLE |  |  |  |
| CLARITY_ORGANISM | The CLARITY_ORGANISM table contains basic information about the organisms used in clinical systems. | ORGANISM_ID, NAME, ABBREVIATION, REC_STATE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RECORD_TYPE_C, RECORD_STATUS_C |  |
| CLARITY_POS | The CLARITY_POS table contains information about your places of service. All EAF records are included in this table regardless of  | POS_ID, POS_NAME, POS_GROUP, POS_TYPE, POS_LOC_IS_OUTSIDE, POS_NAME_ABBR, GL_PREFIX, RPT_GRP_ONE | **Primary table** in this group (101 cols). Overflow siblings joined on shared key: CLARITY_POS_2 (10 cols). Prefer this |
| CLARITY_PRC | The CLARITY_PRC table contains one record for each visit type, panel, agent, and visit type modifier in your system. | PRC_ID, PRC_NAME, PRC_ABBR, RECORD_TYPE, PROC_CAT, OVRD_BILL_NO_TYPE, CHART_PULL, XRAY_PULL | **Primary table** in this group (101 cols). Overflow siblings joined on shared key: CLARITY_PRC_2 (34 cols). Prefer this |
| CLARITY_ROM | This table reflects the information in the Hospital Rooms (ROM) master file. | ROOM_CSN_ID, ROOM_ID, ROM_CONT_DATE_REAL, RECORD_STATE, ROOM_NAME, CONTACT_DATE, ROOM_NUMBER, ROOM_READY_YN |  |
| CLARITY_RSH | This view contains research study and client record information. | RESEARCH_ID, RESEARCH_NAME, RESEARCH_STATUS_C, SERV_AREA_ID, LOC_ID, STUDY_CODE, PROV_ID, APPROVED_AMOUNT |  |
| CLARITY_SA | The CLARITY_SA table contains information about your service areas. The records included in this table are facility profile record | SERV_AREA_ID, SERV_AREA_NAME, SERV_AREA_ABBR, SERV_AREA_TYPE, SERV_AREA_GROUP, GL_PREFIX, RPT_GRP_ONE, RPT_GRP_TWO |  |
| CLARITY_SER | The CLARITY_SER table contains high-level information about your provider records. These records may be caregivers, resources, cla | PROV_ID, PROV_NAME, PROV_TYPE, PROV_ABBR, GL_PREFIX, RPT_GRP_ONE, RPT_GRP_TWO, RPT_GRP_THREE | **Primary table** in this group (127 cols). Overflow siblings joined on shared key: CLARITY_SER_2 (100 cols), CLARITY_SE |
| CLARITY_SER_2 | This table contains high-level information about your provider records. | PROV_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, IP_ORD_PROV_YN, DEF_LETTER_PREF_C, DEF_CHART_STATN_ID, HOME_CITY, HOME_STATE_C | **Overflow table** for CLARITY_SER (127 cols). Contains additional columns for the same records — join on the shared pri |
| CLARITY_SER_ADDR | The CLARITY_SER_ADDR table includes the office addresses for providers. | PROV_ID, LINE, ADDR_UNIQUE_ID, ADDR_LINE_1, ADDR_LINE_2, ADDR_LINE_3, CITY, STATE_C |  |
| CLARITY_SER_DEPT | The CLARITY_SER_DEPT table contains the departments in which each of your providers will be scheduled. A provider can be scheduled | PROV_ID, LINE, DEPARTMENT_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, INACT_CAD_DEPT_YN, OUTLOOK_DEPT_YN, SUBGROUP_C |  |
| CLARITY_SER_LICEN2 | The CLARITY_SER_LICEN2 table includes basic license information for providers. | PROV_ID, LINE, LICENSE_TYPE, LICENSE_NUM, LICENSE_EXP_DATE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, LICENSE_STATE_C |  |
| CLARITY_SER_SPEC | The CLARITY_SER_SPEC table contains the specialties associated with each of your providers. A provider can have multiple specialti | PROV_ID, LINE, SPECIALTY_C, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| CLARITY_TBL | This table contains a list of table (E0B) records that exist in the Clarity Compass along with pertinent information including the | TABLE_ID, TABLE_NAME, EXTRACT_FILENAME, RELEASED_VERSION_C, LAST_MOD_VERSION_C, BS_TEMPLATE_ID, DEPENDENT_INI, IS_JOB_DIVIDED_YN | **Overflow table** for CLARITY_TBL_2 (93 cols). Contains additional columns for the same records — join on the shared pr |
| CLARITY_TBL_APP | Contains a list of applications that use a given table record along with whether the table is marked as core. | TABLE_ID, LINE, APPLICATION_C, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CORE_TABLE_YN |  |
| CL_CHRG_EDIT_RULE | This table contains rule information. | RULE_ID, RULE_NAME, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, DISPLAY_NAME, RPT_DISPLAY_PP_ID, RULE_DESCRIP_STRING, PERF_MEASURE_C |  |
| CL_ELG | This table contains information on allergens. | ALLERGEN_ID, ALLERGEN_NAME, RECORD_STATE_NAME, EDIT_NAME, ALLERGEN_TYPE_C, INTRACTN_FWD_ID, MED_INTRCT_LINK, CM_PHY_OWNER_ID |  |
| CL_EMP_ID | The CL_EMP_ID table contains the system ID numbers for your users. Each record may have multiple IDs; therefore, a line number is  | USER_NUMBER_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, MPI_ID_TYPE_ID, MPI_ID, MPI_FROM_DATE, MPI_TO_DATE |  |
| CL_ICD_PX | The CL_ICD_PX table is the master table for ICD procedures. | ICD_PX_ID, ICD_PX_NAME, HCD_REC_STATE_C, PROCEDURE_NAME, PROC_MASTER_NM, SHORT_PROC_NAME, BILL_DESC, CM_PHY_OWNER_ID |  |
| CL_PRL_SS | This table contains the SmartSet/Protocol/Pathway settings that do not change per contact for each SmartSet, Protocol, Pathway, or | PROTOCOL_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, PROTOCOL_NAME, RECORD_STATUS_2_C, SS_TYPE_C, PRL_STATUS_C, PROTOCOL_TYPE_C_ID |  |
| CL_PRL_SS_OT | This table contains the contact specific settings for each SmartSet or Protocol. | PROTOCOL_ID, CONTACT_DATE_REAL, CONTACT_DT, CM_CT_OWNER_ID, CONTACT_NUM, DISPLAY_NAME, VERSION_STATUS_C, FILTER_LOCATOR_ID |  |
| CL_QANSWER | This table contains general information about questionnaire answer records. For example, the questionnaire the answer record is fo | ANSWER_ID, FORM_ID, QUESTIONNAIRE_DAT, IS_CLOSED, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, QF_VERIFY_HVR_ID, IMG_ANSWER_SET_NAME |  |
| CL_QANSWER_QA | This table contains the questions and answers for questionnaire answer records. It also includes audit information such as when th | ANSWER_ID, LINE, QUEST_ID, QUEST_DAT, QUEST_ANSWER, QUEST_COMMENT, QUEST_LINE_NUM, QUEST_EDIT_USER_ID |  |
| CL_QFORM | The CL_QFORM table is the primary table for non-contact specific information related to questionnaire forms. | FORM_ID, FORM_NAME, RECORD_STATE, FORM_TYPE_C, USE_OF_FORM, REPORT_NAME, SORT_ORDER, VB_FORM_NAME |  |
| CL_QQUEST | The CL_QQUEST table is the primary table for storing non-contact specific information related to questions in a questionnaire. | QUEST_ID, QUEST_NAME, RECORD_STATE, QUEST_TYPE_C, HCF_QUEST_LPP_ID, HCF_FILING_LPP_ID, REG_RESP_INI, REG_RESP_ITEM |  |
| CL_RSN_FOR_VISIT | This table contains basic information for records in the Reason for Visit (HRV) master file. | REASON_VISIT_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, REASON_VISIT_NAME, RECORD_STAT_HRV_C, ABBREVIATION, DISPLAY_TEXT |  |
| CL_SPHR | The CL_SPHR stores basic information about the SmartPhrase master file (HH1). | SMARTPHRASE_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, SMARTPHRASE_NAME, RECORD_STATUS_C, MNEMONIC, FACILITY_LEVEL_YN, INST_OF_NA_EDIT_TM |  |
| CONCEPT_MAPPED | The CONCEPT_MAPPED table stores the Concept Identifier of the SNOMED concept or SmartData Identifier (SDI) of the SmartData elemen | MAPPING_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, MAPPING_TYPE_C, CONCEPT_ID, MAPPING_DEFINITION, PREF_LEX_MAP_YN |  |
| COVERAGE | The COVERAGE table contains high-level information on both managed care and indemnity coverage records in your system. | COVERAGE_ID, COVERAGE_TYPE_C, COVERAGE_STATUS_C, CARRIER_ID, PAYOR_ID, PLAN_ID, PLAN_GRP_ID, SUBSCR_NUM | **Primary table** in this group (116 cols). Overflow siblings joined on shared key: COVERAGE_2 (91 cols), COVERAGE_3 (62 |
| COVERAGE_2 | The COVERAGE_2 table contains high-level information on both managed care and indemnity coverage records in your system. | CVG_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, STATUS_C, RETRO_QUEUE_FLAG, COPAY_INFO, IS_DEDUCT_MET_C, IS_ASGN_CVG_C | **Overflow table** for COVERAGE (116 cols). Contains additional columns for the same records — join on the shared primar |
| COVERAGE_3 | The COVERAGE_3 table contains high-level information on both managed care and indemnity coverage records in your system. | CVG_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, PAYOR_STATE_C, PAYOR_ZIP, PAYOR_PHONE, PAYOR_CLAIM_OFC_NUM, REF_PROV_NAME_ID | **Overflow table** for COVERAGE (116 cols). Contains additional columns for the same records — join on the shared primar |
| COVERAGE_CREATION | *** Deprecated *** The table has been replaced by the ENTRY_DATE column on Clarity table COVERAGE_4. | CVG_ID, CONTACT_DATE_REAL, CONTACT_DATE |  |
| COVERAGE_MEMBER_LIST | The COVERAGE_MEMBER_LIST table contains information about the members associated with each coverage record. Since one coverage rec | COVERAGE_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, PAT_ID, MEM_COVERED_YN, MEM_REL_TO_SUB_C, MEM_REL_TO_GUAR_C |  |
| COVERAGE_MEM_LIST | This view contains information about the members associated with each coverage record. Because one coverage record can have multip | COVERAGE_ID, LINE, PAT_ID, MEM_EFF_FROM_DATE, MEM_EFF_TO_DATE, MEM_COVERED_YN, MEM_EDI_UPDATE_DT, MEM_REL_TO_SUB_C |  |
| CP_TEMP_PROB_TEMP | This table stores Template Element (OT) (I LCE 105), the problem templates associated with the care plan. | TEMPLATE_ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CM_CT_OWNER_ID, TEMPLATE_ELMENT_ID |  |
| CSA_PARTITION_LOOKUP |  |  |  |
| CUST_SERVICE | The CUST_SERVICE table stores information entered into system's Customer Service module. This can be used to report on communicati | COMM_ID, ENTRY_USER_ID, ENTRY_DATE, SOURCE_TYPE_C, SOURCE_MEMBER_ID, TOPIC_C, SUBJECT_TYPE_C, RES_C |  |
| CUST_SERVICE_TRANSFER | The CUST_SERVICE_TRANSFER table contains information about patient transfer requests that have been documented in a customer servi | COMM_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, TRANS_PAT_SSN, TRANS_REF_PROV, TRANS_PAT_NAME, TRANS_PAT_AGE, TRANS_PAT_SEX_C |  |
| CUST_SERV_ATCHMENT | Extracts the attachments for this NCS (customer service) record. | COMM_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ATCHMENT_USER_ID, ATCHMENT_INSTANT, ATCHMENT_TYPE_C, ATCHMENT_PAT_ID |  |
| CVG_ACCT_LIST | This table contains the list of guarantor accounts associated with a coverage. | CVG_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ACCT_SHARING_CVG_ID |  |
| DATE_DIMENSION | This table is similar to a typical Data Warehouse "Date Dimension". Link your dates to this table to avoid processing date functio | CALENDAR_DT, DAY_OF_WEEK, WEEK_NUMBER, WEEK_ENDING_DT, LAST_FRIDAY_DT, MONTH_END_DT, DAY_OF_MONTH, MONTH_NAME |  |
| DELIVERY_ANES_MTHD | This table contains anesthesia methods that were selected in Stork's Delivery Summary activity and populated in the delivery recor | SUMMARY_BLOCK_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, DEL_ANESTH_METHOD_C |  |
| DELIVERY_CORDCOMPS | This table contains newborn-specific cord complications, selected in Stork's Delivery Summary activity, populated in the delivery  | SUMMARY_BLOCK_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, DEL_CORD_COMP_C |  |
| DELIVERY_CORD_VESS | This table contains the number of cord vessels for the newborn. This table contains choices selected in Stork's Delivery Summary a | SUMMARY_BLOCK_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, DEL_CORD_VESSELS_C |  |
| DELIVERY_PRES | This table contains the presentation types of the newborn. These are choices selected in Stork's Delivery Summary activity, and ar | SUMMARY_BLOCK_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, DEL_PRESENTATION_C |  |
| DELIVERY_RESUSCIT | This table contains newborn-specific resuscitation measures, selected in Stork's Delivery Summary activity and populated in the de | SUMMARY_BLOCK_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, DEL_RESUSCITATION_C |  |
| DESKTOP_ACTIVITY | The DESKTOP_ACTIVITY table contains information about activity records used by Hyperspace. | ACTIVITY_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ACTIVITY_NAME, DISPLAY_NAME, ACTIVITY_DESCRIPTOR, RELEASED_ACTIVITY_DESCRIPTOR, REL_DESCRIPTOR_CALC_LOCAL_DTTM |  |
| DEVICE_INFO | This table displays high-level information for device (DEV) records. | DEVICE_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, DEVICE_NAME, RECORD_STATE_C, DEVICE_DESC, DEVICE_TYPE_ID, DEVICE_GROUP_YN |  |
| DM_DIABETES | DM_DIABETES is a data mart table that stores information related to the topic of diabetes. This table consolidates patient informa | RECORD_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, REGISTRY_STATUS_C, PAT_ID, CUR_PCP_PROV_ID, CUR_PRIM_LOC_ID, CONTACT_LAST_DT |  |
| DM_ICU_STAY | DM_ICU_STAY is a data mart table that stores information related to ICU stays. This table consolidates patient information from ma | RECORD_ID, REGISTRY_STATUS_C, PAT_ID, ICU_STAY_BLOCK_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ICU_LENGTH_OF_STAY_DAYS, NEXT_DEPARTMENT_ID |  |
| DM_IP_READMISSION | This registry stores both current and historical information related to the topic of readmissions. This registry consolidates hosp | RECORD_ID, DM_DATE, REGISTRY_STATUS_C, PAT_ID, PAT_ENC_CSN_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, IS_ENCOUNTER_A_READMISSION_YN |  |
| DM_WLL_ALL | DM_WLL_ALL is a data mart table that stores information related to general patient health. This table consolidates patient informa | RECORD_ID, REGISTRY_STATUS_C, PAT_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, NUM_ED_VIS, NUM_HOSP_ADMSNS, AGE |  |
| DM_WLL_ALL_EXT | DM_WLL_ALL_EXT is a data mart table that stores external information related to the general wellness registry metrics for all pati | RECORD_ID, REGISTRY_STATUS_C, PAT_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ABDOM_AORTIC_ANEURYSM_SCRN_DT, HEP_C_VIRUS_SCRN_DT, VISUAL_IMPAIRMENT_SCRN_DT |  |
| DOCS_RCVD | High level information about received documents. | DOCUMENT_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, TYPE_C, PAT_ID, DOC_SOURCE_ORG_ID, DOC_SET, ENC_EVENT_IDENT |  |
| DOCS_RCVD_DETAILS | Details about received documents, including request audit information. | DOCUMENT_ID, CONTACT_DATE_REAL, CONTACT_DATE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CM_CT_OWNER_ID, CONTACT_SERIAL_NUM, CONTACT_NUM | **Primary table** in this group (108 cols). Overflow siblings joined on shared key: DOCS_RCVD_DETAILS_2 (99 cols), DOCS_ |
| DOCS_RCVD_NOTE_SECTIONS | Stores note section data received. | DOCUMENT_ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, NOTE_SECTION_IDENTIFIER, NOTE_SECTION_TYPE, NOTE_SECTION_NOTE_ID, CONTACT_SERIAL_NUM |  |
| DOCS_RCVD_PED_VITALS | Contains pediatric vitals (aka birth history) received through external documents and stored in DXR. | DOCUMENT_ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, PED_VITAL_REF_ID, PED_VITAL_SOURCE_VALUE, PED_VITAL_SOURCE_UNIT, PED_VITAL_BIRTH_LENGTH_CM |  |
| DOCS_RCVD_PREG_DATING | This table contains Pregnancy Dating information received from other organizations. | DOCUMENT_ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, EVENT_IDENTIFIER, OB_DT_EDD_DATE, OB_DT_WORKING_EDD_YN, OB_DT_EVENT_C |  |
| DOCS_RCVD_RSLTS | This table stores discrete results received from outside sources. | DOCUMENT_ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, RESULT_INST_DTTM, RESULT_PROC_NAME, RESULT_PROC_ID, PROC_LOINC |  |
| DOCS_RCVD_RSLT_VAR_INFO | Contains the genomic variant information received with results. | DOCUMENT_ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, RESULT_VAR_KEY, RESULT_VAR_CHKSUM, RESULT_VAR_FHIR_SR_RESRC_IDENT, RESULT_VAR_UNP_YN |  |
| DOCUMENT_OCR | This table contains textual information for a media file that has been accumulated through optical character recognition. | DOCUMENT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, OCR_WORD, OCR_WORD_PAGE, OCR_WORD_X_POS, OCR_WORD_Y_POS |  |
| DOC_INFORMATION | The DOC_INFORMATION table contains information about documents, including scanned and electronically signed documents. | DOC_INFO_ID, REC_STATE, DOC_INFO_TYPE_C, DOC_GRP_C, DOC_STAT_C, IS_VISIT_SPEC_YN, DOC_DESCR, DOC_RECV_TIME | **Primary table** in this group (101 cols). Overflow siblings joined on shared key: DOC_INFORMATION_2 (101 cols), DOC_IN |
| DOC_INFORMATION_2 | The DOC_INFORMATION table contains information about documents, including scanned and electronically signed documents. | DOCUMENT_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, COMM_ORIG_HNO_ID, DOC_REP_CONTEXT_C, DOC_RDI_ID, DOCUMENT_FAX_NUM, COMM_ORIG_RDI_ID | **Overflow table** for DOC_INFORMATION (101 cols). Contains additional columns for the same records — join on the shared |
| D_PROV_PRIMARY_HIERARCHY | This table gives provider-level information for use in reports. It includes, among other details, the provider's primary departmen | PROV_ID, PROV_NAME, PROV_NM_WID, PROV_NM_CRED, PROV_NM_CRED_WID, DEPARTMENT_ID, DEPARTMENT_NAME, DEPARTMENT_NM_WID |  |
| EDG_CURRENT_ICD10 | Diagnosis terms can map to multiple codes in a code set. This table discretely lists the mapped codes for term-type diagnoses. Cod | DX_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CODE |  |
| EDG_CURRENT_ICD9 | Diagnosis terms can map to multiple codes in a code set. This table discretely lists the mapped codes for term-type diagnoses. Cod | DX_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CODE |  |
| EDP_PROC_CAT_INFO | This table contains information about procedure categories. Procedure categories are used to group together related procedures, su | PROC_CAT_ID, SCHED_FOR_OUTPAT_YN, USE_VT_SPEC_REST_C, PROMPT_FOR_VT_YN, MAMMO_RELATED_YN, PROC_CAT_NAME, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID | **Primary table** in this group (101 cols). Overflow siblings joined on shared key: EDP_PROC_CAT_INF_2 (51 cols). Prefer |
| ED_EVENT_TMPL_INFO | This table contains the noadd single items (name, ID, record state?) for a given event template. | RECORD_ID, RECORD_NAME, RECORD_STATE_NAME, DISPLAY_NAME, EVENT_NAME, TEMP_NAME_EDIT, ITEMS_EDITED_TIME, UPDATE_TIME |  |
| ED_IEV_EVENT_INFO | This table contains information about the current event records. | EVENT_ID, LINE, EVENT_TYPE, EVENT_STATUS_NAME, EVENT_DISPLAY_NAME, EVENT_TIME, EVENT_RECORD_TIME, EVENT_USER_ID |  |
| ED_IEV_PAT_INFO | This table contains information that is useful for linking records (patient, department, etc.) to their appropriate events. | EVENT_ID, RECORD_STATE_NAME, PAT_ID, EPT_DAT, ITEMS_EDITED_TIME, UPDATE_DATE, PAT_DATE_REAL, DTE_EXTERNAL |  |
| EMP_CAT_GROUPERS_ONE | This table contains information about the first category report grouper in user records. | USER_NUMBER_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CAT_RPT_GRP_ONE_C |  |
| EMP_NOTES | This table extracts the free text notes recorded about the user. | USER_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, NOTES |  |
| EMR_SYSTEM_DEFS | This table contains information from no-add, single-response items in EMR System Definitions. | FACILITY_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, PREGNANCY_RATG_C, LACTATION_RATG_C, OB_CSECT_GRPER_ID, MR_PSIST_STRTD_YN, CHK_SER_PHR_C |  |
| ENROLL_INFO | The ENROLL_INFO table contains information about patient enrollments in research studies, including status, alias, start and end d | ENROLL_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RECORD_STATUS_C, RESEARCH_STUDY_ID, PAT_ID, ENROLL_STATUS_C, STUDY_ALIAS |  |
| ENROLL_STAT_ACTV | This table contains list of all enrollment statuses considered to be "active". | FACILITY_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RSH_ENR_STAT_ACT_C |  |
| ENROLL_STAT_PRE | Table contains list of enrollment statuses considered to be "pre-enrolled". | FACILITY_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RSH_ENR_STAT_PRE_C |  |
| EPISODE | This table contains high-level information on the episodes recorded in the clinical system for your patients. When a provider sees | EPISODE_ID, NAME, STATUS, SUM_BLK_TYPE_ID, PAT_ID, START_DATE, END_DATE, COMMENTS | **Primary table** in this group (101 cols). Overflow siblings joined on shared key: EPISODE_2 (57 cols), OCCURRENCE_CODE |
| EPISODE_DEF | This table contains information about Episode Definition records. | EPISODE_DEF_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, EPISODE_TYPE_C, BASE_PWY_PER_TYPE_C, PWY_PER_TYPE_NAME, RTT_STATUS_MAP_ID, EPISODE_DEF_NAME |  |
| EPISODE_LINK | The EPISODE_LINK table contains high-level information on the episodes recorded in the clinical system for your patients. It is in | EPISODE_ID, LINE, STATUS, SUM_BLK_TYPE_ID, PAT_ID, PAT_ENC_DATE_REAL, PAT_ENC_CSN_ID, CM_PHY_OWNER_ID |  |
| EPI_PROBLEM_LIST | Contains the problems linked to this episode. | SUMMARY_BLOCK_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, PROBLEM_LIST_ID |  |
| EPT_CARE_TEAMS | This table displays provider IDs associated with patient encounters. | PAT_ENC_CSN_ID, LINE, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, CARE_TEAMS_ID |  |
| EPT_TEAM_AUDIT | This table represents the audit trail for team-based actions taken for a patient. | PAT_ENC_CSN_ID, LINE, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, TEAM_AUDIT_ID, TEAM_ACTION_C |  |
| ETHNIC_BACKGROUND | Table to store information about the patient's ethnic background. | PAT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ETHNIC_BKGRND_C |  |
| EXTERNAL_CNCPT_MAP | The EXTERNAL_CNCPT_MAP table stores information about mappings as well as the entities (record/category/item) they reference. The  | MAPPING_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RECORD_STATUS_C, CUSTOM_MAPPING_YN, ENTITY_INI, ENTITY_ITEM, ENTITY_VALUE_NUM |  |
| EXTERNAL_DEATH_REPORTS | External reports of patient death information. | PAT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, EXT_DEATH_STAT_C, EXT_DEATH_DATE, EXT_DEATH_SOURCE_C, EXT_DEATH_COMMENT |  |
| EXT_ORD_SIGNED_SUMMARY | This table contains summary information for medication orders from external encounters. | ORDER_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, EXT_ORD_SIGNED_SUMMARY |  |
| FACILITY_PROFILE | This table contains basic information about your facility record. It only contains information from the newest contact. | LAB_ID, CONTACT_DATE_REAL, LAB_DATE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CM_CT_OWNER_ID, SPEC_REC_BEHAVIOR_C, SPEC_RECV_BEH_EX_C |  |
| FAMILY_HX | The FAMILY_HX table contains data recorded in the family history contacts entered in the patient's chart during a clinical system  | PAT_ID, PAT_ENC_DATE_REAL, LINE, CONTACT_DATE, END_HIST_DATE_REAL, MEDICAL_HX_C, MEDICAL_OTHER, RELATION |  |
| FDC_ID | The FDC_ID table contains the system ID numbers for your flowsheet datacaptor information. Each flowsheet datacaptor may have mult | RECORD_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, MPI_ID_TYPE_ID, MPI_ID, MPI_FROM_DATE, MPI_TO_DATE |  |
| FEE_BILLING_SETTINGS | This table is used to specify processing fees for outpatient pharmacy work requests. | PHARMACY_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, FEE_TYPE_C, FEE_ITEM_ID, DELIVERY_METHOD_C |  |
| FEE_SCHEDULE | This table contains the fee schedules used by pricing contracts. | CONTRACT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, FEE_SCHEDULE_ID |  |
| FEE_SCHEDULE_MAP | The FEE_SCHEDULE_MAP table contains basic information about the fee schedule map that is used to select a fee schedule and convers | FEE_SCHEDULE_MAP_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, FEE_SCHEDULE_MAP_NAME, RECORD_STATUS_C, EXTERNAL_IDENTIFIER, RECORD_CREATION_DT, INSTANT_OF_UPDATE_DTTM |  |
| FINALIZE_PHYSICIAN | This table contains information about the physician who finalized a study and when it was finalized. | ORDER_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, FINALIZE_PROV_ID, FINALIZING_INS_DTTM, FINALIZING_INST_UTC_DTTM, FINALIZING_INST_LOCAL_DTTM |  |
| FIN_DIV | This table contains the extracted information of the Financial Division. | FIN_DIV_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, FIN_DIV_NM, ABBR, RPT_GRP_1, RPT_GRP_2, RPT_GRP_3 |  |
| FIN_SUBDIV | This table contains the extracted information of the Financial Subdivision. | FIN_SUBDIV_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, FIN_SUBDIV_NM, ABBR, FIN_DIV_ID, RPT_GRP1, RPT_GRP2 |  |
| FLOWSHEET | This table contains review flowsheet or synopsis records from your system. It includes the flowsheet (or synopsis) ID, the flowshe | FLOWSHEET_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, FLOWSHEET_NAME, SHORT_TITLE, FLOWSHEET_TYPE_C |  |
| FLOWSHEET_DC_INFO | This table displays no add item information for device variable records (FDC).  This includes basic items such as record, name, ID | RECORD_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, VARIABLE_NAME, RECORD_STATE_C, VARIABLE_ID, SPECIAL_TYPE_C, UNIT_C |  |
| FLOWSHEET_INFO | This table contains details about the review flowsheet or synopsis records in your system, namely what kind of information a flows | FLOWSHEET_ID, CONTACT_DATE_REAL, LINE, VERSION_DATE, SOURCE_ID, WHAT, HEADER_OVERRIDE, MAXIMUM_WIDTH |  |
| FLOWSHEET_ROWS | This table displays flowsheet row information for device variable records (FDC). | RECORD_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, FLOWSHEET_ROW_ID, FLO_LIST_YN, DISABLE_AUTOFILE_YN |  |
| F_AN_RECORD_SUMMARY | This derived fact table collects core information about anesthesia records into a standardized summary format. Each row uniquely r | AN_EPISODE_ID, UPDATE_DATE, AN_PAT_ID, AN_53_ENC_CSN_ID, AN_52_ENC_CSN_ID, AN_INPATIENT_DATA_ID, AN_LOG_ID, AN_PREOP_NOTE_ID |  |
| F_DIAGNOSIS_INFO | This table will be deprecated in the Epic February 2026 release. This derived table finds all diagnoses for all patients. It looks | DX_ID, PAT_ID, UPDATE_DATE, NUM_ENC_DX, LAST_DATE_ENC_DX, FIRST_DATE_ENC_DX, NUM_PROBLEM_LIST, LAST_DATE_PROB_LIST |  |
| F_ED_ENCOUNTERS | The F_ED_ENCOUNTERS table stores commonly used information for ED encounters. Each emergency department encounter has a single row | PAT_ENC_CSN_ID, UPDATE_DATE, ED_EPISODE_ID, PAT_ID, AGE_AT_ARRIVAL_YEARS, AGE_AT_ARRIVAL_MONTHS, ENC_ADDRESS_LINE, ADT_ARRIVAL_DATE |  |
| F_IP_HSP_WORKLOAD_ACUITY | This table stores information pertaining to Workload Acuity scoring systems. Each row is a filed score identified by the associate | PAT_ENC_CSN_ID, ACUITY_SYSTEM_ID, SCORE_LOC_DTTM, SCORE_UTC_DTTM, SCORE_DATE_LOC, SCORE_TIME_LOC, DEPT_ID, TRTMT_TM_NURSE_CUR_ID |  |
| F_IP_ORD_FLO_VOLUME | This table stores information about volume flowsheet documentation pertaining to orders. Each row is a pairing of flowsheet docume | VOLUME_FSD_ID, VOLUME_FSD_LINE, VOLUME_ORDER_ID, UPDATE_DATE, VOLUME_MEAS_VALUE, VOLUME_REC_DTTM, INPATIENT_DATA_ID, PAT_ENC_CSN_ID |  |
| F_MYC_SESSIONS | This table contains one row per user session that occurs in MyChart. We define this as the set of all events in the MyChart audit  | MYPT_ID, UA_SESSION_NUM, SESSION_TYPE, UPDATE_DATE, START_DTTM, MYC_END_DTTM_NO_TIMEOUT, END_DTTM, START_DATE |  |
| F_OPIOID_ORDERS | This derived table stores information on opioid outpatient medication orders and is intended to boost the performance of the opioi | ORDER_ID, UPDATE_DATE, HAS_NALOXONE_YN, PROV_REV_PDMP_IN_ENC_YN, PDMP_REV_IN_ENC_YN, DAYS_SINCE_PROV_REV_PDMP, DAYS_SINCE_LAST_PDMP_REV |  |
| F_PAT_CODES | This table will be deprecated in the Epic November 2025 release. This table is not the current recommendation for reporting on pat | EVENT_ID, LINE, PAT_ENC_CSN_ID, CODE_STATUS_C, CODE_START_DTTM, CODE_END_DTTM, CODE_TYPE, FST_CARDIAC_RHYTHM |  |
| F_PAT_MYCHART_STATUS_HX | This table can be used to determine the MyChart status of a patient at a time. This transforms the PAT_MYC_STAT_HX table such that | PAT_ID, START_DTTM, UPDATE_DATE, END_DTTM, START_DT, END_DT, MYCHART_STATUS_C, START_LINE |  |
| F_RX_ORDER | The F_RX_ORDER table contains information about medication orders prepared or supplied by inpatient pharmacies that is typically u | ORDER_MED_ID, REPORT_DATE, UPDATE_DATE, PAT_DEPT_ID, ORDERING_DATE_REAL, FIRST_VERIFY_DATE_REAL, FIRST_VERIFY_DATE_REAL_LINE, LAST_VERIFY_DATE_REAL |  |
| F_SCHED_APPT | This table contains information about appointments, with one row per appointment. It is derived from the PAT_ENC table and contain | PAT_ENC_CSN_ID, UPDATE_DATE, CONTACT_DATE, PAT_ID, APPT_STATUS_C, DEPARTMENT_ID, PROV_ID, PRC_ID |  |
| F_SCHED_APPT_STATS | Basic appointment statistics broken down by provider, department, and date. Note: if your organization uses joint appointments and | STATISTICS_DATE, PROV_ID, DEPARTMENT_ID, UPDATE_DATE, MASTER_SCHEDULABLE_HRS, SCHEDULABLE_HRS, BOOKED_HRS, AVAIL_OPENINGS_ON_DAY_CNT |  |
| F_VENT_EPISODES | This table contains a listing of all the mechanical ventilation episodes documented in Flowsheets. A ventilation episode begins wh | VENT_START_FSD_ID, VENT_START_FSD_LINE, UPDATE_DATE, INPATIENT_DATA_ID, VENT_START_DTTM, START_FLO_MEAS_ID, VENT_END_FSD_ID, VENT_END_FSD_LINE |  |
| GENE_IDENT | Version-independent information about a gene record such as its name or HUGO Gene Nomenclature (HGNC) ID. | GENE_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RECORD_SYMBOL, RECORD_STATUS_2_C, CURR_CONTACT_DATE_REAL, GENE_HGNC_IDENT |  |
| GEO_REGION | The GEO_REGION table contains information about geographical regions. This includes codes to identify these regions. | GEO_REGION_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, GEO_REGION_NAME, RECORD_STATE_C, GEO_REGION_TYPE_C, INACTIVE_DATE, APP_EXCHANGE_OWNER |  |
| GOAL | This table contains data on discrete goals (IGO) records associated with a patient. | GOAL_ID, USER_ID, GOAL_TYPE_ID, PROBLEM_ID, CREATED_TIME, DELETED_YN, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| GOAL_TEMPLATES | This table contains goal template information. It includes columns for the goal template name, goal template record state, display | GOAL_TEMPLATE_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, GOAL_TEMPLATE_NAME, RECORD_STATE_C, GOAL_TEMPLATE_TYP_C, CP_DUP_GOAL_ACT_C, GOAL_USAGE_C |  |
| GOAL_TYPE | This table contains information on goal types (INO records). | GOAL_TYPE_ID, GOAL_NAME, TYPE_NAME, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RECORD_STATUS_C, DISPLAY_NAME |  |
| GROUPER_COMPILED_REC_LIST | Contains the compiled list of records for a grouper. | COMPILED_GROUPER_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, GROUPER_RECORDS_VARCHAR_ID, GROUPER_RECORDS_NUMERIC_ID, BASE_GROUPER_ID, COMPILED_CONTEXT |  |
| GROUPER_ITEMS | The GROUPER_ITEMS table contains high-level information about your grouper records: description, context, grouper type and concept | GROUPER_ID, GROUPER_NAME, DESCRIPTION, CONTEXT_INI, CONCEPT_LOGIC, CM_LOG_ONWER_ID, CM_PHY_OWNER_ID, GROUPER_TYPE_C | **Primary table** in this group (25 cols). Overflow siblings joined on shared key: GROUPER_ITEMS_2 (8 cols). Prefer this |
| HNO_INFO | This table contains common information from General Use Notes items. This table focuses on time-insensitive, once-per-record data  | NOTE_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, DELETED_CAT_C, NOTE_TYPE_NOADD_C, NOTE_FORMAT_NOADD_C, DICT_IDENTIFIER, PAT_ID | **Primary table** in this group (102 cols). Overflow siblings joined on shared key: HNO_INFO_2 (53 cols). Prefer this ta |
| HNO_INFO_2 | This table contains common information from General Use Notes items. This table focuses on one time only data while other HNO tabl | NOTE_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, BOOK_CONFRM_DATETIM_DTTM, RELEVANT_REC_EVENT_ID, WAS_PRECHARTED_YN, GROUP_NOTE_ID, QN_MESSAGE_TYPE_C | **Overflow table** for HNO_INFO (102 cols). Contains additional columns for the same records — join on the shared primar |
| HNO_INFO_2_20260225 |  |  |  |
| HNO_NOTE_TEXT | The HNO_NOTE_TEXT table contains the note text on I HNO 41 or I HNO 40. The text in HNO 40 or 41 is first converted to plain text. | NOTE_ID, CONTACT_DATE_REAL, LINE, NOTE_CSN_ID, CONTACT_DATE, CM_CT_OWNER_ID, CHRON_ITEM_NUM, NOTE_TEXT |  |
| HSB_TPL_LIST | The linking of an episode ID to a patient ID and a treatment plan ID. | EPISODE_ID, LINE, TPL_ID, CM_LOG_OWNER_ID, CM_PHY_OWNER_ID |  |
| HSP_ACCT_ADMIT_DX | This table contains hospital account admit diagnoses from the Hospital Accounts Receivable (HAR) master file. | HSP_ACCOUNT_ID, LINE, ADMIT_DX_ID, ADMIT_DX_TEXT, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| HSP_ACCT_CPT_CODES | This table contains hospital account CPT(R) codes from the Hospital Accounts Receivable (HAR) master file. | HSP_ACCOUNT_ID, LINE, CPT_CODE, CPT_CODE_DATE, CPT_PERF_PROV_ID, CPT_EVENT_NUMBER, CPT_MODIFIERS, LMRP_CODE |  |
| HSP_ACCT_CVG_LIST | This table contains hospital account and PB visit coverage list information from the Hospital Accounts Receivable (HAR) master fil | HSP_ACCOUNT_ID, LINE, COVERAGE_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CVG_IGNR_PRIM_PAY_YN, CVG_IGNR_RSN_C, CVG_TIMELY_FILING_DATE |  |
| HSP_ACCT_DX_LIST | This table contains hospital account final diagnosis list information from the Hospital Accounts Receivable (HAR) master file. | HSP_ACCOUNT_ID, LINE, DX_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, DX_POA_YNU, DX_AFFECTS_DRG_YN, DX_COMORBIDITY_YN |  |
| HSP_ACCT_EXTINJ_CD | This table contains hospital account external injury codes information from the Hospital Accounts Receivable (HAR) master file. | HSP_ACCOUNT_ID, LINE, EXT_INJURY_DX_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, EXT_INJURY_POA_YNU, EXT_COMORBIDITY_YN, EXT_DX_AFF_DRG_YN |  |
| HSP_ACCT_MULT_DRGS | This table contains multiple diagnosis related group information for hospital accounts. | HSP_ACCOUNT_ID, LINE, DRG_ID_TYPE_ID, DRG_ID, DRG_MPI_CODE, DRG_REIMBURSEMENT, DRG_MDC_VALUE, DRG_WEIGHT |  |
| HSP_ACCT_PAT_CSN | This table contains hospital account patient contact serial number (CSN) information from the Hospital Accounts Receivable (HAR) m | HSP_ACCOUNT_ID, LINE, PAT_ID, PAT_ENC_CSN_ID, PAT_ENC_DATE_REAL, PAT_ENC_DATE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| HSP_ACCT_PX_LIST | This table contains hospital account final procedure list information from the Hospital Accounts Receivable (HAR) master file. | HSP_ACCOUNT_ID, LINE, FINAL_ICD_PX_ID, PROC_DATE, PROC_PERF_PROV_ID, PROC_EVENT_NUMBER, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| HSP_ADMIT_DIAG | The HSP_ADMIT_DIAG table contains information on admission diagnoses. This table is based on patient contact serial number. | PAT_ID, PAT_ENC_DATE_REAL, LINE, DX_ID, ADMIT_DIAG_TEXT, CM_CT_OWNER_ID, PAT_ENC_CSN_ID |  |
| HSP_ATND_PROV | The HSP_ATND_PROV table contains information on inpatient or outpatient attending providers. This table is based on PAT_ENC_CSN_ID | PAT_ID, PAT_ENC_DATE_REAL, LINE, ATTEND_FROM_DATE, ATTEND_TO_DATE, PROV_ID, ED_ATTEND_YN, CM_CT_OWNER_ID |  |
| HSP_DISCH_DIAG | The HSP_DISCH_DIAG table contains information on inpatient discharge diagnoses. Each record in this table is based on PAT_ENC_CSN_ | PAT_ID, PAT_ENC_DATE_REAL, LINE, DX_ID, DISCH_DIAG_CMNT, CM_CT_OWNER_ID, PAT_ENC_CSN_ID |  |
| HSP_ISOLATION | *** Deprecated *** This view is deprecated in favor of the ISOLATIONS table as that now includes all isolations. ****** The HSP_IS | PAT_ID, PAT_ENC_DATE_REAL, LINE, ISOLATION_C, ISO_ADDED_TIME, ISO_ADDED_USER_ID, ISO_RMVD_TIME, ISO_RMVD_USER_ID |  |
| HSP_TRTMT_TEAM | The HSP_TRTMT_TEAM table contains information on inpatient treatment teams. Each record in this table is based on PAT_ENC_CSN_ID. | PAT_ID, PAT_ENC_DATE_REAL, LINE, PROV_ID, TRTMNT_TEAM_REL_C, TRTMNT_TM_BEGIN_DT, TRTMNT_TM_END_DT, TRTMNT_TM_ED_YN |  |
| IDENTITY_ID | The IDENTITY_ID table contains the system master person index ID numbers for your patients. Each patient may have multiple master  | PAT_ID, LINE, IDENTITY_ID, IDENTITY_TYPE_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, EPI_FROM_DATE, EPI_TO_DATE |  |
| IDENTITY_ID_HX | The IDENTITY_ID_HX table contains the system master person index ID History for your patients. Each patient may have multiple mast | PAT_ID, LINE, ID_HX, ID_CHG_DATE, ID_TYPE_HX, ID_CHG_USER_ID, ID_CHG_TYPE_C, IDENTITY_NEW_ID |  |
| IDENTITY_ID_TYPE | The IDENTITY_ID_TYPE table contains the list of ID Types in your system. | ID_TYPE, ID_TYPE_NAME, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RECORD_STATUS_C, ID_INI_C, ABBR, ID_NUM_RULES_C |  |
| IDENTITY_SER_ID | The IDENTITY_SER_ID table contains the system master person index ID numbers for your providers. Each provider may have multiple m | PROV_ID, LINE, IDENTITY_ID, IDENTITY_TYPE_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, MPI_ID_FROM_DATE, MPI_ID_TO_DATE |  |
| IDENTITY_SER_ID_HX | The IDENTITY_SER_ID_HX table contains the system master person index ID History for your providers. Each provider may have multipl | PROV_ID, LINE, ID_HX, ID_CHG_TIME, ID_TYPE_HX, ID_CHG_USER_ID, IDENTITY_NEW_ID, OLD_PROV_ID |  |
| ILLICIT_DRUG_TYPES | This table contains patient information related to the illicit drug type category. | PAT_ENC_CSN_ID, LINE, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, ILLICIT_DRUG_TYPE_C |  |
| IMMUNE | The IMMUNE table contains data for immunizations ordered through clinical system. May also contain information on immunizations as | IMMUNE_ID, PAT_ID, IMMUNZATN_ID, IMMUNE_DATE, DOSE, ROUTE_C, SITE_C, MFG_C |  |
| IMM_ADMIN | The IMM_ADMIN table contains information about the immunization administered. The rows included in this table are items from DXR ( | DOCUMENT_ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, IMM_TYPE_ID, IMM_TYPE_FREE_TEXT, IMM_DATE, IMM_DOSE |  |
| INDICATIONS_OF_USE | This table contains imported indications of use available for the medication. | MEDICATION_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, INDICATIONS_USE_ID, GRP_VEN_C, DFLT_VEN_YN, INDICATION_LIC_YN |  |
| INFECTIONS | This table contains basic information about patient infections. | INFECTION_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RECORD_STATUS_C, INFECTION_RECORD_TYPE_C, PAT_ID, PAT_ENC_CSN_ID, INFECTION_TYPE_C |  |
| INTERF_SPEC_STAT | This table displays the interface status for a given order. | ORDER_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, INTERF_ID, INTERF_SPEC_STAT_C, VERIFY_STATUS_C, STATUS_DTTM |  |
| IP_COMP_FLOWSHEET | This table displays completed flowsheet row information for Inpatient (INP) records. | INPATIENT_DATA_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, COMPLETE_FLOW_ROWS, ROW_STATUS_C, UPDATE_INSTANT_TM, UPDATE_USER_ID |  |
| IP_DATA_STORE | This table contains generic information related to a patient's inpatient stay, including data on patient education, notes, and oth | INPATIENT_DATA_ID, RECORD_STATUS_NAME, PAT_ID, TEMPLATE_ID, DISCH_INST_HNO_ID, EDU_STATUS_NM, EDU_NOBARRIER_C, EDU_SPOKEN |  |
| IP_FLOWSHEET_ROWS | This table contains flowsheet row (FLO) data for an encounter. This table is a key table in tying LDA assessment row lines in flow | INPATIENT_DATA_ID, LINE, FLO_MEAS_ID, ROW_TEMPLATE, ROW_VARIANCE_NAME, FLOWSHT_ROW_NAME, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| IP_FLO_CUSTOM_LIST | This table contains the possible choices for this flowsheet row. It also contains the corresponding charge row values and trigger  | ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, CM_CT_OWNER_ID, CUST_LIST, CUSTLST_EXTID_TP_C, CUSTLIST_EXT_ID |  |
| IP_FLO_GP_DATA | This table contains generic information about flowsheet groups/rows. | FLO_MEAS_ID, FLO_MEAS_NAME, FLO_DIS_NAME, FLO_ROW_NAME, VALUE_TYPE_NAME, MIN_VALUE, MAX_VALUE, UNIT | **Primary table** in this group (102 cols). Overflow siblings joined on shared key: IP_FLO_GP_DATA_2 (21 cols). Prefer t |
| IP_FLO_LDA_TYPES | This table contains the groups that this flowsheet group (LDA) can be sorted into. This allows for easy reporting. | ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, CM_CT_OWNER_ID, LDA_TYPE_OT_C, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| IP_FLO_MEASUREMNTS | This table contains the list of FLO records which belong to the group. | ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, CM_CT_OWNER_ID, MEASUREMENT_ID, STRT_REMOVED_YN, AN_HIDE_ROW_YN |  |
| IP_FLT_DATA | This table contains information related to defined flowsheet templates. | TEMPLATE_ID, TEMPLATE_NAME, DISPLAY_NAME, GROUP_COL_WIDTH, NAME_COL_WIDTH, TIME_INTERVAL, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| IP_FLWSHT_MEAS | This table contains the patient-specific measurements from flowsheets. | FSD_ID, LINE, FLO_MEAS_ID, OCCURANCE, RECORDED_TIME, ENTRY_TIME, TAKEN_USER_ID, ENTRY_USER_ID |  |
| IP_FLWSHT_REC | This table contains linking information associated with flowsheet records. | FSD_ID, INPATIENT_DATA_ID, RECORD_DATE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, DAILY_NET, UPDATE_DATE, PAT_ID |  |
| IP_FREQUENCY | This table contains data on discrete frequency (EFQ) records. | FREQ_ID, FREQ_NAME, FREQ_TYPE, APPLIES_TO, NUMBER_OF_TIMES, TIME_UNIT, NOW_YN, PRN_YN |  |
| IP_LDA_NOADDSINGLE | This table stores LDA information for a patient. A record is created in LDA for insertion of every line, drain, airway, or wound f | IP_LDA_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, PAT_ID, PAT_ENC_CSN_ID, FLO_MEAS_ID, REMOVAL_INSTANT, PLACEMENT_INSTANT |  |
| IP_NURSE_NOTES | This table displays information for nurse notes. | INPATIENT_DATA_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, NURSE_NOTE_TYPE_C, NURSE_NOTE_STATUS_C, NURSE_AUTHOR_ID, NURSE_NOTE_INST_TM |  |
| IP_ORDER_REC | This table contains Inpatient order reconciliation information. | EVENT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RECON_ORD_ID, EVENT_LINE_NUM, REC_ACTION_C, REC_REORDER_ID |  |
| ISOLATIONS | This table contains patient isolation data. | ISOLATION_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RECORD_STATUS_2_C, PAT_ID, PAT_ENC_CSN_ID, ISOLATION_C, ISOLATION_STATUS_C |  |
| LAB_AP_MULT | Lab Anatomic Pathology multiple no-add items. | REQUISITION_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, AP_CASE_HOLD_C |  |
| LAB_CASE_DB_MAIN | The main table for Lab Anatomic Pathology cases. It contains mostly items that do not change much over time. | CASE_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CASE_ACCESSION_DTTM, CASE_RECEIVED_DTTM, CASE_OVERDUE_DTTM, CASE_PAT_ID, CASE_GROUPER_ID |  |
| LAB_CASE_INFO | Lab Anatomic Pathology case information. | REQUISITION_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CASE_TYPE_ID, CASE_NUM, AP_CASE_STATUS_C |  |
| LAB_CASE_RESULT_DX | This table contains result diagnosis information for anatomic pathology cases. | CASE_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RESULT_DX_ID |  |
| LAB_PROFILE | This table contains basic information about your labs. These are LDF records where the record type (item LDF 27) is set to departm | LAB_ID, LAB_NAME, LAB_ABBR, LDF_TYPE_C, LAB_STATUS_C, LAB_LINK_DEP_ID, LAB_LLB_ID, EXTERNAL_LAB_YN |  |
| LAB_SECTION | This table contains information about your lab sections. These are LDF records where the record type (item LDF 27) is set to secti | SECTION_ID, LDF_TYPE_C, LAB_ID, SECTION_NAME, SECTION_ABBR, SECTION_STATUS_C, OTSTND_LIST_REFRESH, LLB_LAB_ID |  |
| LAB_SMT_NOADD | Table for no-add single response items on the submitter record. | RECORD_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RECORD_NAME, RECORD_STATUS_C, PARENT_SUBMITTER_ID, SHARE_PAT_YN, EMR_PARTICIPANT_C |  |
| LD_COMPLICATIONS | Labor and delivery complications. These complications are documented in the Delivery Summary. | SUMMARY_BLOCK_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, LD_COMPLICATIONS_C |  |
| LENGTH_OF_STAY | The LENGTH_OF_STAY table contains information about the duration of the inpatient stay for a hospital encounter. It contains infor | PAT_ENC_CSN_ID, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, LENGTH_OF_STAY_DAYS, LENGTH_OF_STAY_MINS, INPATIENT_DAYS |  |
| LINKED_CHARGEABLES | This table contains information about chargeable records linked to orderable or performable procedure records. An orderable or per | PROC_ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, CM_CT_OWNER_ID, LINKED_CHRG_ID, CHRG_LINK_TYPE_C, CHARGE_TYPE_C |  |
| LNC_DB_MAIN | This is the primary table for Logical Observation Identifiers Names and Codes (LOINC?) information. | RECORD_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, LOINC_CODE_NM, RECORD_STATUS_C, LNC_REC_TYP_C, LNC_VER, LNC_VER_DT |  |
| MAJOR_RULES | This table contains the list of rule records that contribute to the acuity scoring systems. | ACUITY_SYSTEM_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, MAJOR_RULES_ID, LINKED_RULE_TYPE_C |  |
| MAR_ADMIN_ALERT | This table contains links to the alert data (ALT) displayed during medication administrations. | ORDER_MED_ID, GROUP_LINE, VALUE_LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, MAR_ALERT_ID |  |
| MAR_ADMIN_INFO | This table contains the currently active medication administration data. This includes all scheduled and acted upon administration | ORDER_MED_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, TAKEN_TIME, MAR_ORIG_DUE_TM, EDITED_LINE, SCHEDULED_TIME |  |
| MAR_FSD_LINK | This table contains links to flowsheet data (FSD) saved as part of medication administrations. | ORDER_MED_ID, GROUP_LINE, VALUE_LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, MAR_FLO_FSD_ID |  |
| MAR_FSD_LINK_LINE | This table contains the line counts for the linked administrations that are connected through override pull linking. | ORDER_MED_ID, GROUP_LINE, VALUE_LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, MAR_FLO_FSD_LINE |  |
| MAR_OVRD_LINK | This table contains the order IDs for medications that are connected through override pull linking. | ORDER_MED_ID, GROUP_LINE, VALUE_LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, OVRD_LNK_ORDER_ID |  |
| MDS_RECS | This table contains data on Minimum Data Set (MDS) assessments. An MDS assessment is represented by a Registry Data (RDI) record w | REGISTRY_DATA_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RECORD_STATUS_C, REGISTRY_ID, REGISTRY_TYPE_C, PAT_ID, ARD_TARGET_DATE | **Primary table** in this group (101 cols). Overflow siblings joined on shared key: MDS_RECS_2 (7 cols). Prefer this tab |
| MEDICAL_COND_INFO | This table contains basic no-add information about medical conditions. | MEDICAL_COND_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, MEDICAL_COND_NAME, RECORD_STATE_C, EXTERNAL_ID_TYPE_C, EXTERNAL_IDENTIFIER, REPL_MED_COND_ID |  |
| MEDICAL_HX | The MEDICAL_HX table contains data from medical history contacts entered in clinical system patient encounters. Since one patient  | PAT_ID, PAT_ENC_DATE_REAL, LINE, CONTACT_DATE, END_HIST_DATE_REAL, DX_ID, ICD9_CODE, MEDICAL_HX_DATE |  |
| MEDS_REV_HX_LIST | This table lists the patient's current medications from each time a user reviewed the patient's medications. Reviewing user and ot | PAT_ID, CONTACT_SERIAL_NUM, LINE_COUNT, VALUE_COUNT, MEDICATION_ORDER_ID, TAKING_YN, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| MED_DISPENSE | This table contains information about a patient's med dispense history from a third-party interface. This information can be helpf | DOCUMENT_ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, EXT_DRUG_DESP, EXT_MED_REF_ID, EXT_DRUD_ID_STR, EXT_MED_ERX_ID |  |
| MPI_CSID_NUM | Table contains the Identity visit IDs. | PAT_ENC_CSN_ID, LINE, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, MPI_CSID, MPI_CSID_TYPE_ID |  |
| MULT_DISC_DX | This table contains information on the defined multidisciplinary diagnoses/problems. | PROBLEM_ID, NAME, SYSTEM_C, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RECORD_STATUS_C, DISPLAY_NAME |  |
| MYC_MESG | This table contains information on messages sent to and from web-based chart system patients. | MESSAGE_ID, CREATED_TIME, MYC_MSG_TYP_C, PARENT_MESSAGE_ID, INBASKET_MSG_ID, PAT_ID, PAT_ENC_DATE_REAL, FROM_USER_ID |  |
| MYC_MESG_RCP_POOL | This table holds the final pool recipients (HIP records) for this Patient Access Message (WMG) record. | MESSAGE_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, IB_POOL_RECIP_ID |  |
| MYC_MESG_RCP_STAFF | This table holds the In Basket Staff Recipients (I WMG 196) item, which is the final staff (EMP) recipients for this Patient Acces | MESSAGE_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, IB_STAFF_RECIP_ID |  |
| MYC_PATIENT | The MYC_PATIENT table contains one row for each web-based chart system account. The data contained in each row consists of basic a | MYPT_ID, PAT_ID, PROXY_ACCOUNT_YN, LOGIN_NAME, MYC_STATUS_C, LAST_LOGIN_TIME, NUM_FAILED_LOGINS, FORCE_PWD_CHG_YN | **Primary table** in this group (102 cols). Overflow siblings joined on shared key: MYC_PATIENT_2 (16 cols). Prefer this |
| MYC_PAT_NOTE_VIEW | This table contains information about the patient that viewed this note and when the viewing was done. | NOTE_ID, CONTACT_DATE_REAL, LINE, PAT_ID, PATIENT_VIEW_TIME, CM_CT_OWNER_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| NAVIGATOR_SECTIONS | The NAVIGATOR_SECTIONS table contains information about navigators. Only navigators that are sections (I LVN 100=3) are included. | NAVIGATOR_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, SECTION_CAPTION, SECTION_NAME, SECTION_DESCRIPTOR, RELEASED_NAVIGATOR_ID, REL_NAVIGATOR_CALC_LOCAL_DTTM |  |
| NEPHROLOGY_INFO | The NEPHROLOGY_INFO table contains information about a patient's dialysis episode. The records included in this table are HSB reco | EPISODE_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CONTACT_TYPE_ID, EPISODE_STATUS_C, DEPARTMENT_ID, COMMENTS, PAT_ID |  |
| NOTE_AMBIENT_SECTIONS | Stores ambient note section information. | NOTE_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, AMBIENT_SESSION_SECTION_IDENT, AMBIENT_SESSION_IDENT, AMB_NOTES_SECTION_UPD_FLAG_YN, UPDATED_SECTION_NOTE_ID |  |
| NOTE_ATTRIBUTION | This table stores the attribution of a note. | NOTE_CSN_ID, LINE, NOTE_ID, CONTACT_DATE_REAL, CONTACT_DATE, NOTEATTR_USER_ID, NOTEATTR_SOURCE_C, NOTEATTR_CHAR_COUNT |  |
| NOTE_ENC_INFO | This table contains information from overtime single-response items about General Use Notes (HNO) records. Contact creation logic  | NOTE_ID, CONTACT_SERIAL_NUM, CONTACT_DATE_REAL, LOGICAL_OWNER_ID, PHYSICAL_OWNER_ID, CM_CT_OWNER_ID, EXTER_DOCUMENT_ID, COSIGN_INSTANT_DTTM | **Primary table** in this group (99 cols). Overflow siblings joined on shared key: NOTE_ENC_INFO_2 (20 cols). Prefer thi |
| NOTE_SMARTLINK_IDS | This table stores the SmartLink IDs used by the notes. | NOTE_CSN_ID, LINE, NOTE_ID, CONTACT_DATE_REAL, CONTACT_DATE, SMARTLINKS_ID |  |
| NOTE_SMARTPHRASE_IDS | This table stores the SmartPhrase IDs used by the notes. | NOTE_CSN_ID, LINE, NOTE_ID, CONTACT_DATE_REAL, CONTACT_DATE, SMARTPHRASES_ID |  |
| NOTE_WRITE_TIMING | The length of time a user spends working on a note. | NOTE_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, WRITE_USER_ID, OPEN_EDIT_UTC_DTTM, START_EDIT_UTC_DTTM, SAVE_EDIT_UTC_DTTM |  |
| OBGYN_STAT | Table for the converted OB/Gyn status structure. | PAT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, OBGYN_STAT_C, APP_INST_UTC_DTTM, UPDT_INST_UTC_DTTM, UPDATE_USR_ID |  |
| OB_DEL_INDUCT_RSN | This table contains the category values which correspond to indications for induction. This data comes from the Delivery Summary a | SUMMARY_BLOCK_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, INDUCTION_REASON_C |  |
| OB_DEL_PROC | This table contains the category values which correspond to procedures that occur during or immediately following the delivery. Th | SUMMARY_BLOCK_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, DEL_PROC_C |  |
| OB_HISTORY | Stores the patients OB history. Only the most recent history contact is in this view. | PAT_ENC_CSN_ID, LINE, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, OB_HX_MULT_PREG_GRP, OB_HX_OUTCOME_DT |  |
| OB_HSB_DATING | This table contains the associated information about the criteria for determining the estimated date of delivery for this pregnanc | SUMMARY_BLOCK_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, OB_DT_EVENT_C, OB_DT_DTESYS_DT, OB_DT_DTEUSR_DT, OB_DT_GA_SYS |  |
| OB_HSB_DELIVERY | This table contains information about the delivery for this pregnancy, as entered in Stork's Delivery Summary activity. | SUMMARY_BLOCK_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, OB_DEL_2ND_STAGE_HR, OB_DEL_1ST_STAGE_HR, OB_DEL_1ST_STAGE_M, OB_DEL_2ND_STAGE_M, OB_DEL_3RD_STAGE_M | **Primary table** in this group (101 cols). Overflow siblings joined on shared key: OB_HSB_DELIVERY_2 (19 cols). Prefer  |
| OB_HSB_DELIVERY_2 | This table contains information about the delivery for this pregnancy, as entered in Stork's Delivery Summary activity. | SUMMARY_BLOCK_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, AUGMENTATION_DTTM, DEL_LIVING_CMT, DEL_ADDL_CMT, OB_HX_LIVING_STAT_C, OB_LAST_KNOWN_LIV_C | **Overflow table** for OB_HSB_DELIVERY (101 cols). Contains additional columns for the same records — join on the shared |
| OB_HSB_DEL_CMPLCTN | This table contains information about the complications encountered during the delivery for this pregnancy. | SUMMARY_BLOCK_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, OB_DEL_COMPLIC_ID, UPDATE_DATE |  |
| OB_HSB_DEL_EPISIO | This table contains information about any episiotomies performed to aid the delivery for this pregnancy. | SUMMARY_BLOCK_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, OB_DEL_EPISIO_C |  |
| OB_HSB_DEL_INDUCT | This table contains information about any methods used to induce delivery for this pregnancy. | SUMMARY_BLOCK_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, OB_DEL_INDUCTION_C |  |
| OB_HSB_DEL_RIPETYP | This table contains information about the cervical ripening methods used during labor for this pregnancy. | SUMMARY_BLOCK_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, OBD_CERV_RIPE_TP_C |  |
| OB_HSB_DEL_RP_DTTM | The OB_HSB_DEL_RP_DTTM table contains membrane rupture date and time information recorded from the OB Delivery Summary. It uses th | SUMMARY_BLOCK_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, OB_DEL_RUP_DTTM, RUPT_TM_PRESENT_YN |  |
| OB_HSB_DEL_RUPTCLR | This table contains information about the color of the vaginal fluid that resulted on membrane rupture for this pregnancy. | SUMMARY_BLOCK_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, OB_DEL_RUPTCOLOR_C |  |
| OB_HSB_DEL_RUPTTYP | This table contains information about the how membranes ruptured for this pregnancy. | SUMMARY_BLOCK_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, OB_DEL_RUPTURE_TP_C |  |
| OB_HSB_FLUID_ODOR | This table contains information about the fluid odor from the rupture of membranes during the delivery for this pregnancy. | SUMMARY_BLOCK_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, FLUID_ODOR_C |  |
| OB_HX_HSB | The OB_HX_HSB table contains information about episodes (pregnancy and delivery record HSB records) linked to a patient's OB histo | PAT_ENC_CSN_ID, LINE, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, OB_HX_PREG_EPIS_ID, OB_HX_DEL_REC_ID |  |
| OB_TOTAL | This patient information table holds the obstetrics information for each patient history contact.  The table contains information  | PAT_ENC_CSN_ID, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, OB_MULTIPLE_BIRTHS, OB_THERAPEUTIC_AB, OB_SPONTANEOUS_AB |  |
| OCS_CODE_STATUS | This table contains information about patient code statuses, which are mainly used for documenting compliance reasons and quality. | OCS_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, OCS_NAME, OCS_STATUS_C, CODE_STATUS_C, ACTIVATED_INST, USER_ID |  |
| OMOP_TO_EPIC_PATIENT_CROSSWALK |  |  |  |
| ORDER_ANATOMICAL_REGION | This table stores the anatomical regions of this order. | ORDER_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ANATOMICAL_REGION_C |  |
| ORDER_ATTRIBUTE | The ORDER_ATTRIBUTE table enables you to report on attributes for each order. Currently, you could use value 1 to get all order th | ORDER_ID, LINE, ORD_ATTRIBUTE_C, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| ORDER_COMMENT | The ORDER_COMMENT table allows you to report on comments for non-medication orders. | ORDER_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ORDERING_COMMENT |  |
| ORDER_DISP_INFO | This table contains dispense information for orders. | ORDER_MED_ID, CONTACT_DATE_REAL, CONTACT_DATE, PHARMACY_USR_ID, ACTION_INSTANT, SERVICE_DATE, DISPENSE_PHR_ID, INP_ADMIN_LINE_NO | **Primary table** in this group (101 cols). Overflow siblings joined on shared key: ORDER_DISP_INFO_2 (100 cols), ORDER_ |
| ORDER_DISP_INFO_2 | This table contains dispense information for orders. | ORDER_ID, CONTACT_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, TRACKED_DISP_INFO, RX_TO_PHRM_DEA, RX_XFER_PHARMACY_ID, RX_XFR_LAST_DISP_DT | **Overflow table** for ORDER_DISP_INFO (101 cols). Contains additional columns for the same records — join on the shared |
| ORDER_DISP_MEDS | This table contains information about the dispensed medications for orders. | ORDER_MED_ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, DISP_MED_ID, DISP_QTY, DISP_QTYUNIT_C, DISP_NDC_CSN |  |
| ORDER_DX_MED | The ORDER_DX_MED table enables you to report on the diagnoses associated with medications ordered in clinical system (prescription | ORDER_MED_ID, LINE, PAT_ID, PAT_ENC_DATE_REAL, PAT_ENC_CSN_ID, DX_ID, ICD9_CODE, DX_QUALIFIER_C |  |
| ORDER_DX_PROC | The ORDER_DX_PROC table enables you to report on the diagnoses associated with procedures ordered in clinical system. Since one pr | ORDER_PROC_ID, LINE, PAT_ID, PAT_ENC_DATE_REAL, PAT_ENC_CSN_ID, DX_ID, ICD9_CODE, DX_QUALIFIER_C |  |
| ORDER_IMPRESSION | This table stores impression information for a procedure. | ORDER_PROC_ID, LINE, CM_CT_OWNER_ID, IMPRESSION, ORD_DATE_REAL, CONTACT_DATE |  |
| ORDER_INSTANTIATED | This table contains a list of orders that have been instantiated. | ORDER_ID, LINE, INSTNTD_ORDER_ID, INSTNTD_ORD_TYPE_C, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| ORDER_LAST_EDIT | This table is designed to keep track of the most recent edits made to an order. It reports on the action taken, as well as when an | ORDER_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ORD_LST_ED_INST_TM, ORD_LST_ED_CLIENT, ORD_LST_ED_ACTION_C, ORD_LST_ED_USER_ID |  |
| ORDER_MED | The ORDER_MED table enables you to report on medications ordered in EpicCare (prescriptions). We have also included patient and co | ORDER_MED_ID, PAT_ID, PAT_ENC_DATE_REAL, PAT_ENC_CSN_ID, ORDERING_DATE, ORDER_CLASS_C, PHARMACY_ID, COSIGNER_USER_ID | **Primary table** in this group (139 cols). Overflow siblings joined on shared key: ORDER_MED_2 (75 cols), ORDER_MED_3 ( |
| ORDER_MEDINFO | The ORDER_MEDINFO table is an addendum table for ORDER_MED and enables you to report on detail medication information for each ord | ORDER_MED_ID, MED_LINKED_PROC_ID, MED_CNCT_DAT_REAL, LAST_ADMIN_INST, NUMBER_OF_DOSES, DOSES_REMAINING, RESUME_STATUS_C, MIXTURE_TYPE_NAME |  |
| ORDER_MEDMIXINFO | This table is used to extract ingredient medication information for mixture orders. | ORDER_MED_ID, LINE, MEDICATION_ID, INGREDIENT_TYPE_C, MIN_DOSE_AMOUNT, MAX_DOSE_AMOUNT, DOSE_UNIT_C, FREQUENCY_ID |  |
| ORDER_MED_2 | This table enables you to report on medications ordered in EpicCare or Ambulatory Pharmacy (Prescriptions). This table should be u | ORDER_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, TXT_AUTHPROV_NAME, TXT_AUTHPROV_DEA, TXT_AUTHPROV_PHONE, TXT_AUTHPROV_FAX, TXT_AUTHPROV_STREET | **Overflow table** for ORDER_MED (139 cols). Contains additional columns for the same records — join on the shared prima |
| ORDER_MED_3 | This table enables you to report on medications ordered. This table should be used with ORDER_MED. | ORDER_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ORIG_RX_DOSAGE, ORIG_RX_QUANTITY, ORIG_RX_REFILLS, ORIG_RX_DIRECTIONS, ORIG_RX_PRE_PROV_ID | **Overflow table** for ORDER_MED (139 cols). Contains additional columns for the same records — join on the shared prima |
| ORDER_MED_4 | This table enables you to report on medications ordered. This table should be used with ORDER_MED. | ORDER_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, E_PRES_PAT_NAME, E_PRES_PAT_ADDR, E_PRES_EARLIEST_DAT, E_PRES_DEA_CODE_C, TWO_FACT_AUTH_DTTM | **Overflow table** for ORDER_MED (139 cols). Contains additional columns for the same records — join on the shared prima |
| ORDER_MED_5 | This table enables you to report on medications ordered. This table should be used with ORDER_MED. | ORDER_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, FREE_TXT_SUP_PROV_NAME, FREE_TXT_SUP_PROV_IS_EXT_YN, FREE_TXT_SUP_PROV_DEA, FREE_TXT_SUP_PROV_NPI, FREE_TXT_SUP_PROV_PHONE | **Overflow table** for ORDER_MED (139 cols). Contains additional columns for the same records — join on the shared prima |
| ORDER_MED_6 | This table enables you to report on medications ordered. This table should be used with ORDER_MED. | ORDER_MED_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, AUTH_SER_ADDRESS_ID, ORDER_SER_ADDR_ID, SUP_SER_ADDRESS_ID, NORWAY_FEST_REIMB_PURSUANT_C, NORWAY_REIMBURSEMENT_CODE | **Overflow table** for ORDER_MED (139 cols). Contains additional columns for the same records — join on the shared prima |
| ORDER_MED_SIG | The ORDER_MED_SIG table stores the patient instructions for a prescription as entered by the user. The table should be used in con | ORDER_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, SIG_TEXT | **Overflow table** for ORDER_MED (139 cols). Contains additional columns for the same records — join on the shared prima |
| ORDER_MED_VITALS | This table stores historical patient vitals information for each medication order at the time the order was released. It should on | ORDER_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, WEIGHT_AT_RELEASE, WEIGHT_REL_SOURCE_C, HEIGHT_AT_RELEASE, HEIGHT_REL_SOURCE_C, BSA_AT_RELEASE |  |
| ORDER_METRICS | This table is designed to extract the information necessary to determine where and how orders are being placed in the system. It c | ORDER_ID, AUTH_PROV_ID, ORDERING_PROV_ID, ORDERING_USER_ID, CPOE_YN, LGQ_ORDERSET_ID, USER_OVERRIDE_YN, REORDERED_YN |  |
| ORDER_MODALITY_TYPE | This table stores the anatomical regions of this order. | ORDER_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, MODALITY_TYPE_C |  |
| ORDER_MYC_INFO | When sharing a lab result with a web-based chart system patient, the clinician may choose to attach a Result Comment. Data for the | ORDER_PROC_ID, RELEASE_TIME, PATIENT_NOTE_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RELEASED_YN |  |
| ORDER_NARRATIVE | This table stores the narrative information resulting from a procedure. | ORDER_PROC_ID, LINE, CM_CT_OWNER_ID, NARRATIVE, ORD_DATE_REAL, CONTACT_DATE, IS_ARCHIVED_YN |  |
| ORDER_NARRATIVE_20260217 |  |  |  |
| ORDER_OR_CSN | This table contains the contact serial number (CSN) for the OpTime log/case from which the order was placed. | ORDER_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, OR_CSN_NUM, OR_CSN_TYPE_C, QUICKFORM_ORDER_YN, CASE_DATE_SUGGESTD_YN, AUTO_ADD_TO_AUTH_YN |  |
| ORDER_PARENT_INFO | This table will hold procedure order data where it is sometimes necessary to obtain the information from the parent (or possibly g | ORDER_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, PARENT_ORDER_ID, ORDERING_DTTM, ORD_LOGIN_DEP_ID, PAT_ENC_CSN_ID, PAT_CONTACT_DEP_ID |  |
| ORDER_PROC | The ORDER_PROC table enables you to report on the procedures ordered in the clinical system. We have also included patient and con | ORDER_PROC_ID, PAT_ID, PAT_ENC_DATE_REAL, PAT_ENC_CSN_ID, RESULT_LAB_ID, ORDERING_DATE, ORDER_TYPE_C, PROC_ID | **Primary table** in this group (102 cols). Overflow siblings joined on shared key: ORDER_PROC_2 (100 cols), ORDER_PROC_ |
| ORDER_PROC_2 | The ORDER_PROC_2 table enables you to report on the procedures ordered in the clinical system. This procedure table has the same b | ORDER_PROC_ID, PROV_ID, MOD_BEGIN_TM, MOD_END_TM, CM_LOG_OWNER_ID, CM_PHY_OWNER_ID, OVERRIDE_TM, RVSN_RSN_C | **Overflow table** for ORDER_PROC (102 cols). Contains additional columns for the same records — join on the shared prim |
| ORDER_PROC_3 | The ORDER_PROC_3 table enables you to report on the procedures ordered in the clinical system. This procedure table has the same b | ORDER_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, MAMMO_OUTCOME_C, OLD_RAD_STAT_C, TRANSCRIPTIONIST, ORDERING_MODE_C, PROV_STATUS_C | **Overflow table** for ORDER_PROC (102 cols). Contains additional columns for the same records — join on the shared prim |
| ORDER_PROC_4 | The ORDER_PROC_4 table enables you to report on the procedures ordered in the clinical system. This procedure table has the same b | ORDER_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, QUESR_SERIES_ID, QUESR_SERIES_ANS_ID, LAST_MAMMO_ORD_ID, LAST_MAMMO_LOC_ID, LAST_MAMMO_PROC_NAM | **Overflow table** for ORDER_PROC (102 cols). Contains additional columns for the same records — join on the shared prim |
| ORDER_PROC_5 | The ORDER_PROC_5 table enables you to report on the procedures ordered in the clinical system. This procedure table has the same b | ORDER_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CC_TEX_RECIPIENT, PRIME_DEP_RECIPIENT_ID, CC_DEP_RECIPIENT_ID, FAST_DECISION_C, FUTURE_RELATIVE_EXPECTED_DT_C | **Overflow table** for ORDER_PROC (102 cols). Contains additional columns for the same records — join on the shared prim |
| ORDER_RAD_ACC_NUM | This stores the accession numbers associated with the order. | ORDER_PROC_ID, LINE, CM_LOG_OWNER_ID, CM_PHY_OWNER_ID, ACC_NUM, SPECIMEN_APP_IDN |  |
| ORDER_RAD_PRELIM | This table stores prelimming physician information for imaging procedures. | ORDER_PROC_ID, LINE, CM_LOG_OWNER_ID, CM_PHY_OWNER_ID, PROV_ID, PRELIM_DT, PRELIM_UTC_DTTM, PRELIM_LOCAL_DTTM |  |
| ORDER_RES | The ORDER_RES table contains result finding information for an order. Result findings include mammography pathology results, cardi | FINDING_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RESULT_TYPE_C, FINDING_SIDE_C, FNDG_HQA_ID, FINDING_TYPE_C, RECOMMENDATION_C | **Primary table** in this group (102 cols). Overflow siblings joined on shared key: ORDER_RES_2 (100 cols), ORDER_RES_3  |
| ORDER_RESULTS | This table contains information on results from clinical system orders. This table extracts only the last Orders (ORD) contact for | ORDER_PROC_ID, LINE, ORD_DATE_REAL, ORD_END_DATE_REAL, RESULT_DATE, COMPONENT_ID, PAT_ID, PAT_ENC_DATE_REAL |  |
| ORDER_RES_COMMENT | This table contains result component comments for orders that are populated by the Incoming Results Interface. These result compon | ORDER_ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, CM_CT_OWNER_ID, RESULTS_CMT, COMPONENT_ID, LINE_COMMENT |  |
| ORDER_RES_COMP_CMT | This table contains result component value comments for orders that are populated by the Incoming Results Interface. These result  | ORDER_ID, CONTACT_DATE_REAL, LINE_COMP, CONTACT_DATE, COMPONENT_ID, LINE_COMMENT, CM_CT_OWNER_ID, RESULTS_COMP_CMT |  |
| ORDER_RES_PATH | Stores the pathology codes and malignancy types attached to a pathology result on an order. | FINDING_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, PATH_CODES_C, MALIGNANCY_TYPE_C |  |
| ORDER_RPTD_SIG_HX | This table contains a history of sig-related data for prescriptions, both what the provider initially prescribed and what the pati | ORDER_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, PAT_ENC_CSN_ID, ENTRY_USER_ID, ENTRY_DTTM, ACTION_C |  |
| ORDER_SENSITIVITY | The ORDER_SENSITIVITY table contains information on the sensitivity of orders placed in clinical system. | ORDER_PROC_ID, LINE, PAT_ID, PAT_ENC_DATE_REAL, PAT_ENC_CSN_ID, ORD_DATE_REAL, ORD_END_DATE_REAL, CONTACT_DATE |  |
| ORDER_SIGNED_MED | This table contains the users, providers, and messages related to medication verbal orders and cosign orders. | ORDER_MED_ID, LINE, PAT_ID, PAT_ENC_DATE_REAL, PAT_ENC_CSN_ID, SIGNED_TYPE_C, VERB_COMM_PROV_ID, VERB_SGNER_USER_ID |  |
| ORDER_SMARTSET | This table contains data on smartsets and smartgroups that orders originated from. | ORDER_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, SS_PRL_ID, SS_DAT, SS_SECTION_ID, SS_SECTION_NAME, SS_SECTION_DAT |  |
| ORDER_STATUS | The ORDER_STATUS table contains overtime single response orders information. | ORDER_ID, ORD_DATE_REAL, CONTACT_DATE, CONTACT_NUMBER, CONTACT_TYPE_C, ABNORMAL_YN, ORDER_CREATOR_ID, RESULTING_PROV | **Primary table** in this group (100 cols). Overflow siblings joined on shared key: ORDER_STATUS_2 (7 cols). Prefer this |
| ORDER_SUMMARY | Contains the summary for an order that has been signed. | ORDER_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ORD_SUMMARY |  |
| ORD_APPT_SRL_NUM | This table contains the appointment serial number of the appointments scheduled for an order. | ORDER_PROC_ID, LINE, APPTS_SCHEDULED, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| ORD_BLOOD_ADMIN | Administrable Procedure Items in Orders (ORD). | ORDER_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ADMIN_PX_TYPE_C, BLOOD_UNIT_NUM, BLOOD_CODING_SYS_C, BLOOD_UNIT_NM_SRC_C, BLOOD_PRODUCT_CODE |  |
| ORD_DOSING_PARAMS | This table contains dosing parameters. | ORDER_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ORD_DOSING_WEIGHT, ORD_DW_REC_DTTM, ORD_WT_SOURCE_C, ORD_WT_COMMENTS, ORD_DOSING_HEIGHT | **Primary table** in this group (16 cols). Overflow siblings joined on shared key: ORD_DOSING_PARAMS_2 (4 cols). Prefer  |
| ORD_INDICATIONS | This table stores the indications of use selected for a medication record. | ORDER_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, INDICATIONS_ID |  |
| ORD_LDA_LINK | Links between Orders (ORD) and LDAs. | ORDER_ID, LINE, LDA_ID, LDA_PORT_C, LDA_INST_LINKED_TM, LDA_COMMENT, LDA_INST_RECORD_TM, LDA_USER_ID |  |
| ORD_MED_USER_ADMIN | This table contains user-entered administration instructions. This information is already contained as a part of the table ORD_MED | ORDER_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, MED_USER_ADMN_INSTR, ORDERING_DATE |  |
| ORD_SPECIMEN_INFO | This table contains information on the associated specimen for the order including active status and the accessioning lab system. | ORDER_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, SPECIMEN_LAB_ID, SPECIMEN_ACTIVE_C, SPECIMEN_ACTIVE_UTC_DTTM, SPECIMEN_INACTIVE_UTC_DTTM, SPECIMEN_INACTIVE_C |  |
| ORD_SPEC_QUEST | This table contains order specific questions and their responses. | ORDER_ID, LINE, ORD_QUEST_ID, ORD_QUEST_DATE, IS_ANSWR_BYPROC_YN, ORD_QUEST_COMP, ORD_QUEST_RESP, ORD_QUEST_CMT |  |
| ORD_VARIANT | This table contains a list of all of the variant records associated with the result for this order. | ORDER_ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, VARIANT_ID |  |
| ORGAN | Table for general organ information about transplanted and native organs. | ORG_RECORD_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, TX_DNR_ID, TX_RCP_ID, TX_ORG_SRC_C, TX_DNR_REL_C, ORG_DEATH_ID |  |
| ORGANISM_LIST | Comprehensive organism list generated from order results. | ORDER_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ORGANISM_LIST_ID |  |
| ORG_DETAILS | Details about the organization. Includes external name, phone/e-mail, hours of operation, HSI, URL. | ORGANIZATION_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ORGANIZATION_NAME, RECORD_STATUS_C, ORG_TYPE_C, HEALTH_SYSTEM_ID, ORG_URL |  |
| OR_CASE | The OR_CASE table contains OR management system case records. | OR_CASE_ID, CASE_NAME, SURGERY_DATE, CASE_TYPE_C, CASE_CLASS_C, PAT_ID, PAT_AGE, PAT_CLASS_C | **Primary table** in this group (134 cols). Overflow siblings joined on shared key: OR_CASE_2 (112 cols), OR_CASE_3 (104 |
| OR_CASE_2 | The OR_CASE_2 table enables you to report on surgical and procedural case data. This table has the same basic structure as OR_CASE | CASE_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, SURGICAL_RISK_C, POTENTL_BLOODLOSS_C, AWARENESS_DT, READY_TO_SCHED_C, SURGEON_REQ_LEN | **Overflow table** for OR_CASE (134 cols). Contains additional columns for the same records — join on the shared primary |
| OR_CASE_3 | The OR_CASE_3 table enables you to report on surgical and procedural case data. This table has the same basic structure as OR_CASE | CASE_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, SETUP_TIME_MOD_YN, DFLT_SETUP_MINS, DFLT_CLEANUP_MINS, DFLT_PREP_MINS, DFLT_WRAPUP_MINS | **Overflow table** for OR_CASE (134 cols). Contains additional columns for the same records — join on the shared primary |
| OR_CASE_ADDL_CODES | This table stores the additional codes for the case. | CASE_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, OR_CASE_ADDL_CODE_ID |  |
| OR_CASE_ALL_PROC | The OR_CASE_ALL_PROC table contains OR management system case procedures. | OR_CASE_ID, LINE, OR_PROC_ID, POS_C, LRB_C, ANES_TYPE_C, OP_REG_C, PICKLIST_GEN_C |  |
| OR_CASE_ALL_SURG | The OR_CASE_ALL_SURG table contains OR management system case surgeons. | OR_CASE_ID, LINE, SURG_ID, ROLE_C, SERVICE_C, CASE_BEGIN, CAE_END, TOTAL_LENGTH |  |
| OR_CASE_APPTS_PR | The OR_CASE_APPTS_PR table contains OR management system case appointments.  This table contains pre-operation information. | OR_CASE_ID, APPT_TYPE, LINE, UNIQUE_ID, APPT_PRC_ID, OR_PROC_ID, PROV_ID, DEPT_ID |  |
| OR_CASE_AUDIT_TRL | The OR_CASE_AUDIT_TRL table contains OR management system case audit trail information. | OR_CASE_ID, LINE, AUDIT_ACTION_C, AUDIT_USER_ID, AUDIT_DATE, AUDIT_REQUEST_BY, AUDIT_COMMENTS, CM_PHY_OWNER_ID |  |
| OR_CASE_ORDER_IDS | This table contains the IDs of the orders which were used to create a case. | CASE_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ORDER_ID |  |
| OR_CASE_SCHED_HIST | The OR_CASE_SCHED_HIST table contains OR management system case scheduling history. | OR_CASE_ID, LINE, ROOM_ID, HIST_DATE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, HIST_SCHED_USER_ID, HIST_SCHED_DATE |  |
| OR_GRP | This table contains general information about the OR Surgeon Group (OGP) record. | GROUP_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, GROUP_NAME, RECORD_STATUS_C, GROUP_DATE, CONTACT_NUMBER |  |
| OR_GRP_SURGEON | The OR_GRP_SURGEON table contains OR management system surgeon groups. | GROUP_ID, LINE, SURGEONS_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| OR_IMP | The OR_IMP table contains implant information. | IMPLANT_ID, IMPLANT_NAME, PO_NUMBER, ABBREVIATION, IMPLANT_TYPE_C, MANUFACTURER_C, STATUS_C, SMDA_YN | **Primary table** in this group (101 cols). Overflow siblings joined on shared key: OR_IMP_2 (101 cols), OR_IMP_3 (40 co |
| OR_IMP_IMPLANT | The OR_IMP_IMPLANT table contains implantation information for implants that were marked as being implanted for a surgery or invas | IMPLANT_ID, LINE, IMPLANTED_DATE, IMPLANT_LOG_ID, MANUF_NOTIFY_DATE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, IMPLANTED_TIME |  |
| OR_LNLG_IMPLANTS | This table contains the implants information for the surgical/invasive procedure log (ORL). | RECORD_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, IMP_INV_TYPE_ID, IMP_NO_INV_ITEM_YN, IMPLANT_ID, IMPLANT_ACTION_C, IMPLANT_NUM_USED |  |
| OR_LOC | The OR_LOC table contains information about surgical, radiology, and invasive lab locations. | LOC_ID, DEP_ID, TR_SKIP_SAT_YN, TR_SKIP_SUN_YN, EOD_OFFSET_DAYS, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, LOCATION_TYPE_C |  |
| OR_LOG | The OR_LOG table contains information about surgical and procedural log (ORL) records. | LOG_ID, LOG_NAME, SURGERY_DATE, CASE_TYPE_C, CASE_CLASS_C, TRAUMA_CASE_YN, PAT_ID, PAT_AGE | **Primary table** in this group (124 cols). Overflow siblings joined on shared key: OR_LOG_2 (109 cols), OR_LOG_3 (13 co |
| OR_LOG_ADDL_CODES | This table stores the additional codes for the log. | LOG_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, OR_LOG_ADDL_CODE_ID |  |
| OR_LOG_ALL_PROC | The OR_LOG_ALL_PROC table contains OR management system log procedures. | LOG_ID, LINE, OR_PROC_ID, POS_C, ANES_TYPE_C, LRB_C, OP_REG_C, WND_CLS_C |  |
| OR_LOG_ALL_STAFF | The OR_LOG_ALL_STAFF table contains information about all staff members associated with a procedural case that has been performed. | LOG_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, STAFF_TYPE_MAP_C, STAFF_ID, ROLE_C, SERVICE_C |  |
| OR_LOG_ALL_SURG | The OR_LOG_ALL_SURG table contains OR management system log surgeons. | LOG_ID, LINE, SURG_ID, ROLE_C, SERVICE_C, START_TIME, END_TIME, TOTAL_LENGTH |  |
| OR_LOG_CASE_TIMES | The OR_LOG_CASE_TIMES table contains OR management system log timing information. | LOG_ID, LINE, TRACKING_EVENT_C, TRACKING_TIME_IN, TRACKING_TIME_OUT, TRACKING_TIME_ELPS, TRACK_EVENT_TYPE_C, TRACKING_STATUS_C |  |
| OR_LOG_CHARGES | This table contains the charge information for the surgical log (ORL) record. | LOG_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, UNIQUE_ID, CHARGE_SOURCE_C, UPDATE_ID, CHARGE_CANCELED_YN |  |
| OR_LOG_LN_IMPLANT | This table contains the line IDs (ORM) for the implant information of the surgical/invasive procedure log (ORL). | LOG_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, IMPLANTS_ID |  |
| OR_LOG_TIMING_EVENTS | The OR_LOG_TIMING_EVENTS table contains information about case timing events associated with a procedural case that has been perfo | LOG_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, TIMING_EVENT_C, TIMING_EVENT_DTTM |  |
| OR_LOG_VIRTUAL | The OR_LOG_VIRTUAL table contains virtual items for the OR management system log records. | LOG_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, PRIMARY_ANES_TYPE_C, RESP_ANES_ID, PRIMARY_PROC_ID, PATIENT_AGE, NUMBER_OF_PROCS |  |
| OR_OTA | The OR_OTA table contains information about the release of blocks in the OR Scheduling system. | RECORD_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CONTACT_NUM, CONTACT_DATE, MOD_TYPE_C, REL_DAYS_IN_ADVANC, SER_RECORD_ID |  |
| OR_PROC | The OR_PROC table contains OR management system procedures. | OR_PROC_ID, PROC_NAME, INACTIVE_YN, ABBREV, PROC_MOD_YN, USESETNGS_FROM_ID, TYPE_OF_PROC_C, USE_CALC_TIMES_YN | **Primary table** in this group (101 cols). Overflow siblings joined on shared key: OR_PROC_2 (17 cols). Prefer this tab |
| OR_PROC_CPT_ID | The OR_PROC_CPT_ID table contains OR management system procedure CPT codes. | OR_PROC_ID, LINE, CPT_ID, REAL_CPT_CODE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, IS_DEFAULT_CODE_YN |  |
| OR_ROOM_TEMPLATE | The OR_ROOM_TEMPLATE table includes scheduling template slot patterns for operating rooms. A slot is an exclusive range of reserve | ROOM_ID, DAY_OF_THE_WEEK_C, PATTERN_START_DATE, PATTERN_END_DATE, SLOT_TYPE_C, SLOT_START_TIME, SLOT_END_TIME, PUBLIC_SLOT_YN |  |
| OR_ROOM_TEMPLATE_AUDIT | The OR_ROOM_TEMPLATE_AUDIT table stores the audit trail for OR templates. | DEPARTMENT_ID, ROOM_ID, AUDIT_DTTM, LINE, AUDIT_ACTION_C, AUDIT_USER_ID, TEMPLATE_START_DATE, TEMPLATE_END_DATE |  |
| OR_SER_SURG_SRVC | The OR_SER_SURG_SRVC table contains OR management system surgical services. | PROV_ID, LINE, SERVICE_C, ALLOW_ALL_SERV_YN, LOC_ID, ALLOW_ALL_PROC_YN, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| OR_SPLY | The OR_SPLY table contains inventory item records. | SUPPLY_ID, SUPPLY_NAME, ACTIVE_YN, ABBR, CHARGE_CODE, CHARGE_PER_UNIT, COST_PER_UNIT, NAME |  |
| OTHER_COMMUNCTN | This table stores miscellaneous communication devices that can be used to reach the patient. Examples are mobile phone and pager. | PAT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, OTHER_COMMUNIC_C, OTHER_COMMUNIC_NUM, START_DAY_C, END_DAY_C |  |
| OTP_INFO | This table stores basic information about a treatment plan order, such as its status, display name, which medication or procedure  | OTP_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ORDER_TYPE_C, PROC_ID, ORDER_DESC, DISPLAY_NAME, PRESEL_DISPLAY_NAME | **Primary table** in this group (100 cols). Overflow siblings joined on shared key: OTP_INFO_1 (63 cols), OTP_INFO_2 (69 |
| OTP_INFO_1 | This table is a continuation of related table OTP_INFO. It stores additional information about a treatment plan order, such as ver | OTP_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, TRANSPORTATION_C, IP_DISC_INTERVAL_ID, IP_STANDING_COUNT, IP_STAND_CNT_TYPE_C, IP_INCLUDE_NOW_C | **Overflow table** for OTP_INFO (100 cols). Contains additional columns for the same records — join on the shared primar |
| OVC_SPECIMENS | The OVC_SPECIMENS table contains information about which specimens a container is related to. For Anatomic Pathology case tracking | CONTAINER_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, SPECIMEN_ID |  |
| PATIENT | The PATIENT table contains one record for each patient in your system. The data contained in each record consists of demographics, | PAT_ID, PAT_NAME, ADD_LINE_1, ADD_LINE_2, CITY, STATE_C, COUNTY_C, COUNTRY_C | **Primary table** in this group (137 cols). Overflow siblings joined on shared key: PATIENT_2 (69 cols), PATIENT_3 (103  |
| PATIENT_2 | This table supplements the PATIENT table. It contains basic information about patients. | PAT_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RECORD_TYPE_6_C, BIRTH_TM, DEATH_TM, FAX, CITIZENSHIP_C | **Overflow table** for PATIENT (137 cols). Contains additional columns for the same records — join on the shared primary |
| PATIENT_3 | This table supplements the information contained in the PATIENT table. It contains basic information about patients, such as the p | PAT_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, LACT_STAT_CUR_C, LACT_STAT_INST_DTTM, LACT_STAT_CSN, LACT_STAT_USER_ID, HM_PLAN_DISP_FLAG | **Overflow table** for PATIENT (137 cols). Contains additional columns for the same records — join on the shared primary |
| PATIENT_4 | This table supplements the PATIENT table. It contains basic information about patients. | PAT_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, INTERPRT_NEEDED_CMT, DENT_COMMENT, EPT_LOG_DATE, ESRD_G_START_DT, ESRD_B_START_DT | **Overflow table** for PATIENT (137 cols). Contains additional columns for the same records — join on the shared primary |
| PATIENT_5 | This table supplements the PATIENT table. It contains basic information about patients. | PAT_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, PHYSICAL_IMPAIRED_C, MEMORY_IMPAIRED_C, SPEECH_IMPAIRED_C, DISABLED_VETERAN_C, VA_RECOGNIZED_C | **Overflow table** for PATIENT (137 cols). Contains additional columns for the same records — join on the shared primary |
| PATIENT_ADDRESS |  |  |  |
| PATIENT_ADDRESS_ARCGIS |  |  |  |
| PATIENT_ADDRESS_GEO_CENSUS |  |  |  |
| PATIENT_ADDRESS_GEO_CONGRESSIONAL_DISTRICT_MO |  |  |  |
| PATIENT_ADDRESS_GEO_DISTRICT_MO |  |  |  |
| PATIENT_ADDRESS_GEO_LEGISLATIVE_DISTRICT_MO |  |  |  |
| PATIENT_ADDRESS_STAGE |  |  |  |
| PATIENT_ENC_VIDEO_VISIT | This table contains the video visit related data for a patient that is stored at the patient contact level. | PAT_ENC_CSN_ID, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, PAT_ENC_LVL_VIDEO_VISIT_ID, TH_MODE_VV_CHG_USER_ID, TH_MODE_VV_CHG_REASON |  |
| PATIENT_EXT_DEATH_DATE_HX | This table stores previously entered values for a patient's date of death. | PAT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, EXT_RPT_DEATH_DATE |  |
| PATIENT_MYC | This table contains web-based chart system-related data items that are stored in the Patient (EPT) master file. These items genera | PAT_ID, PAT_ACCESS_CODE, PAT_ACCESS_CODE_TM, PAT_ACCESS_STAT_C, MYCHART_STATUS_C, RECV_EMAIL_YN, ACCESSCODE_STAT_C, DEACT_ACCT_YN |  |
| PATIENT_RACE | This table contains information on a patient's race. | PAT_ID, LINE, PATIENT_RACE_C, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| PATIENT_TYPE | This table contains one record for each patient type for each patient. | PAT_ID, LINE, PATIENT_TYPE_C, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| PAT_ACCT_CVG | The PAT_ACCT_CVG table contains information about a patient?s accounts and coverages. The table will contain one record for each a | PAT_ID, LINE, ACCOUNT_ID, SERV_AREA_ID, ACCOUNT_TYPE_C, TYPE_LINE_NUM, ACCOUNT_ACTIVE_YN, COVERAGE_ID |  |
| PAT_ADDL_ADDR_DETAILS | Stores the patient's additional address details. | PAT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ADDRESS_DETAILS_C, ADDRESS_DETAILS_VAL |  |
| PAT_ADDRESS | This table contains each patient's permanent address (I EPT 50). The primary key for this table is the combination of PAT_ID and L | PAT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ADDRESS |  |
| PAT_ADDR_CHNG_HX | This table keeps track of changes in the patient's address. | PAT_ID, LINE, ADDR_HX_LINE1, ADDR_HX_LINE2, ADDR_HX_LN_EXTRA, CITY_HX, COUNTY_HX_C, STATE_HX_C |  |
| PAT_ALLERGIES | The allergies that are associated with a patient are stored on this table. This table also provides a link from the Patient (EPT)  | PAT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ALLERGY_RECORD_ID |  |
| PAT_CVG_FILE_ORDER | The PAT_CVG_FILE_ORDER table contains information about the filing order of each member's coverages. Since members can have multip | PAT_ID, LINE, COVERAGE_ID, FILING_ORDER, FILING_ORDER_CAT, HOSP_FILE_ORD, HOSP_FILE_ORD_CAT, CM_PHY_OWNER_ID |  |
| PAT_ENC | The patient encounter table contains one record for each patient encounter in your system. By default, this table does not contain | PAT_ID, PAT_ENC_DATE_REAL, PAT_ENC_CSN_ID, CONTACT_DATE, ENC_TYPE_C, ENC_TYPE_TITLE, AGE, PCP_PROV_ID | **Primary table** in this group (143 cols). Overflow siblings joined on shared key: PAT_ENC_2 (101 cols), PAT_ENC_3 (101 |
| PAT_ENC_2 | This table supplements the PAT_ENC table. It contains additional information related to patient encounters or appointments. | PAT_ENC_CSN_ID, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, MERGE_CT_PRV_EXT_ID, CHECK_IN_NO_VISI_YN, COPAY_COINS_FLAG | **Overflow table** for PAT_ENC (143 cols). Contains additional columns for the same records — join on the shared primary |
| PAT_ENC_4 | This table supplements the PAT_ENC, PAT_ENC_2, and PAT_ENC_3 tables. It contains additional information related to patient encount | PAT_ENC_CSN_ID, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, UNAV_TIME_RSN_C, OVBK_OVR_USER_ID, CANC_CHKIN_USER_ID | **Overflow table** for PAT_ENC (143 cols). Contains additional columns for the same records — join on the shared primary |
| PAT_ENC_6 | This table supplements the PAT_ENC, PAT_ENC_2, PAT_ENC_3, PAT_ENC_4, and PAT_ENC_5  tables. It contains additional information rel | PAT_ENC_CSN_ID, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, LINKED_ENC_CSN, PATIENT_ID_METHOD_C, PATIENT_ID_METHOD_TEXT | **Overflow table** for PAT_ENC (143 cols). Contains additional columns for the same records — join on the shared primary |
| PAT_ENC_7 | This table supplements the PAT_ENC, PAT_ENC_2, PAT_ENC_3, PAT_ENC_4, PAT_ENC_5, and PAT_ENC_6 tables. It contains additional infor | PAT_ENC_CSN_ID, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, NOTIFY_REP_ADMSN_C, REP_NOTIFIED_C, NOTIFY_REP_COMMENTS | **Overflow table** for PAT_ENC (143 cols). Contains additional columns for the same records — join on the shared primary |
| PAT_ENC_AMBIENT_SESSIONS | Stores ambient session information from a patient's encounter. | PAT_ENC_CSN_ID, LINE, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, AMBIENT_SESSION_IDENT, DEVICE_LOCAL_IDENT |  |
| PAT_ENC_CURR_MEDS | The PAT_ENC_CURR_MEDS table enables you to report on current (as well as active) medications per encounter as listed in clinical s | PAT_ID, PAT_ENC_DATE_REAL, LINE, PAT_ENC_CSN_ID, CONTACT_DATE, CURRENT_MED_ID, IS_ACTIVE_YN, UPDATE_DATE |  |
| PAT_ENC_DX | The patient encounter diagnosis table contains one record for each diagnosis associated with each encounter level of service. This | PAT_ID, PAT_ENC_DATE_REAL, LINE, CONTACT_DATE, PAT_ENC_CSN_ID, DX_ID, ICD9_CODE, ANNOTATION |  |
| PAT_ENC_FORM_ANS | Table PAT_ENC_FORM_ANS has information for items in related group 20800. | PAT_ENC_CSN_ID, LINE, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, QF_LQF_ID, QF_HQA_ID |  |
| PAT_ENC_HOSP_PROB | The PAT_ENC_HOSP_PROB contains the hospital problems for each hospital encounter. | PAT_ID, PAT_ENC_DATE_REAL, LINE, CONTACT_DATE, PAT_ENC_CSN_ID, PROBLEM_LIST_ID, PRINCIPAL_PROB_YN, CM_CT_OWNER_ID |  |
| PAT_ENC_HSP | This table is the primary table for hospital encounter information. A hospital encounter is a contact in the patient record create | PAT_ID, PAT_ENC_DATE_REAL, PAT_ENC_CSN_ID, ADT_CONTACT, ADT_INITIAL, ADT_PAT_CLASS_C, ADT_BILLING_TYPE_C, ADT_PATIENT_STAT_C | **Primary table** in this group (133 cols). Overflow siblings joined on shared key: PAT_ENC_HSP_2 (78 cols). Prefer this |
| PAT_ENC_HSP_2 | The PAT_ENC_HSP_2 table is the subsequent table for the PAT_ENC_HSP table, which is the primary table for hospital encounter infor | PAT_ENC_CSN_ID, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, EX_DIS_DT_ENTR_DTTM, EX_DIS_TM_ENTR_DTTM, CONTRACT_REG_FLAG | **Overflow table** for PAT_ENC_HSP (133 cols). Contains additional columns for the same records — join on the shared pri |
| PAT_ENC_LETTERS | The patient encounter letters table contains information about letters associated with encounters. | PAT_ENC_CSN_ID, LINE, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, LTR_STATUS_C, LETTER_CREAT_DT |  |
| PAT_ENC_LNK_CASE | Table that extracts the case/log linking information from a patient's encounter. | PAT_ENC_CSN_ID, LINE, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, LINKED_CASE_ID |  |
| PAT_ENC_NO_SHOW | This table contains no-show documentation. When patients do not arrive for an appointment, they are marked as a no-show. Each no-s | PAT_ENC_CSN_ID, LINE, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, NO_SHOW_ACTION_C, NO_SHOW_OUTCOME_C |  |
| PAT_ENC_RSN_VISIT | The PAT_ENC_RSN_VISIT contains the data entered as the Reason for Visit for a clinical system encounter. Each row in this table is | PAT_ID, PAT_ENC_DATE_REAL, PAT_ENC_CSN_ID, LINE, CONTACT_DATE, ENC_REASON_ID, ENC_REASON_NAME, ENC_REASON_OTHER |  |
| PAT_ENC_STAT_HX | This is the ADT encounter status history. It will track changes to the patient's encounter status (I EPT 10115) and confirmation s | PAT_ENC_CSN_ID, LINE, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, UPDATE_USER_ID, UPDATE_TIME |  |
| PAT_EPISODE | The PAT_EPISODE table links patient ID numbers to Episodes of Care records. This is especially helpful for connecting patients to  | PAT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, EPISODE_ID |  |
| PAT_HX_REVIEW | This table contains information about when a patient's history was reviewed and by whom. More detailed information on what kinds o | PAT_ENC_CSN_ID, LINE_COUNT, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, HX_REVIEWED_USER_ID, HX_REVIEWED_DATE |  |
| PAT_LIST | The PAT_LIST table contains patients and the corresponding patient lists that they are members of. | PAT_ID, LINE, LIST_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| PAT_LIST_INFO | The PAT_LIST_INFO table contains the no-add, single response patient list information. | LIST_ID, LIST_DESCRIPTION, RECORD_STATUS_C, LIST_TYPE_C, MASTER_LIST_ID, LIST_SUBTYPE_C, LIST_OWNER, LIST_CREATOR_ID |  |
| PAT_MERGE_HISTORY | This table stores the patient merge history. When the system contains two records that actually represent only one patient, the re | PAT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, PATIENT_MRG_HIST |  |
| PAT_MRN_HX | *** Deprecated *** Some of the deprecated table's data is no longer populated in Chronicles and is no longer available, the rest c | PAT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, MRN_HX, MRN_HX_CHANGE_INST, MRN_HX_CHANGE_STAF, MRN_HX_PAT_NAME |  |
| PAT_MYC_PRXY_ACSS | Proxy access in web based chart system provides the means for one patient to view data for another patient. A typical use of this  | PAT_ID, LINE, PROXY_PAT_ID, MYC_PRXY_RELATN_C, FROM_DATE, TO_DATE, ACCESS_ECL_ID, CM_PHY_OWNER_ID |  |
| PAT_NATIVE_ORG | Table of the patient's native organs. | PAT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ORG_RECORD_ID |  |
| PAT_OCCUPN_HX | This table contains descriptive occupation history for patients recorded for a given encounter.  Each row represents one line of t | PAT_ENC_CSN_ID, LINE, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, HX_OCCUPN, HX_EMPLOYER_ID |  |
| PAT_OR_ADM_LINK | This table stores the link between encounter ID and the associated log or case ID. | PAT_ENC_CSN_ID, PAT_ID, PAT_ENC_DATE_REAL, CM_CT_OWNER_ID, OR_LINK_CSN, OR_LINK_INP_ID, OR_SHARE_PERIOP_YN, OR_SUM_BLOCKS_ID |  |
| PAT_PCP | This table contains the Primary Care Provider (PCP) information for your patients over time. It can also contain data about provid | PAT_ID, LINE, CHANGE_DATE, PCP_PROV_ID, EFF_DATE, TERM_DATE, USER_ID, CHANGE_REQ_BY_C |  |
| PAT_RELATIONSHIPS | Demographic information for patient contacts. | PAT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, PAT_REL_NAME, PAT_REL_ADDRESS, PAT_REL_CITY, PAT_REL_STATE_C |  |
| PAT_RELATIONSHIP_LIST | This table includes the majority of patient contact demographic info, general relationship info, and patient-level relationship in | PAT_RELATIONSHIP_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RECORD_STATUS_C, PAT_ID, PAT_CONTACT_PAT_ID, PAT_LEVEL_RELATIONSHIP_YN, SSN |  |
| PAT_REL_ADDR | This table extracts the related multiple-response item Pat Rel Address (I EPT 1701) item, which stores the addresses of each emerg | PAT_ID, GROUP_LINE, VALUE_LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, PAT_REL_ADDRESS |  |
| PAT_SEXUAL_ORIENTATION | This table contains information about a patient's sexual orientation. | PAT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, SEXUAL_ORIENTATN_C |  |
| PAT_SPEC_CMTS | Specialty Comments saved from SnapShot. | PAT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, SPECIALTY_COM_ID |  |
| PAT_SURG_DATA | This table contains information about items related to surgery, including: primary surgeon, procedure, location, and case and log  | PAT_ENC_CSN_ID, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, CS_SURG_SURGEON_ID, CS_SURG_PROC_ID, CS_SURG_LOCATION_ID |  |
| PAT_UCN_CONVERT | Contains if the patient's notes are converted for UCN. | PAT_ENC_CSN_ID, LINE, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, LINKED_UCN_NOTES_ID |  |
| PNEG_MED_HX | The PNEG_MED_HX table contains data from pertinent negatives medical history contacts entered in clinical system patient encounter | PAT_ENC_CSN_ID, LINE, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, PNEG_MED_HX_ID, PNEG_MED_HX_DT |  |
| PRB_TEMP_GOAL_TEMP | This table stores the goal templates associated with the problem template. | TEMPLATE_PROBLEM_ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CM_CT_OWNER_ID, GOAL_TEMPLATE_ID |  |
| PRB_TEMP_INFO | This table displays information about the problems, goals, and outcomes associated with the template problem record. | TEMPLATE_PROBLEM_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, TEMPLATE_PROB_NAME, TEMPLATE_TYPE_ID, RECORD_STATUS_C, IS_AUTOGENERATED_YN, IS_INDIV_ALLOWED_YN |  |
| PROBLEM | This table contains data on care integrator problems associated with a patient. | PROBLEM_ID, TYPE_PROBLEM_ID, CREATED_DATE, DELETED_DATE, DEL_REASON_C, DISCIPLINE_C, IP_DISC_TYPE_ID, CM_PHY_OWNER_ID |  |
| PROBLEM_LIST | The PROBLEM_LIST table contains data from patients' problem lists in the clinical system. The data in this table reflects the curr | PROBLEM_LIST_ID, PAT_ID, DX_ID, ICD9_CODE, DESCRIPTION, NOTED_DATE, RESOLVED_DATE, DATE_OF_ENTRY |  |
| PROBLEM_LIST_HX | This table contains data relating to the history of problems from patients' problem lists in the clinical system. | PROBLEM_LIST_ID, LINE, HX_PROBLEM_ID, HX_DESCRIPTION, HX_DATE_NOTED, HX_DATE_RESOLVED, HX_COMMENT, HX_DATE_OF_ENTRY |  |
| PROB_GOALS | This table contains data on the discrete goal (IGO) records associated with each problem. | PROBLEM_ID, LINE, GOAL_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| PROC_SPECIMEN_SRC | This table contains the list of sources from which specimens were taken. | PROC_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, SPECIMEN_SOURCE_C |  |
| PROVTEAM_REC_INFO | This table extracts the basic record information for the provider team including the name and the date the record was created. Pro | ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RECORD_NAME, RECORD_STATUS_C, RECORD_TYPE_C, CURRENT_CONTACT, RECORD_CREATION_DT |  |
| PT_GOALS_INFO | This table contains data in the Discrete Goals (IGO) master file that is no-add data. | GOAL_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, USER_ID, GOAL_TEMPLATE_ID, GOAL_TEMPLATE_DAT, PAT_ID, CREATE_INST_DTTM |  |
| QM_GEN_INFO | This table contains general information about the quality measure associated with registry data records. | REGISTRY_DATA_ID, REGISTRY_TYPE_C, PAT_ID, PAT_DATE, QM_SUM_MEASURE_CSN, QM_YEAR, QM_PROV_AND_TIN, QM_ENC_PROV_ID |  |
| RDI_PAT_CSN | This table displays the contact information that is related to the report generated for the ACC Registry. | REGISTRY_DATA_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, PAT_CSN, UPDATE_DATE |  |
| REFERRAL | The REFERRAL table is the primary table for referral information stored in system. | REFERRAL_ID, EXTERNAL_ID_NUM, PAT_ID, PCP_PROV_ID, ENTRY_DATE, RFL_STATUS_C, REFERRING_PROV_ID, VENDOR_ID | **Primary table** in this group (112 cols). Overflow siblings joined on shared key: REFERRAL_2 (100 cols), REFERRAL_3 (5 |
| REFERRAL_DX | The REFERRAL_DX table contains diagnosis information stored with referrals. | REFERRAL_ID, LINE, DX_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, DX_TEXT, DX_CODE_TYPE_C |  |
| REFERRAL_ORDER_ID | This table holds the Order ID for orders which EpicCare fills when dropping this referral. | REFERRAL_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ORDER_ID |  |
| REFERRAL_PX | This table contains information on procedures associated with referrals. This table is related to the REFERRAL_ORDER_ID table. The | REFERRAL_ID, LINE, PX_ID, UNITS_REQUESTED, UNITS_APPROVED, TOTAL_PRICE, NET_PAYABLE, PATIENT_PORTION |  |
| REFERRAL_SOURCE | The REFERRAL_SOURCE table contains information about referral sources. Referral sources can be physicians who write medical referr | REFERRING_PROV_ID, REFERRING_PROV_NAM, PROV_TYPE, FIRST_PROV_SPEC, FIRST_SERV_AREA_ID, SSN, OFFICE_PHONE, DOCTOR_DEGREE |  |
| REFERRAL_SPEC | This table contains information on the specialties for referring providers. | REFERRING_PROV_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RFL_SPECIALTY_C |  |
| REGISTRY_DATA_INFO | This table contains basic information about registry data, including what type of registry data it is. | RECORD_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RECORD_STATUS_C, NETWORKED_ID, RECORD_CREATION_DT, INSTANT_OF_UPD_TM, RELATED_INI |  |
| REG_DATA_HX_MEMBERSHIP | History data on the status changes to registry inclusion. | RECORD_ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, REGISTRY_ID, CHANGE_INSTANT_UTC_DTTM, STATUS_C, STATUS_REASON_C |  |
| REG_DATA_HX_METRICS | This is the history of the registry data's metrics and their associated values. | RDT_ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, HX_MET_ID, HX_MET_LAST_UPD_DTTM, HX_MET_STRING_VAL, HX_MET_VAL_DESC_C |  |
| REPORT_DETAILS | This table contains information about general characteristics of reports containing print groups.  This table includes whether it  | LRP_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, REPORT_NAME, RECORD_STATE_C, TEMP_NAME_EDIT, HTML_REPORT_YN, STYLESHEET_C |  |
| REQ_SPECIMEN | This table contains the specimen IDs for specimens that are related to each requisition. | REQUISITION_ID, LINE, REQ_SPECIMEN_ID, CM_LOG_OWNER_ID, CM_PHY_OWNER_ID |  |
| RESULT_SYNOPTIC | Synoptic result record table. | RESULT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, SYNOPTIC_RESULT_ID |  |
| RESULT_VARIANT | RESULT_VARIANT is the primary table for storing variant result data. | RESULT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, VARIANT_ID, VARIANT_RPT_YN |  |
| RESUME_REPORTED_SIG | This table contains information on how home medications with reported sigs were reconciled at discharge. | EVENT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ORDER_MED_ID, EVENT_LINE_NUM, PAT_SIG_REPLY_C, RPT_SIG_LINE_NUM |  |
| RES_COMPONENTS | Primary table for result component information. | RESULT_ID, RES_TYPE_ID, LINE, LAB_ID, RES_SPECIMEN_ID, COMPONENT_ID, COMPONENT_GRP_C, COMPONENT_RESULT |  |
| RES_DB_MAIN | The RES_DB_MAIN is the primary table for storing results data. | RESULT_ID, RES_TYPE_ID, LAB_ID, RES_VAL_STATUS_C, RES_TEST_ID, RES_SPECIMEN_ID, RES_SPEC_NO_REL, RES_EPT_PAT_ID |  |
| RES_VAL_DATA_RM | Stores data for multi-line value item. For a given line data may be spread across multiple lines. | RESULT_ID, GROUP_LINE, VALUE_LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, MULT_LN_VAL_STORAGE, MULT_LN_VAL_STG_RAW |  |
| RES_VAL_PTR_RM | For a given component this holds all the pointers to the table that stores the multi line data. | RESULT_ID, GROUP_LINE, VALUE_LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CMP_MULTILINE_VALUE |  |
| RES_VLD_AUDIT | Result audit information for verification and unverification (result correction). | RESULT_ID, RES_TYPE_ID, LINE, LAB_ID, RES_SPECIMEN_ID, RES_VLD_STATUS_C, RES_UNVLD_RSN_C, RES_VLD_USER |  |
| RIS_INT_STUDY_CMT | This table contains the comments when an imaging physician determines a study as interesting. | ORDER_PROC_ID, LINE, INT_STUDY_COMMENT, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| RSLT_ORDERS | This table contains information about orders associated with result records. | RESULT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, SOURCE_ORDER_ID |  |
| RTYPE_DB_MAIN | The RTYPE_DB_MAIN table contains information for result type records. | RESULT_TYPE_ID, TYPE_OF_DATA_C, RTM_DFLT_MNEM_PR_ID, RESULT_TYPE_NAME, TYPE_OF_RES_TYP_C, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, PREVENT_TAB_RR_YN |  |
| RXNORM_CODES | This table contains the RxNorm code for the medications. | MEDICATION_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RXNORM_CODE_LEVEL_C, RXNORM_CODE, RXNORM_PRIMARY_YN, RXNORM_TERM_TYPE_C |  |
| RX_MED_EQUIV_INFO | This table contains medications' equivalency information. | MEDICATION_ID, LINE, EQUIV_QTY, EQUIV_UNIT_C, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| RX_MED_NDC_CODE | This table contains medications' NDC codes. | MEDICATION_ID, LINE, NDC_CODE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| RX_MED_TWO | This table contains medications' information. | MEDICATION_ID, MEDICATION_NAME, RECORD_STATE_NAME, TEMP_NAME_EDIT, PROPTRY_STATUS_C, BRAND_NAME_CODE_C, NAME_SOURCE_C, CHK_INGRED_NAME | **Primary table** in this group (103 cols). Overflow siblings joined on shared key: RX_MED_FOUR (41 cols), RX_MED_ONE (1 |
| RX_NDC | This table contains the National Drug Code (NDC) information. | NDC_ID, NDC_CODE, NDC_FORMAT, RAW_11_DIGIT_NDC, RAW_NDC_CODE, MFG_LONG_NAME, MFG_ABBR_NAME, MFG_CODE | **Primary table** in this group (101 cols). Overflow siblings joined on shared key: RX_NDC_2 (6 cols). Prefer this table |
| RX_NDC_STATUS | This table contains the medication related to NDC for each contact. | NDC_ID, CONTACT_DATE_REAL, CONTACT_DATE, LINE, CNCT_STAT_NAME, CNCT_STAT_CHG_TIME, MEDICATION_ID, CNCT_SERIAL_NUM |  |
| SDD_DATA | This table stores defining information about a patient's SDOH data. Each row in this table represents documentation for a single S | SDOH_DATA_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RECORD_STATUS_C, DOMAIN_C, PAT_ID, CONCERNS_PRESENT_YN, RECORD_CREATE_UTC_DTTM |  |
| SDD_ENTRIES | This table stores basic info about Social Driver entries. Each row represents one documentation of a need or risk for the patient  | SDOH_DATA_ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, ENTRY_DOM_CONFIG_ID, ENTRY_EFFECTIVE_UTC_DTTM, ENTRY_INTERPRETATION, ENTRY_CONCERN_LVL_C |  |
| SMARTFORM_CONCEPT | This table contains information about SmartData elements that are data bound on SmartForms. | FORM_ID, CONTACT_DATE_REAL, LINE, CONTACT_DATE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CM_CT_OWNER_ID, CONCEPT_ID |  |
| SMRTDTA_ELEM_DATA | The SMRTDTA_ELEM_DATA table stores metadata (context, linked records, time of entry, etc.) concerning SmartData element values ent | HLV_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ELEMENT_ID, CUR_VALUE_DATETIME, CUR_VALUE_USER_ID, CUR_VALUE_SOURCE, CONTEXT_NAME |  |
| SMRTDTA_ELEM_ENCOUNTER | This table is a bridge between encounter context SmartData element values and the source patient encounter contacts. | HLV_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, PAT_ENC_CSN_ID, PAT_ID, ELEMENT_ID |  |
| SMRTDTA_ELEM_HISTORY | This table is a bridge between history context SmartData element values and the source patient history contacts. | HLV_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, PAT_ENC_CSN_ID, PAT_ID, ELEMENT_ID |  |
| SMRTDTA_ELEM_NOTE | This table is a bridge between note context SmartData element values and the source note records. | HLV_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, NOTE_ID, ELEMENT_ID |  |
| SMRTDTA_ELEM_VALUE | The SMRTDTA_ELEM_VALUE table stores SmartData element values entered by users through SmartForms, SmartTools and other documentati | HLV_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, SMRTDTA_ELEM_VALUE, ELEM_NW_ID_VAL_NUM |  |
| SOCIAL_HX | The SOCIAL_HX table contains social history data for each history encounter stored in your system. This table has one row per hist | PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, END_HIST_DATE_REAL, IS_TOBACCO_USER, TOBACCO_PAK_PER_DY, TOBACCO_USED_YEARS, TOBACCO_COMMENT |  |
| SOCIAL_HX_ALC_USE | The SOCIAL_HX_ALC_USE  table contains social alcohol history data entered in clinical system patient encounters. Note: Typically,  | PAT_ENC_CSN_ID, LINE, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, ALCOHOL_DRINKS_WK, HX_DRINK_TYPES_C |  |
| SPEC_AP_RESULT | This table contains information related to results entered on a specimen's anatomic pathology result. | SPECIMEN_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, AP_RES_TYPE_C, AP_RES_NOTE_ID, AP_RES_STATUS_C, NOTIF_SENT_UTC_DTTM |  |
| SPEC_DB_MAIN | The SPEC_DB_MAIN table contains basic information about your specimen records. These include clinical pathology, anatomic patholog | SPECIMEN_ID, LAB_ID, SPEC_NUMBER_LN1, SPEC_DTM_COLLECTED, SPEC_DTM_RECEIVED, SPEC_CONTAINER_ID, SPEC_SOURCE_C, SPEC_COLL_SITE_C |  |
| SPEC_TASK_LIST | This table contains task information for Microbiology specimens and Anatomic Pathology cases. | SPECIMEN_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, TASK_TEST_ID, TASK_C, TASK_ACTION_C, TASK_PARAMS |  |
| SPEC_TASK_LIST_SUB | This is sub container information for Anatomic Pathology specimens. | SPECIMEN_ID, GROUP_LINE, VALUE_LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, TASK_LINKED_SCTR_ID |  |
| SPEC_TEST_REL | The SPEC_TEST_REL table contains information stored on each specimen record that relates to the tests performed on the specimen. E | SPECIMEN_ID, LINE, LAB_ID, SPEC_NUMBER_RLTD, SPEC_TST_ID, SPEC_TEST_PRI_C, SPEC_TST_LAB_ID, SPEC_TST_ORDER_ID |  |
| SPHR_PLAIN_TEXT | The SPHR_PLAIN_TEXT table contains information about SmartPhrase text in plain text format from the SmartPhrase master file (HH1). | SMARTPHRASE_ID, LINE, CONTACT_DATE, CM_CT_OWNER_ID, PLAIN_TEXT, CONTACT_DATE_REAL, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| STAND_HOV_INST_ORD | The records in this table contain child order IDs of standing orders released in an HOV encounter. | ORDER_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, STAND_INS_IP_ORD_ID |  |
| SURGICAL_HX | The SURGICAL_HX table contains data from medical history contacts entered in clinical system patient encounters. Since one patient | PAT_ID, PAT_ENC_DATE_REAL, END_HIST_DATE_REAL, LINE, PROC_ID, PROC_CODE, SURGICAL_HX_DATE, COMMENTS |  |
| TC_REQUEST_STATUS_HX | This table stores information related to the status change history for Transfer Center requests. | COMM_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, REQUEST_STATUS_C, STATUS_UPDATE_UTC_DTTM, STATUS_UPDATE_USER_ID, DEST_DECLINE_RSN_C |  |
| TEST_EXPIRATION | Test expiration times. | TEST_ID, LINE, EFFECTIVE_DATE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CM_CT_OWNER_ID, EXP_TIME, EXP_TIME_UNIT_C |  |
| TEST_MSTR_DB_MAIN | The TEST_MSTR_DB_MAIN table stores general settings for laboratory test records. | TEST_ID, TEST_NAME, TEST_ABBR, TEST_STATUS_C, TEST_SUSC_YN, TEST_NOADD_RTYPE_ID, TEST_NOADD_GW_RTYP, TEST_NOADD_OW_RTYP |  |
| TPL_CYCLES | The cycle information for the treatment plan. | TREATMENT_PLAN_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CYCLE_ID, CYCLE_NAME, CYCLE_STATUS_C, CYCLE_START_DATE |  |
| TPL_INFO | This table contains basic information about a treatment plan or a pathway, such as the plan/pathway name, the user who created the | TREATMENT_PLAN_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, TREATMENT_PLAN_NAME, PLAN_STATUS_C, PLAN_REC_TYP_C, PLAN_START_DATE, ZERO_BASED_YN |  |
| TPL_TXDAYS | This table contains the treatment days in a treatment plan record or the steps in a pathway record. | TREATMENT_PLAN_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, TREATMENT_DAY_ID, TREATMENT_DAY_SRC, TX_DAY_TYPE_C, TREATMENT_DAY_DAT |  |
| TPL_UPDATE_INFO | The update information for the treatment plan. | TREATMENT_PLAN_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, UPDATED_BY_USER_ID, UPDATED_ON_TM, UPDATED_IN_PAT_ENC_CSN_ID |  |
| TRANSPLANT_CLASS | This table contains transplant classifications (types of organs being transplanted). | SUMMARY_BLOCK_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, TX_CLASS_C, TX_ACTIVE_COORD_ID |  |
| TRANSPLANT_INFO | This table contains information regarding the transplant episode. Only episodes whose Episode Type Class (I HBD 130) is 4 - Transp | SUMMARY_BLOCK_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, TX_REV_DT, TX_EPSD_TYPE_C, TX_NUM, TX_HIST_LOCATION, TX_SURG_DT |  |
| TREATMENT_TEAM | This table stores information about patient treatment teams such as relationship, specialty, department, and start/end time. Each  | PAT_ENC_CSN_ID, LINE, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, TR_TEAM_BILL_PR_ID, TR_TEAM_EM_CODE_ID |  |
| TRG_BLOCK_INFO | This table contains information about certain types of planned orders, including orders from treatment days in treatment plans and | REGIMEN_ID, CONTACT_DATE_REAL, LINE, CONTACT_DT, CM_CT_OWNER_ID, BLOCK_ID, BLOCK_DAT, BLOCK_INI |  |
| TRG_DEL_BLOCK_INFO | The information about the deleted order blocks (patient order templates) in the treatment day. | REGIMEN_ID, CONTACT_DATE_REAL, LINE, CONTACT_DT, DELETED_BLOCK_ID, DELETED_BLOCK_CAT_C, DEL_BLK_SRC_DAY_UID, DEL_ORD_SRC_AOG_ID |  |
| TRG_INFO | This table stores treatment day or pathway step information that is contact-independent, such as the treatment day/pathway step st | REGIMEN_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, REGIMEN_NAME, DEFER_DAY_RSN_C, CANCEL_DAY_RSN_C, STATUS_COMMENTS, TRG_TPL_ID |  |
| TRTTEAM_AUDIT | Extract for treatment team audit trail items. | PAT_ENC_CSN_ID, LINE, PAT_ID, PAT_ENC_DATE_REAL, CONTACT_DATE, CM_CT_OWNER_ID, TT_USER_ID, TT_EDIT_INSTANT |  |
| TXP_CURRENT_MELD_PELD_HX | This table contains the liver score history for a transplant episode. After 6/28/2022 exceptions will not be included due to chang | SUMMARY_BLOCK_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CURRENT_SCORE, CURRENT_STATUS_C, CURRENT_SCORE_TYPE, CURRENT_EXCEPTION_C |  |
| TX_DIAG | This table contains information about the diagnoses associated with transactions. Since one transaction may be associated with mul | TX_ID, LINE, POST_DATE, SERV_AREA_ID, DX_ID, ICD9_CODE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| UAL_ACTIVITY_HOURS | This table stores user action log data about how activities were used within workspace actions summarized by hour of the day. Each | UAL_ACTIVITY_HOUR_KEY, USER_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, WORKSTATION_ID, ACTIVITY_HOUR_DTTM, ACTIVITY_HOUR_UTC_DTTM, WORKSPACE_KIND |  |
| UAL_LOGIN_EVENTS | This table stores user action log data about login events. Each row represents a login event. | UAL_LOGIN_EVENT_KEY, USER_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, WORKSTATION_ID, LOGIN_ACTION_DTTM, LOGIN_ACTION_UTC_DTTM, LOGIN_TYPE_C |  |
| UTILIZATION | This table contains information for utilization data. | UTILIZATION_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, UTILIZATION_TYPE_C, UTILIZATION_DATE, UTILIZATION_GROUP_ID, LOCATION_ID, BLOCK_ID |  |
| VALID_PATIENT | The VALID_PATIENT table contains one row for each patient in your system and indicates whether the patient is considered valid for | PAT_ID, IS_VALID_PAT_YN, CM_LOG_OWNER_ID, CM_PHY_OWNER_ID |  |
| VARIANT | Main variant result table. | VARIANT_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RECORD_STATUS_C, VARIANT_TYPE_C, VARIANT_NAME, HGVS_NAME, PAT_ID |  |
| VARIANT_SYSTEM | The VARIANT_SYSTEM table contains the external variant identifier and the system that defined it and its version. | VARIANT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, VARIANT_SYSTEM_C, VARIANT_SYSTEM_VER, VARIANT_CODE |  |
| VAR_ALLELE_NAME | The VAR_ALLELE_NAME table contains information about the alleles the variant belongs to. | VARIANT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, ALLELE_NAME |  |
| VAR_CONTAINED | The VAR_CONTAINED table contains the list of simple or complex variants contained within a complex variant. | VARIANT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CONTD_VARIANT_ID |  |
| VAR_INTERPRETATION | The VAR_INTERPRETATION table contains the interpretation text for the variant. | VARIANT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, INTERPRETATION |  |
| VAR_PHENOTYPES | The VAR_PHENOTYPES table contains the external phenotype identifier and the system that defined it. | VARIANT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, PHENOTYPE_SYSTEM_C, PHENOTYPE_CODE, PHENOTYPE_NAME, MODE_OF_INHERITANCE_C |  |
| VAR_PHENOTYPE_DESC | The VAR_PHENOTYPE_DESC table contains the phenotype description for the variant. | VARIANT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, PHENOTYPE_DESC |  |
| VAR_REPEAT_EXPANSION | This table stores information about repeat expansion variants, including the repeated nucleotides and the number of times the nucl | VARIANT_ID, LINE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, REPEAT_NUCLEOTIDES, REPEAT_NUMBER, REPEAT_NUMBER_LEADING, REPEAT_NUMBER_TRAILING |  |
| VERIFICATION | The VERIFICATION table contains information about your verification records. These records include verification information for pa | RECORD_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RECORD_NAME, RECORD_STATUS_C, VERIF_RECORD_INI, VERIF_RECORD_IDNT, VERIFICATION_TYPE_C |  |
| VESSEL_DOC | Table contains items that represents anatomy of body (vessel related items). | RECORD_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, RECORD_NAME, RECORD_STATUS_C, ANATOMY_TYPE_C, ANATOMY_EXT_NAME, ANATOMY_ABBREV |  |
| V_CANCER_STAGING | This view stores contact-specific information for a patient's cancer stage records. Each row in this table corresponds to a single | STAGE_ID, CONTACT_DATE_REAL, CONTACT_DATE, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID, CM_CT_OWNER_ID, CONTACT_NUM, MOST_RECENT_CONTACT_YN |  |
| V_CASE_SCHEDULE_CHANGE | The view is designed to simplify reporting on canceled and rescheduled cases. The view contains information about the times when a | CASE_ID, LOG_ID, ACTION_C, ACTION_NM, GENERAL_ACTION_NM, ACTION_DTTM, AUDIT_USER_ID, AUDIT_USER_NM |  |
| V_CUBE_D_DEP_LOC | This view contains data from the CLARITY_DEP and CLARITY_POS table, optimized for use in SSAS Cubes. This data contains basic info | DEPARTMENT_ID, DEPARTMENT_NAME, DEPARTMENT_DISPLAY_NAME, DEPARTMENT_SPECIALTY, LOCATION_ID, LOCATION_NAME, LOCATION_DISPLAY_NAME, LOCATION_TYPE |  |
| V_CUBE_D_PROVIDER | This view contains data from the CLARITY_SER table, optimized for use in SSAS Cubes. | PROVIDER_ID, PROVIDER_NAME, PROVIDER_DISPLAY_NAME, PROVIDER_TYPE, STAFF_RESOURCE, PRIMARY_SPECIALTY, IS_RESIDENT_YN, CLINICIAN_TITLE |  |
| V_EHI_DXR_LINKED_PATS | Placeholder view for DXR EHI data that needs to be marked as both static and dynamic. | DOCUMENT_ID, PAT_ID, CM_PHY_OWNER_ID, CM_LOG_OWNER_ID |  |
| V_IMG_STUDY | This view is designed to simplify reporting on orders performed in the imaging applications. It combines information for orders sc | ORDER_ID, PAT_ID, PAT_MRN_ID, PAT_NAME, PAT_NM_WMRN, PAT_SEX_C, PAT_AGE_AT_EXAM, ACCESSION_NUM |  |
| V_LOG_BASED | This view brings together fields needed from logs and cases that are used to report on KPI metrics. | LOG_ID, CASE_ID, PAT_ID, PAT_AGE, PATIENT_CLASS_C, PATIENT_CLASS_NM, PATIENT_CLASS_GROUP, CASE_CLASS_C |  |
| V_LOG_TIMING_EVENTS | The V_LOG_TIMING_EVENTS view contains information about case timing events associated with a procedural case. | LOG_ID, CASE_ID, SCHED_SETUP_START_DTTM, SCHED_IN_ROOM_DTTM, SCHED_OUT_ROOM_DTTM, SCHED_CLEANUP_COMP_DTTM, PATIENT_IN_FACILITY_DTTM, PATIENT_IN_PREPROCEDURE_DTTM |  |
| V_NOTE_VIEW_INFO | The replacement tables are V_NOTE_SHARE_W_PAT_INFO, HNO_INFO, ZC_NOTE_TYPE, ZC_NOTE_TYPE_IP, and MYC_PAT_NOTE_VIEW. The replacemen | NOTE_ID, PAT_ID, PAT_ENC_CSN_ID, ENC_START_DTTM, ENC_PROV_ID, ENC_DEPARTMENT_ID, ENC_REV_LOC_ID, ENC_SERV_AREA_ID |  |
| V_OB_DEL_RECORDS | This view is used to display information relevant to a baby's delivery record on one row. Note that babies that are unlinked from  | BABY_ID, MOM_ID, DELREC_ID, DELMETH_C, GA, PROV_NAME, DEL_DTTM, LIVING_C |  |
| V_ONC_TREATMENT_PLAN_ORDERS | A dimensional view which combines the various pieces of the treatment plan structure (plan, cycle, day, and order). It includes li | TREATMENT_PLAN_ID, PLAN_RECORD_TYPE_C, PLAN_STATUS_C, PLAN_STATUS_NAME, PLAN_VERSION, PLAN_CREATED_DATETIME, PLAN_CREATOR_USER_ID, PLAN_START_DATE |  |
| V_PAT_ADT_LOCATION_HX | A dimensional view used to find a patient's department, room and/or bed at a given datetime.  The view contains one row for each a | EVENT_ID, PAT_ENC_CSN, EVENT_TYPE_C, IN_DTTM, OUT_DTTM, ADT_DEPARTMENT_ID, ADT_DEPARTMENT_NAME, ADT_DEPARTMENT_NM_WID |  |
| V_PAT_DIALYSIS_HISTORY | Stores all dialysis history information. Each row represents a single dialysis entry, including a start/end date and details about | PAT_ID, DIALYSIS_CENTER_ID, DIALYSIS_DEPARTMENT_ID, DIALYSIS_TYPE_C, DIALYSIS_START_DATE, DIALYSIS_END_DATE, DIALYSIS_COMMENTS, EPISODE_ID |  |
| V_PAT_HX_TOB_USE | This view calculates the current pack years for a patient based on current tobacco use information documented. | PAT_ID, TOB_PACK_YEARS, TOB_CURRENT_PPD, TOB_START_DATE, TOB_QUIT_DATE |  |
| V_RTE_VISIT_COVERAGES | This view is used by a datalink query that populates Eligibility Metrics based on visit coverages. | PAT_ENC_CSN_ID, PAT_ID, CONTACT_DATE, COVERAGE_ID, PAYOR_ID, BENEFIT_PLAN_ID, FINANCIAL_CLASS_C, DEPARTMENT_ID |  |
| V_SCHED_APPT | This view provides information about appointments, with one row per appointment. It is based on the F_SCHED_APPT appointment fact  | PAT_ENC_CSN_ID, CONTACT_DATE, PAT_ID, APPT_STATUS_C, APPT_STATUS_NAME, DEPARTMENT_ID, DEPARTMENT_NAME, DEPT_SPECIALTY_C |  |
| WUSM_PATIENT_ADDRESS_GEOCODED |  |  |  |
| X_V_CLARITY_UCL |  |  |  |
| X_V_OF_HSP_ACCOUNT |  |  |  |
| ZC_ABNORMAL_TYPE |  | ABNORMAL_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ACCESS_ACTION |  | ACCESS_ACTION_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ACCOMMODATION | This table extracts the information stored in ROM 100: Accommodation Code | ACCOMMODATION_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ACCOM_REASON |  | ACCOM_REASON_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ACCOUNT_TYPE | This table contains the category definitions for guarantor account type (e.g. Personal/Family, etc.) | ACCOUNT_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ACCT_BASECLS_HA | This table contains the category information for account base classes. | ACCT_BASECLS_HA_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ACCT_BILLSTS_HA |  | ACCT_BILLSTS_HA_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ACCT_CLASS_HA | This table contains the category information for account classes. | ACCT_CLASS_HA_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ACTION_TYPE_2 | Contains actions that may be performed on order events. | ACTION_TYPE_2_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ACTIVE_ORDER |  | ACTIVE_ORDER_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ACTIVE_STATUS_2 | This table contains the category information for the provider (SER) record status. This table is different from ZC_ACTIVE_STATUS b | ACTIVE_STATUS_2_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ACUITY_LEVEL |  | ACUITY_LEVEL_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ADDL_ADDR_DETAILS | Stores additional address categories. | ADDRESS_DETAILS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ADJUSTMENT_CAT | This table contains the category information for adjustment categories. | ADJUSTMENT_CAT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ADMIN_ROUTE |  | MED_ROUTE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ADM_SOURCE |  | ADMIT_SOURCE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ADT_UNIT_TYPE |  | ADT_UNIT_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ALCOHOL_BINGE | This table contains the category IDs and Names for the SDOH_ALCOHOL_BNG_C column | ALCOHOL_BINGE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ALCOHOL_DRINKS_PER_DAY | This table contains category IDs and values for the ALCOHOL_DRINKS_PER_DAY_C column. | ALCOHOL_DRINKS_PER_DAY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ALCOHOL_FREQ | This table contains the category IDs and names for the SDOH_ALCOHOL_FREQ_C column. | ALCOHOL_FREQ_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ALCOHOL_USE | This is the table for I EPT 19220 category. | ALCOHOL_USE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ALLELIC_BASIS |  | ALLELIC_BASIS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ALLELIC_PHASE |  | ALLELIC_PHASE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ALLELIC_STATE |  | ALLELIC_STATE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ALLERGEN_TYPE |  | ALLERGEN_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ALLERGY_CERTAINTY | This table defines category values for the Certainty of Risk field in allergy documentation. | ALLERGY_CERTAINTY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ALLERGY_SEVERIT | This table contains the category information for allergy severity. | ALLERGY_SEVERITY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ALRGY_DLET_RSN | This table stores category values for the reason an allergy was deleted. | ALRGY_DLET_RSN_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ALRGY_STATUS |  | ALRGY_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ALRTS_OVR_RSN |  | ALRTS_OVR_RSN_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ALT_STATUS | This table holds the alert status categories.  The alert status is a description of what happened to an interaction alert when it  | ALT_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ANATOMICAL_RESECTION |  | ANATOMICAL_RESECTION_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ANTIBIOTIC |  | ANTIBIOTIC_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_APPLICATION | This table contains the category information contained in E0B 10015. | APPLICATION_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_APPROVAL_APP |  | APPROVAL_APP_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_APPT_CONF_STAT |  | APPT_CONF_STAT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_APPT_STATUS |  | APPT_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_AP_CASE_HOLD | This table contains the category information for anatomic pathology case hold types. | AP_CASE_HOLD_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_AP_CASE_STATUS | This table contains the category information for anatomic pathology case statuses. | AP_CASE_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_AP_RES_STATUS |  | AP_RES_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_AP_RES_TYPE |  | AP_RES_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_AP_SPEC_ATTR | This table contains the category information for anatomic pathology specimen attributes. | AP_SPEC_ATTR_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_AP_WORKLIST_TYP | This table contains the category information for anatomic pathology worklist types. | AP_WORKLIST_TYP_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ARRIV_MEANS |  | MEANS_OF_ARRV_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ASGND_INTERP_TY | This table indicates the kind of interpreter serving an appointment. | ASGND_INTERP_TY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ASSESSMENT_2 |  | ASSESSMENT_2_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_AUDIT_PLATFORM |  | AUDIT_PLATFORM_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_AVATAR_ORIENT |  | AVATAR_ORIENT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_BACKGROUND_AVATAR |  | BACKGROUND_AVATAR_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_BH_CORD_COMP |  | BH_CORD_COMP_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_BH_PRESENTATION |  | BH_PRESENTATION_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_BH_RESUSCIT |  | BH_RESUSCITATIO_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_BIOTYPE | The ZC_BIOTYPE table stores category information for organism biotypes. | BIOTYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_CALCULATED_ENC_STAT |  | CALCULATED_ENC_STAT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_CANCEL_DAY_RSN | The category table for the reason why a treatment day was canceled. | CANCEL_DAY_RSN_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_CANCEL_REASON | This table contains category values for EPT 7300, indicating the cancel reason for the appointment. | CANCEL_REASON_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_CAREPLAN_TYPE | Care plan type category list.  Used by Home Health table HH_LCP_NOADD_SINGL. | CAREPLAN_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_CASE_FLAGS | This table contains the category information for the flags that can be attached to an anatomic pathology case. | CASE_FLAGS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_CENTER | This table contains centers, used as groupers for departments and chart stations. | CENTER_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_CHANGE_TYPE | This table stores information about the category values corresponding to the types of changes that can be made to the patient's ca | CHANGE_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_CHAT_MESSAGE_TYPE |  | CHAT_MESSAGE_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_CHROMOSOME |  | CHROMOSOME_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_CHURCH_ATTENDANCE | This table contains category IDs and values for the CHURCH_ATTENDANCE_C column. | SDOH_CHURCH_ATTENDANCE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_CLASS_OF_PROBLE |  | CLASS_OF_PROBLEM_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_CLIENT_APP_TARGET |  | CLIENT_APP_TARGET_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_CLINICAL_SIGNIF |  | CLINICAL_SIGNIF_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_CLINICAL_SVC |  | CLINICAL_SVC_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_CLUBMTG_ATTENDANCE | This table contains category IDs and values for the CLUBMTG_ATTENDANCE_C column. | CLUBMTG_ATTENDANCE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_CLUB_MEMBER | This table contains category IDs and values for the CLUB_MEMBER_C column. | CLUB_MEMBER_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_CODE_STATUS |  | CD_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_CODE_TYPE |  | CODE_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_COMM_AUTH | Category table for Care Everywhere - Communications Authorized (I DCS 72013) | COMM_AUTH_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_COMM_ORIG_TYP |  | COMM_ORIG_TYP_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_COMPONENT_GRP | This table contains the category information for the groups of result components. | COMPONENT_GRP_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_COMP_REPORTED | This table contains the category information for whether a component is reported or not. | COMP_REPORTED_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_CONF_STAT |  | ADMIT_CONF_STAT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_CONTRAST_REQ | Category table for Contrast Requirement, an item to document whether an exam will be done without contrast, with contrast, or with | CONTRAST_REQ_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_COUNTRY |  | COUNTRY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_COUNTY |  | COUNTY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_CS_SURG_CASE_CLASS | Category table for item EPT-24137, which is the case class.  The categories in this table determine if the case was performed in a | CS_SURG_CASE_CLASS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_CVG_REG_STATUS |  | CVG_REG_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_CYCLE_STATUS | The status of a cycle in a treatment plan. | CYCLE_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DAILY_STRESS | This table contains category IDs and values for the DAILY_STRESS_C column. | DAILY_STRESS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DATA_INDEXED | This table indicates whether event data should be indexed or not. | DATA_INDEXED_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DAY_TYPE | The category table for the type of treatment day (inpatient/outpatient). | DAY_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DBC_SUBSPECIALTY | This table contains the category information for DBC subspecialties. | DBC_SUBSPECIALTY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DC_REASON | The reason for discontinuing a treatment plan. | DC_REASON_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DEFERRED_GEN_STATUS |  | DEFERRED_GEN_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DEFER_DAY_RSN | The category table for the reason why a treatment day was deferred. | DEFER_DAY_RSN_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DEFER_REASON | This table holds the title and abbreviation information of the category list stored in LPL 4086. | DEFER_REASON_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DELETED_CAT | This table indicates whether the category is deleted, hidden or both. | DELETED_CAT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DELIVERY_TYPE |  | DELIVERY_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DEL_PROC | This table contains the category information for the delivery procedures. | DEL_PROC_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DEL_STATUS | The category table for the deletion status of a record. | DEL_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DEP_MSG_TYPE | The department message type category information. | DEP_MSG_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DEP_RPT_GRP_6 |  | RPT_GRP_SIX, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DEP_STS_NAME |  | DEP_STS_NAME_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DETAIL_TYPE |  | DETAIL_TYPE, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DISCH_DEST |  | DISCH_DEST_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DISCH_DISP |  | DISCH_DISP_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DISPENSE_CODE |  | DFLT_DISP_CODE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DISPENSE_REASON |  | DISPENSE_REASON_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DISPENSE_ROUTE |  | DISPENSE_ROUTE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DISP_ENC_TYPE |  | DISP_ENC_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DISP_TYPE |  | DISP_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DISP_VAL | This table contains the category list stored in RFL item 18150. | DISP_VAL_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DNA_VAR_TYPE |  | DNA_VAR_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DOCUMENT_IDENT_SOURCE |  | DOCUMENT_IDENT_SOURCE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DOCUMENT_LOC |  | DOCUMENT_LOC_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DOCUMENT_ORIGIN |  | DOCUMENT_ORIGIN_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DOCUMENT_SOURCE_INFO | Document source info category table. | DOC_SOURCE_INFO_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DOCUMENT_TYPE | Care Everywhere Document Type | DOCUMENT_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DOCUMENT_USAGE |  | DOCUMENT_USAGE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DOC_CONTENT_TYPE | Table for Document Content Type category. | DOC_CONTENT_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DOC_DEL_RSN |  | DOC_DEL_RSN_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DOC_GRP |  | DOC_GRP_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DOC_INFO_TYPE |  | DOC_INFO_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DOC_KIND |  | DOC_KIND_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DOC_LOCATION | This table contains all the category entries for the location of the document. | DOC_LOCATION_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DOC_METHOD |  | DOC_METHOD_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DOC_PND_APRV_STAT |  | DOC_PND_APRV_STAT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DOC_REC_STATE | This table holds category values to determine if the record is Inactive or Deleted. | DOC_REC_STATE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DOC_REJ_RSN |  | DOC_REJ_RSN_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DOC_REP_CONTEXT |  | DOC_REP_CONTEXT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DOC_SPECIALTY |  | DOC_SPECIALTY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DOC_STAT |  | DOC_STAT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DOC_STORAGE_LVL | This table contains the possible category values for the document storage level. | DOC_STORAGE_LVL_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DRG_QUESN_TYP |  | DRG_QUESN_TYP_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DT_ACTION_OUTCOME |  | DT_ACTION_OUTCOME_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DT_ACTION_TYPE |  | DT_ACTION_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DX_CODE_TYPE |  | DX_CODE_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_DX_POA | Category table for HAR 611 (also used by HAR 1851).  Contains present on admission (POA) category values.  This category table is  | DX_POA_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_EAP_CONT_TYPE |  | CONTACT_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_EAP_RPT_GRP_7 |  | RPT_GRP_SEVEN, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_EDG_CODE_SET | This table contains the category list stored in EDG item 95 - Code Set. | EDG_CODE_SET_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_EDIT_MAR_RSLT | *** Deprecated *** The deprecated table's content/data is no longer populated in Chronicles and is no longer available. | RESULT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_EDUCATION_LEVEL | This table contains the category information for the highest level of education achieved. | EDUCATION_LEVEL_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_EDU_LEVEL | This table contains the category IDs and names for the SDOH_EDUCATION_C column. | EDU_LEVEL_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ED_DISPOSITION |  | ED_DISPOSITION_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_EMPY_STAT | This table will be deprecated in a future release. You should use ZC_EMPY_STATUS when reporting on this category list. | EMPY_STAT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_EMPY_STATUS | This table contains information about the employment status category. | EMPY_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_EMP_CAT_RPT_GRP_ONE |  | EMP_CAT_RPT_GRP_ONE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ENGLISH_FLUENCY | This table displays basic information for the English Fluency item. | ENGLISH_FLUENCY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ENROLL_STATUS |  | ENROLL_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ENTRY_SOURCE |  | ENTRY_SOURCE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_EOW_READ_STATUS |  | EOW_READ_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_EPI_STATUS |  | EPI_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_EPM_RPT_GRP_10 |  | RPT_GRP_TEN, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_EPM_RPT_GRP_6 |  | RPT_GRP_SIX, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_EPM_RPT_GRP_7 |  | RPT_GRP_SEVEN, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_EPM_RPT_GRP_8 |  | RPT_GRP_EIGHT, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_EPM_RPT_GRP_9 |  | RPT_GRP_NINE, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_EPRES_ERROR | Error that occurred during the processing of this incoming document(for example patient not found,medication not found or duplicat | EPRES_ERROR_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ERX_SIG_TYPE |  | ERX_SIG_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ETHNIC_BKGRND | This table stores the category information for the Ethnic Background item EPT 134. | ETHNIC_BKGRND_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ETHNIC_GROUP | This table contains the category information for patient ethnic groups. | ETHNIC_GROUP_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_EVENT_REASON | This table extracts the information stored in ADT 210: Reason. | REASON_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_EVENT_SUBTYPE |  | EVENT_SUBTYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_EVENT_TYPE |  | EVENT_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_EXTERNAL_ADMIN | This table holds the title and abbreviation information of the category list stored in LPL 4082. | EXTERNAL_ADMIN_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_EXT_DEATH_SOURCE |  | EXT_DEATH_SOURCE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_EXT_DEATH_STAT |  | EXT_DEATH_STAT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_EXT_MED_CONTEXT |  | EXT_MED_CONTEXT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_FINANCIAL_CLASS | This table holds the financial class category list. Examples of standard category values in this list are Commercial and Self-Pay. | FINANCIAL_CLASS, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_FIN_RESOURCE_RISK | This table contains the category IDs and names for the social drivers of health financial resource strain risk column. | FIN_RESOURCE_RISK_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_FIN_RESOURCE_STRAIN | This table contains the category IDs and names for the SDOH_FRS_C column. | FIN_RESOURCE_STRAIN_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_FLO_DOC_SRC |  | DOCUMENTATION_SOURCE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_FLUID_ODOR | This table contains the category information for fluid odor. | FLUID_ODOR_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_FOOD_INSECURITY_SCARCE |  | FOOD_INSECURITY_SCARCE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_FOOD_INSECURITY_WORRY | This table contains the category numbers and names for the food insecurity worry column. | FOOD_INSECURITY_WORRY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_FORM |  | FORM_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_GENDER_IDENTITY |  | GENDER_IDENTITY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_GENE |  | GENE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_GENE_SYSTEM |  | GENE_SYSTEM_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_GENOME_ASSEMBLY |  | GENOME_ASSEMBLY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_GENOMICS_PROC_CLASS | The type of genomics procedure. This classification is used downstream in genomics features to determine how it should be displaye | GENOMICS_PROC_CLASS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_GENOMIC_SOURCE |  | GENOMIC_SOURCE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_GEN_SEQ_SYSTEM |  | GEN_SEQ_SYSTEM_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_GIVEN_EXTER_RSN | This is the category table of reasons for marking a treatment day as given externally. Item TRG - 315 | GIVEN_EXTER_RSN_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_GUAR_REL_TO_PAT |  | GUAR_REL_TO_PAT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_HCD_CODE_SET |  | CODE_SET_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_HISTORY_SOURCE | The ZC_HISTORY_SOURCE table contains the category values for the patient medical history's source. | HISTORY_SOURCE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_HOME_CARE_TYPE | The episode class category list. | HOME_CARE_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_HOSP_ADMSN_TYPE |  | HOSP_ADMSN_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_HOW_ADDED |  | HOW_ADDED_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_HOW_ISO_ADDED |  | HOW_ISO_ADDED_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_HX_DRINK_TYPES | ZC_HX_DRINK_TYPES stores the category values for drink types related to a patient's social alcohol history. | HX_DRINK_TYPES_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_HX_QUESR_CONTEX |  | HX_QUESR_CONTEX_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ILL_DRUG_USER |  | ILL_DRUG_USER_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_IMAGE_LOCATION |  | IMAGE_LOCATION_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_IMG_SLCT_TYPE |  | IMG_SLCT_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_IMMNZTN_STATUS |  | IMMNZTN_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_INCL_VIEWERS |  | INCL_VIEWERS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_INC_CONTEXT | This table contains the category information for context types. | INC_CONTEXT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_INDUSTRY | This table contains the category information for the industry in which the patient works. | INDUSTRY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_INFECTION |  | INFECTION_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_INF_STATUS |  | INF_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_INGRED_TYPE |  | DISP_CTYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_INTAKE_TYPE_P | This table contains the category information for the types of intake in doc flowsheets. | INTAKE_TYPE_P_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_INTERFACE_STAT |  | INTERFACE_STAT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_INTERPRETER_VEN | This table contains category value which identifies the vendor or other party that is providing an external or phone interpreter f | INTERPRETER_VEN_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_INTF_REF_MEDLOOP |  | INTF_REF_MEDLOOP_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_INTRP_ASSIGNMEN | This table indicates the interpreter assignment status. | INTRP_ASSIGNMEN_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_INVLD_REASON |  | INVLD_REASON_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_IPV_EMOTIONAL_ABUSE | This table contains the category IDs and Names for the social drivers of health intimate partner violence columns (IPV_EMOTIONAL_A | IPV_EMOTIONAL_ABUSE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_IPV_FEAR |  | IPV_FEAR_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_IPV_PHYSICAL_ABUSE |  | IPV_PHYSICAL_ABUSE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_IPV_SEXUAL_ABUSE |  | IPV_SEXUAL_ABUSE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ISOLATION |  | ISOLATION_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ISOLATION_STATUS |  | ISOLATION_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_LAB_STATUS |  | LAB_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_LANGUAGE |  | LANGUAGE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_LD_COMPLICATION | Category values table for the LD_COMPLICATIONS table which contains labor complications. These labor complications are documented  | LD_COMPLICATIONS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_LETTER_TYPE |  | LETTER_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_LICENSE_DISPLAY | This table indicates the license to display for credentials. | LICENSE_DISPLAY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_LINES_GROUP |  | LINES_GROUP_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_LINK_TYPE_4 |  | LINK_TYPE_4_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_LIVING_W_SPOUSE | This table contains category IDs and values for the LIVING_W_SPOUSE_C column. | LIVING_W_SPOUSE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_LOGIN_TYPE | This table contains categories for User Action Log (UAL) login types. | LOGIN_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_LPP_TYPE |  | LPP_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_LVL_OF_CARE |  | LEVEL_OF_CARE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MARITAL_STATUS |  | MARITAL_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MAR_RSLT |  | RESULT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MAR_RSN |  | REASON_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MAR_TIME_SRC | This table contains the category items for the source of the actions stored on the MAR, ORD 11070. | MAR_TIME_SRC_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MC_ADM_SOURCE | This table contains the category items for the patient admission source. | ADMISSION_SOURCE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MC_ADM_TYPE | This table contains the category items for the patient admission type. | ADMISSION_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MC_PAT_STATUS | This table contains the category items for the discharge disposition/patient status. | PAT_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MEDCOM_TYPE |  | MEDCOM_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MEDICAL_HX |  | MEDICAL_HX_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MED_CYTO_WORKFL | This table contains the category information for the workflows for medical cytology case types. | MED_CYTO_WORKFL_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MED_DURATION_UN | This table extracts ECT category item 9080; RX TIME UNITS. | MED_DURATION_UN_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MED_MIXTURE_TEXT_TYPE |  | MED_MIXTURE_TEXT_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MED_TRANSPORT_NEEDS | This table contains the category numbers and names for the medical transportation needs column. | MED_TRANSPORT_NEEDS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MED_UNIT |  | DISP_QTYUNIT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MED_VERIFY_TYPE |  | MED_VERIFY_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MEM_REL_TO_SUB |  | MEM_REL_TO_SUB_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_METHOD_TYPE_2 |  | METHOD_TYPE_2_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_METRIC_DATE_DESC |  | METRIC_DATE_DESC_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_METRIC_STATUS |  | METRIC_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_METRIC_VALUE_DESC |  | METRIC_VALUE_DESC_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MFG |  | MFG_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MICRO_GENUS | This table contains the category information for organism genera. | MICRO_GENUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MICRO_GROUP | This table contains the category information for organism groups. | MICRO_GROUP_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MICRO_SPECIES | This table contains the category information for organism species. | MICRO_SPECIES_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MODALITY_TYPE | This is the category table for the SER 52000 category list. This is the type of modality. | MODALITY_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MOD_TYPE | The ZC_MOD_TYPE is a category table which stores the different types of changes that can be done on the OR template for a staff/re | MOD_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MOSAICISM |  | MOSAICISM_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MSG_CALLER_REL | The ZC_MSG_CALLER_REL table contains the name, title, abbreviation, and internal ID of the category for the relationship between t | MSG_CALLER_REL_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MSG_PRIORITY |  | MSG_PRIORITY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MYCHART_STATUS |  | MYCHART_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MYC_ACCT_TYPE | MyChart account type | MYC_ACCT_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MYC_CARE_PROGRAM | Extract table for the category LCE 81000. | MYC_CARE_PROGRAM_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MYC_MSG_TYP |  | MYC_MSG_TYP_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MYC_PAT_TYPE | Category table for web based chart system Patient type. Web based chart system Only Patient for Proxy Access | MYC_PAT_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MYC_PRXY_RELATN |  | MYC_PRXY_RELATN_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_MYC_STATUS |  | MYC_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_NATV_PRIM_FAIL |  | NAT_PRIMARY_FAIL_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_NCS_TOPIC |  | TOPIC_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_NEAREST_MED_TIM |  | NEAREST_MED_TIM_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_NOTEATTR_SOURCE |  | NOTEATTR_SOURCE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_NOTEATTR_SOURCE_TYPE | This table stores the type of the source by which the content entered the note. For example, content with attribution types "Copie | NOTEATTR_SOURCE_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_NOTE_FORMAT | This table extracts the note format category information for item ECT 7005. | NOTE_FORMAT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_NOTE_PURPOSE | This provides additional information on the type of note (i.e. normal, addendum, cosign.) | NOTE_PURPOSE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_NOTE_SER | This table contains information about the provider type category. | SERVICE_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_NOTE_SOURCE |  | NOTE_SOURCE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_NOTE_STATUS | This table stores all possible category values for the note status. Data from item ECT 7001 is saved here. | NOTE_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_NOTE_TYPE | The table indicates the note type. | NOTE_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_NOTE_TYPE_IP |  | TYPE_IP_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_NO_SHOW_ACTION | The ZC_NO_SHOW_ACTION table contains the name, title, abbreviation, and internal ID of the categories for a no show action. | NO_SHOW_ACTION_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_NO_SHOW_OUTCOME | The ZC_NO_SHOW_OUTCOME table contains the name, title, abbreviation, and internal ID of the categories for the outcome of a no sho | NO_SHOW_OUTCOME_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_NURSE_NOTE_STAT | The ZC_NURSE_NOTE_STAT table is a reference table for IP_NURSE_NOTES. | NURSE_NOTE_STAT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_NURSE_NOTE_TYPE | The ZC_NURSE_NOTE_TYPE table is a reference table for IP_NURSE_NOTES. | NURSE_NOTE_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OB_DEL_APGAR_1 |  | OB_DEL_APGAR_1_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OB_DEL_CERVRIPE |  | OBD_CERV_RIPE_T_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OB_DEL_EPISIO |  | OBD_EPISIOTOMY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OB_DEL_INDUCT |  | OBD_INDUCTION_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OB_DEL_INDUCT_RSN | This table contains the category information for the induction indications. | INDUCTION_REASON_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OB_DEL_LABOR_TYPE |  | OB_DEL_LABOR_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OB_DEL_RUPTCLR |  | OB_DEL_RUPTCOLOR_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OB_DEL_RUPTTYPE |  | OB_DEL_RUPTURE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OB_DEL_STEROIDS |  | OB_DEL_STEROIDS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OB_DT_EVENT |  | OB_DT_EVENT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OB_HX_IS_LIVING |  | OB_HX_IS_LIVING_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OB_HX_OUTCOME |  | OB_HX_OUTCOME_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OCCUPATION | This table contains the category information for patient's occupation. | OCCUPATION_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OCS_CONTEXT |  | OCS_CONTEXT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ORDERING_MODE |  | ORDERING_MODE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ORDER_CLASS |  | ORDER_CLASS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ORDER_PRIORITY | This table contains the category information for order priorities. | ORDER_PRIORITY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ORDER_SOURCE | Category information for Order Source category. | ORDER_SOURCE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ORDER_STATUS |  | ORDER_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ORDER_TYPE | This table contains information for the order type category list. | ORDER_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ORD_BLOB_TYPE | Category table | ORD_BLOB_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ORD_CNTCT_TYPE |  | CONTACT_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ORD_LST_ED_ACTI | Category table for ORD-760: Last edit action. | ORD_LST_ED_ACTI_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ORD_PROC_FREQ | Procedure frequency category list.  A procedure could be requested for a frequency of 4 per month, for example.  The category valu | ORD_PROC_FREQ_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ORGANISM_TYPE | The ZC_ORGANISM_TYPE table stores category information for organism types. | ORGANISM_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ORP_RPT_GRP_S2 |  | ORP_RPT_GRP_S2_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OR_ANSTAFF_TYPE |  | ANEST_STAFF_REQ_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OR_ASA_RATING | *** Deprecated *** The replacement table(s)/columns(s) are listed in the Replacement Objects/Columns grid. | ASA_RATING_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OR_AUDIT_ACTION | This table contains the category information for the audit actions that can be performed on the case. | AUDIT_ACTION_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OR_BLOCK |  | BLOCK_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OR_CANCEL_RSN | This table contains the category information for cancel reasons for procedural cases. | CANCEL_REASON_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OR_CASE_CLASS |  | CASE_CLASS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OR_EVENT_TYPE |  | TRACK_EVENT_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OR_LRB | This table contains the category information for the procedure laterality. | LRB_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OR_MANUFACTURER | This table consists of the category values to indicate the manufacturer in the inventory item (SUP) database. | MANUFACTURER_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OR_OLD_BLOCK |  | OLD_BLOCK_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OR_OP_REGION | This table contains the category information for the procedure operating region. | OPERATING_REGION_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OR_PANEL_ROLE |  | ROLE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OR_PAT_EVENTS |  | TRACKING_EVENT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OR_PAT_STATUS |  | CASE_PROGRESS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OR_SCHED_STATUS |  | SCHED_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OR_SERVICE | This table contains the category information for the procedural services. | SERVICE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OR_STAFF_TYPE | This table contains the category information for the staff type associated with a staff member on a procedural case. The staff typ | SURG_STAFF_REQ_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OR_STAFF_TYP_MAP | This table contains the category information for the staff type mapping associated with a staff member on a procedural case. The m | STAFF_TYPE_MAP_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OR_STATUS | This table contains the category information for status for procedural logs. | STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OR_TIMING_EVENT | This table contains the category information for the case timing events associated with a procedural case. | TIMING_EVENT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OR_TYPE_OF_PROC |  | TYPE_OF_PROC_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OR_WOUND_CLASS | This table contains the category information for the procedure wound class. | WND_CLS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OTHER_COMMUNIC |  | OTHER_COMMUNIC_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OTHER_TRANSPORT_NEEDS |  | OTHER_TRANSPORT_NEEDS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_OUTPUT_TYPE_P | This table contains the category information for the types of output in doc flowsheets. | OUTPUT_TYPE_P_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PASSIVE_SMOKE_EXPOSURE | Smoking Tobacco Passive Exposure Status for the Patient. | PASSIVE_SMOKE_EXPOSURE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PATIENT_FLAG_SRC |  | PATIENT_FLAG_SRC_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PATIENT_RACE | This table contains the category information for patient race. | PATIENT_RACE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PATIENT_STATUS | Category table to hold category values of item EPT 102 - Patient Status. | PATIENT_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PATIENT_TYPE | This table contains information about patient types. | PATIENT_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PATMSG_PRIORITY | This table contains the priority category items for patient messages.  This category is used by PATMSG_PRIORITY_C in HNO_INFO. | PATMSG_PRIORITY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PAT_CLASS | This table contains the category information for the patient classes for the hospital encounter. | ADT_PAT_CLASS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PAT_HOUSING_STA | This table stores the category list for the patient's current housing status. This information is required for the Ryan White gran | PAT_HOUSING_STA_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PAT_LIVING_STAT |  | PAT_LIVING_STAT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PAT_NAME_SUFFIX |  | PAT_NAME_SUFFIX_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PAT_RELATION |  | PAT_RELATION_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PAT_REPORTED_STATUS |  | PAT_REPORTED_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PAT_SERVICE |  | HOSP_SERV_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PAT_SIG_REPLY |  | PAT_SIG_REPLY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PAT_STATUS |  | ADT_PATIENT_STAT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PAT_TITLE |  | PAT_TITLE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PA_UNDO_RSN |  | PREADM_UNDO_RSN_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PCP_CHG_REQ_BY |  | CHANGE_REQ_BY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PCP_SWITCH_RSN |  | SWITCH_REASON_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PCP_TYPE |  | PCP_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PGX_DRUG_EFFICACY |  | PGX_DRUG_EFFICACY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PGX_DRUG_METAB |  | PGX_DRUG_METAB_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PGX_DRUG_TXPORT |  | PGX_DRUG_TXPORT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PGX_HIGH_RISK |  | PGX_HIGH_RISK_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PHAGE_TYPE | The ZC_PHAGE_TYPE table stores category information for organism phage types. | PHAGE_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PHARM_CLASS |  | PHARM_CLASS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PHARM_SUBCLASS |  | PHARM_SUBCLASS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PHONE_COMMUNICATION | This table contains category IDs and values for the PHONE_COMMUNICATION column. | PHONE_COMMUNICATION_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PHONE_REM_STAT | This is the status returned from an automated appointment reminder system.  Typically values for this are confirmed, cancelled, bu | PHONE_REM_STAT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PHOTO_APPROVED |  | PHOTO_APPROVED_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PHYSICAL_LOC | This is a category table defining a list of physical locations. Each category value in this table names a specific place, site or  | PHYSICAL_LOC_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PHYS_ACT_DAYS_PER_WEEK | This table contains category IDs and values for the PHYS_ACT_DAYS_PER_WEEK_C column. | PHYS_ACT_DAYS_PER_WEEK_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PHYS_ACT_MIN_PER_SESS | This table contains category IDs and values for the PHYS_ACT_MIN_PER_SESS_C column. | PHYS_ACT_MIN_PER_SESS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PHYS_TEMP_SRC | This table indicates the temperature source. | PHYS_TEMP_SRC_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PLAN_STATUS |  | PLAN_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PRIORITY_3 |  | PRIORITY_3_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PROBLEM_STATUS |  | PROBLEM_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PROCEDURE_SUBTYPE |  | PROCEDURE_SUBTYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PROCESSING_STAT |  | PROCESSING_STAT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PROC_NOT_DONE_R | This table contains the category information for procedure not performed reason. | PROC_NOT_DONE_R_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PROC_NOT_PERF | This table stores the list of reasons for a surgical procedure not being performed. | PROC_NOT_PERF_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PRODUCT_STATUS |  | PRODUCT_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PROD_TYPE |  | PROD_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PROVIDER_TYPE |  | PROVIDER_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PROV_LICENSURE |  | LICEN_REQD_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PROV_STATUS | The provider status assigned to the order (i.e. open, ordered, reviewed). | PROV_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PROV_TYPE | This table will be deprecated in a future release. You should use ZC_NOTE_SER when reporting on this category list. | PROV_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PRT_CLS |  | PRT_CLS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_PT_ENT_DRAW_STAT | This table contains the category information for the completion status of a patient-entered drawing document record. | PT_ENT_DRAW_STAT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_QUERY_REASON |  | QUERY_REASON_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_QUEST_TYPE |  | QUEST_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_RDT_TYPE | This table stores the category value, name, title, abbreviation and internal ID for category RDT 75 - Type | RDT_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_REACTION | This table contains the category information for allergic reactions. | REACTION_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_REASON_FOR_CANC |  | REASON_FOR_CANC_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_RECORD_STATE_5 |  | RECORD_STATE_5_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_RECORD_STAT_HRV | Category list of the HRV record state (ie. inactive, hidden, etc...) | RECORD_STAT_HRV_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_RECORD_STS | Contains a list of record statuses used for order event actions. | RECORD_STS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_REC_ACTION | This is the category list table for the IP Reconciliation Action (I IEV 1020) item, which stores the reconciliation action taken o | REC_ACTION_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_REGIMEN_CAT | This table extracts OSQ category item 30; Regimen Category. | REGIMEN_CAT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_RELATION_TO_PAT |  | RELATION_TO_PAT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_RELEASE_REASON | The ZC_RELEASE_REASON is a category table which stores the OR block release reasons. | RELEASE_REASON_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_RELIGION |  | RELIGION_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_REQ_CONTEXT | Care Everywhere Document Request Context records the manner in which a document was requested. Was it manual or automatic? Was it  | REQ_CONTEXT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_REQ_STATUS_RCVD | Status of a Care Everywhere document request. | REQ_STATUS_RCVD_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_RESP_METH |  | RESP_METH_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_RESULTS | This table holds information about the category values corresponding to which result notifications a provider on a patient's care  | RESULTS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_RESULT_FLAG |  | RESULT_FLAG_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_RESULT_STATUS |  | RESULT_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_RES_VAL_STATUS | This table contains the category information for the validation statuses of result records. | RES_VAL_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_RFL_CLASS |  | RFL_CLASS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_RFL_PRIORITY |  | PRIORITY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_RFL_STATUS |  | RFL_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_RFL_TYPE |  | RFL_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ROI_AUTH_TYPE |  | ROI_AUTH_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ROUTE |  | ROUTE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ROUTING_DEPT_TY | This table extracts ECT category item 5110; DEPARTMENT TYPES. | ROUTING_DEPT_TY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_RSN_FOR_DISCON |  | RSN_FOR_DISCON_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_RSN_FOR_RFL |  | RSN_FOR_RFL_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_RXNORM_CODE_LEVEL | This table contains the category information for RxNorm code level. | RXNORM_CODE_LEVEL_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_RXNORM_TERM_TYPE | This table contains a list of categories that represent term types for RxNorm codes. | RXNORM_TERM_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_RX_CUST_ID_ISSUE_ORG |  | RX_CUST_ID_ISSUE_ORG_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_RX_DISP_CUST_ID_TYPE | This is the Clarity table for the category I ECT 48000 - Rx Dispense Customer ID Type. | RX_DISP_CUST_ID_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_RX_DOCUMENT_STATUS |  | RX_DOCUMENT_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SCHED_STATUS |  | SCHED_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SDOH_ADDRESSED | This table contains the category IDs and names for the social drivers of health domains. | SDOH_ADDRESSED_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SEROTYPE | The ZC_SEROTYPE table stores category information for organism serotypes. | SEROTYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SEVERITY |  | SEVERITY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SEX |  | RCPT_MEM_SEX_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SEXUALLY_ACTIVE |  | SEXUALLY_ACTIVE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SEXUAL_ORIENTATION |  | SEXUAL_ORIENTATION_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SEX_ASGN_AT_BIRTH |  | SEX_ASGN_AT_BIRTH_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SIMPLE_GENERIC |  | SIMPLE_GENERIC_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SITE |  | SITE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SITE_OF_COLLECT |  | SITE_OF_COLLECT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SMOKELESS_TOB_U |  | SMOKELESS_TOB_U_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SMOKING_TOB_USE |  | SMOKING_TOB_USE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SOCIALIZATION_FREQ | This table contains category IDs and values for the SOCIALIZATION_FREQ_C column. | SOCIALIZATION_FREQ_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SOI_ROM | This table contains the category information for severity of illness and risk of mortality. This category list is used for diagnos | SOI_ROM_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SOURCE_OF_PRI_I | This table extracts the category values for the source of the prioritized date for orders. | SOURCE_OF_PRI_I_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SPECIALTY |  | SPECIALTY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SPECIALTY_DEP | This table contains the category information for department specialties. | SPECIALTY_DEP_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SPECIMEN_SOURCE |  | SPECIMEN_SOURCE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SPECIMEN_TYPE |  | SPECIMEN_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SPEC_AC | This table contains the category information for acute/convalescent flags for specimens. | SPEC_AC_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SPEC_DRAW_TYPE | This table contains the category information for draw types for specimens. | SPEC_DRAW_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SPEC_ORIGIN |  | SPEC_ORIGIN_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SPEC_SOURCE | This table contains the category information for specimen sources. | SPEC_SOURCE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SPEC_TEST_PRI | This table contains the category information for usual specimen priorities. | SPEC_TEST_PRI_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SR_PRIORITY | The ZC_SR_PRIORITY table is a reference table for IP_NURSE_NOTES. | SR_PRIORITY_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_STATE | This table contains the categories for state/province. | STATE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_STATUS_REASON |  | STATUS_REASON_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_STAT_ABNORMS | This table contains the category information for result checking abnormality levels. | STAT_ABNORMS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_STND_TP |  | STND_TP_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_STRUCT_TYPE |  | STRUCT_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_STYLESHEET | Categories table for report stylesheet. | STYLESHEET_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_ST_COMPREHENSIVE |  | ST_COMPREHENSIVE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SUSCEPT |  | SUSCEPT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_SYNOPSIS_DEPT | Categories table for department filter to be used on the synopsis view of a report. | SYNOPSIS_DEPT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_TASK | This table contains the category information for tasks that can be associated with actions. | TASK_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_TASK_ACTION | This table contains the category information for task actions. | TASK_ACTION_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_TAX_STATE | The category table for the state. | TAX_STATE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_TC_CANCEL_RSN | This table stores the reason why a Transfer Center request was canceled. | TC_CANCEL_RSN_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_TC_DECLINE_RSN | This table stores information about why a Transfer Center request destination was declined. | TC_DECLINE_RSN_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_TC_REQUEST_STATUS | This table stores information about the status of a Transfer Center request. | TC_REQUEST_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_TEAM_ACTION | This table extracts the team audit action category. | TEAM_ACTION_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_THERA_CLASS |  | THERA_CLASS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_TIME_SOURCE_STATUS |  | TIME_SOURCE_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_TOBACCO_USER |  | TOBACCO_USER_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_TOFROM_PAT |  | TOFROM_PAT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_TPL_BSA_SRC | The category table for the source of the treatment plan dosing BSA (body surface area). | TPL_BSA_SRC_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_TPL_HT_SOURCE | The category table for the source of the treatment plan dosing height. | TPL_HT_SOURCE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_TRANSCRIPT_SYSTEM |  | TRANSCRIPT_SYSTEM_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_TRIP_DATE_APPROX |  | TRIP_DATE_APPROX_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_TRTMNT_TEAM_INF | This table contains the category information for the Treatment Team Additional Information item, which stores additional informati | TRTMNT_TEAM_INF_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_TRTMT_TEAM_REL |  | TRTMNT_TEAM_REL_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_TRT_DAY_STATUS | This is the category table for the status of a treatment day. | TRT_DAY_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_TRT_GOAL | This table stores the list of treatment goals that can be assigned to a treatment plan. | TRT_GOAL_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_TT_ACTION | This is the table for the treatment team audit action category list. | TT_ACTION_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_TX_CLASS |  | TX_CLASS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_TX_CURRENT_STAG | Category table for transplant stage | TX_CURRENT_STAG_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_TX_STAT_OUT |  | TX_STAT_OUT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_TYPE |  | TYPE, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_TYPE_CASE | This table contains the category information for the types of anatomic pathology case type records. | TYPE_CASE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_UNLINK_REASON |  | UNLINK_REASON_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_USER_TYPES |  | USER_TYPES_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_VALUES_PER_EVNT | This table indicates the number of values per event. | VALUES_PER_EVNT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_VARIANT_FUNC_EFFECT |  | VARIANT_FUNC_EFFECT_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_VARIANT_MOLEC_CONSEQ |  | VARIANT_MOLEC_CONSEQ_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_VARIANT_SYSTEM |  | VARIANT_SYSTEM_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_VARIANT_TYPE |  | VARIANT_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_VERB_ORD_TYPE |  | SIGNED_TYPE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_VERIF_STATUS | This table contains the category information for the specimen validation statuses. | VERIF_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_VETERAN_STAT |  | VETERAN_STATUS_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_WAS_FILTERED | ALT 1200 category values | WAS_FILTERED_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
| ZC_WEIGHT_SOURCE | This table extracts ECT category item  55000; DOSING WEIGHT SOURCE. | WEIGHT_SOURCE_C, NAME, TITLE, ABBR, INTERNAL_ID |  |
