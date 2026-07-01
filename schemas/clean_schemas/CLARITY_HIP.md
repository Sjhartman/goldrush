# CLARITY_HIP

**Source:** https://datahandbook.epic.com/ClarityDictionary/Details?tblName=CLARITY_HIP

## Description

In Basket Registries store information to determine the recipients who can display and handle specific types of messages. This table contains the basic information about these Registries. Registries are stored in the HIP master file.

## Metadata

| Property | Value |
| --- | --- |
| Type | Extracted Table |
| Load Type | FULL |
| Load Frequency | WEEKLY - FULL |
| Chronicles INI | HIP |
| Release Version | SPRING 2007 |
| May contain EHI? | Yes |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| REGISTRY_ID | NUMERIC (18,0) | The Registration Identification Number |
| REGISTRY_NAME | VARCHAR (254) | The name of the In Basket registry in the HIP master file. |
| REGSTRY_STATUS_C | INTEGER |  |
| LOGICAL_OWNER | No | This column has been deprecated.  It has been replaced with CM_LOG_OWNER_ID. |
| PHYSICAL_OWNER | No | This column has been deprecated.  It is being replaced with CM_PHY_OWNER_ID. |
| REGISTRY_DESC | VARCHAR (254) | This is a description of the Registry.  It may include information about how the Registry is set up to determine recipients and how it is to be used. |
| RECIP_MASTERFILE | VARCHAR (3) | Indicates whether recipients receive messages through the User (EMP), Workstation (LWS), or Patient (EPT) master files. |
| SELECTION_INI | VARCHAR (3) | Stores whether recipients are chosen from the User (EMP), Provider (SER), Department (DEP), Workstation (LWS) or Patient (EPT) master files.   Note: other master files may be used in special cases. |
| CAT_SELECT_ITEM | VARCHAR (100) | This item is where you can optionally restrict selection of recipients to groups.  To do so, select an item within the "Send Message to" master file (preferably a category list).  This makes it so that you can no longer send messages to individuals; you can only send messages to groups made up of all the individuals who have common values for the specified Selection Item. |
| SEARCH_ITEM *(deprecated)* | VARCHAR (100) | *** Deprecated *** In table CLARITY_HIP, the column SEARCH_ITEM (HIP/100) has been deprecated.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| MASTER_LIST *(deprecated)* | VARCHAR (100) | *** Deprecated *** In table CLARITY_HIP, the column MASTER_LIST (HIP/105) has been deprecated.  The deprecated column's content/data is no longer available since it is no longer populated in Chronicles. |
| GET_ID_LPP_ID | NUMERIC (18,0) | This item allows you to specify the Selection Linker (a programming point) to be used to make the connection between the "Send Message to" master file and the "Message Received by" master file.  The STANDARD SELECTION LINKER (2700) connects User, Provider, and Department to User; Workstation to Workstation; and Patient to Patient |
| RX_REFIL_POOL_YN | VARCHAR (1) |  |
| DEFAULT_AS_POOL_YN | VARCHAR (1) |  |
| MAIL_SYSTEM_C | INTEGER |  |
| EXTERNAL_ACCOUNT | VARCHAR (100) | External account is used only when the Mail System prompt is set to "External Mail".  This setting indicates that mail generated in your licensed applications shall be routed to an external mail system.  The account name to route messages to is stored here.    The format of a mail account using SMTP/POP services is name@companyname.com |
| SEND_SYSTEM_ID | NUMERIC (18,0) | If the Mail System prompt is set to "External Mail" this is where the external system service (LPP record) to be used to route messages to an external account is stored. |
| CLASS_ITEM | VARCHAR (100) | If your Registry is not a pool, you can simplify selection of groups of recipients by defining classes.  To do so, select an item within the "Send Message to" master file (preferably a category list).  You can then choose to send a message to individuals, or to classes made up of all the  individuals who have a common value for the specified Class Selection  Item. |
| ACTIVE_REGISTRY_C | INTEGER |  |
| XTRN_MAIL_STRCT_ID | NUMERIC (18,0) | This is the programming point to be used to format a message routed to an external e-mail address. |
| USE_XTRN_ITEM | VARCHAR (100) | If this registry can be used to route messages to an external e-mail address this item stores the item in the "Message Received by" master file that indicates whether messages should be sent to an external e-mail address. |
| SEND_SYSTEM_ITEM | VARCHAR (100) | If this registry can be used to route messages to an external e-mail address, this column stores the item in the "Message Received by" master file that indicates the type of the sending system used to send message. |
| XTRN_ADDRESS_ITEM | VARCHAR (100) | If this registry can be used to route messages to an external e-mail address, this column stores the item in the "Message Received by" master file that indicates the e-mail address to which external messages should be sent. |
| ACCOUNT_NAME_ITEM | VARCHAR (100) | If this registry can be used to poll messages from an external POP server, this column stores the item in the "Message Received by" master file that  indicates the email address of the POP account. |
| ACCOUNT_PASWD_ITEM | VARCHAR (100) | If this registry can be used to poll messages from an external POP server, this column stores the item in the "Message Received by" master file that  indicates the password of the POP account. |
| PAGER_ID_ITEM | VARCHAR (100) | If this registry can be used to send messages to the pagers, this column stores the item in the "Message Received by" master file that indicates Pager ID. |
| SYSTEM_ITEM | VARCHAR (100) | If this registry can be used to send messages to the pagers, this column stores the item in the "Message Received by" master file that indicates the type of  the service used by the pager. |
| ALPHANUMERIC_ITEM | VARCHAR (100) | If this registry can be used to send messages to the pagers, this column stores the  item in the "Message Received by" master file that indicates whether the pager can handle the alpha/numeric messages. |
| MSG_TYPES_ITEM | VARCHAR (100) | If this registry can be used to send messages to the pagers, this column stores the item in the "Message Received by" master file that indicates the type of the messages to be sent to the pager. |
| CHART_STATION | VARCHAR (18) | When you forward a chart to a pool of users from the Deficiency Completion activity, the system checks this field to determine the default destination chart station. |
| INST_NOADD_EDIT *(deprecated)* | DATETIME | *** Deprecated *** This data item has been discontinued and replaced with item level tracking auditing.   This is the last instant where a noadd item was edited. |
| NOADD_ITEMS_EDITED *(deprecated)* | VARCHAR (508) | *** Deprecated *** This data item has been discontinued and replaced with item level tracking.  These are the items that were edited on the instant of noadd edit. |
| CM_LOG_OWNER_ID | VARCHAR (25) | ID of the logical deployment owner for this record. Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |
| CM_PHY_OWNER_ID | VARCHAR (25) | ID of the physical deployment owner for this record. Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| LMT_RECV_TYPES_YN | VARCHAR (1) |  |
| USE_CONFIG_YN | VARCHAR (1) |  |
| PRIM_POOL_MNGR_ID | VARCHAR (18) | Item 20414 in the Registry master file will allow manual configuration of the primary manager of a pool.  It will store the user ID of the primary manager. It will be configured by administrators. |
| USE_CALC_POOL_MN_YN | VARCHAR (1) |  |
| LIMIT_MSG_TYPE_CAL_YN | VARCHAR (1) |  |
| REASON_NO_MSG_C | INTEGER |  |
| DIST_SCHEME_ID | NUMERIC (18,0) | Store the distribution scheme this pool routes to |
| EXTERNAL_NAME | VARCHAR (254) | Name shared in provider directory |
| DIRECT_ADDRESS | VARCHAR (254) | Mixed case Direct address for this pool |
| HIP_SHARED_YN | VARCHAR (1) |  |
| CE_POOL_ROUTING_C | INTEGER |  |
| CE_EXTERNAL_POOL_IDENT | VARCHAR (192) | CE external pool ID for HIP record in provider directory. |
| INVALID_HIP | VARCHAR (192) | If an invalid pool was the reason pool is unable to recieve a message, this item will tell you which HIP was invalid. |

## Foreign Keys

| Pos. | Src. Col. | Dest. Tbl. | Dest. Col. | Cond? | May Be Stale? | Supp? |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | REGISTRY_ID | IB_REG_BASE_DEPLY | REGISTRY_ID | No | No | No |  |
| 3 | REGSTRY_STATUS_C | ZC_DEL_STATUS | DEL_STATUS_C | No | No | No |  |
| 3 | REGSTRY_STATUS_C | ZC_EDG_REC_STAT | EDG_REC_STAT_C | No | No | No |  |
| 3 | REGSTRY_STATUS_C | ZC_ERS_REC_STAT | RECORD_STATUS_C | No | No | No |  |
| 3 | REGSTRY_STATUS_C | ZC_HCD_REC_STATE | HCD_REC_STATE_C | No | No | No |  |
| 3 | REGSTRY_STATUS_C | ZC_HFL_RECORD_STAT | HFL_RECORD_STAT_C | No | No | No |  |
| 3 | REGSTRY_STATUS_C | ZC_IMM_REC_STATUS | IMM_REC_STATUS_C | No | No | No |  |
| 3 | REGSTRY_STATUS_C | ZC_LLB_STATUS | LLB_STATUS_C | No | No | No |  |
| 3 | REGSTRY_STATUS_C | ZC_LMA_RECORD_STAT | LMA_RECORD_STAT_C | No | No | No |  |
| 3 | REGSTRY_STATUS_C | ZC_MEM_REC_STATUS | MEM_REC_STATUS_C | No | No | No |  |
| 3 | REGSTRY_STATUS_C | ZC_OR_REC_STATUS | OR_REC_STATUS_C | No | No | No |  |
| 3 | REGSTRY_STATUS_C | ZC_PBA_REC_STAT | PBA_REC_STAT_C | No | No | No |  |
| 3 | REGSTRY_STATUS_C | ZC_PROV_REC_STATE | PROV_REC_STATE_C | No | No | No |  |
| 3 | REGSTRY_STATUS_C | ZC_RECORD_STATE_2 | RECORD_STATE_2_C | No | No | No |  |
| 3 | REGSTRY_STATUS_C | ZC_RECORD_STATE_3 | RECORD_STATE_3_C | No | No | No |  |
| 3 | REGSTRY_STATUS_C | ZC_RECORD_STATE_4 | RECORD_STATE_4_C | No | No | No |  |
| 3 | REGSTRY_STATUS_C | ZC_RECORD_STATE_6 | RECORD_STATE_6_C | No | No | No |  |
| 3 | REGSTRY_STATUS_C | ZC_RECORD_STATE_7 | RECORD_STATE_7_C | No | No | No |  |
| 3 | REGSTRY_STATUS_C | ZC_RECORD_STAT_EPM | RECORD_STAT_EPM_C | No | No | No |  |
| 3 | REGSTRY_STATUS_C | ZC_RECORD_STAT_EPP | RECORD_STAT_EPP_C | No | No | No |  |
| 3 | REGSTRY_STATUS_C | ZC_RECORD_STAT_ETX | RECORD_STAT_ETX_C | No | No | No |  |
| 3 | REGSTRY_STATUS_C | ZC_RECORD_STAT_HRV | RECORD_STAT_HRV_C | No | No | No |  |
| 3 | REGSTRY_STATUS_C | ZC_RECORD_STAT_RMC | RECORD_STAT_RMC_C | No | No | No |  |
| 12 | GET_ID_LPP_ID | CLARITY_LPP | LPP_ID | Unknown | No | No |  |
| 15 | MAIL_SYSTEM_C | ZC_MAIL_SYSTEM | MAIL_SYSTEM_C | Unknown | Unknown | Yes |  |
| 15 | MAIL_SYSTEM_C | ZC_MAIL_SYSTEM_2 | MAIL_SYSTEM_2_C | No | No | No |  |
| 17 | SEND_SYSTEM_ID | CLARITY_LPP | LPP_ID | Unknown | No | No |  |
| 19 | ACTIVE_REGISTRY_C | ZC_ACTIVE_REGISTRY | ACTIVE_REGISTRY_C | No | No | No |  |
| 19 | ACTIVE_REGISTRY_C | ZC_YES_NO | YES_NO_C | Unknown | Unknown | Yes |  |
| 20 | XTRN_MAIL_STRCT_ID | CLARITY_LPP | LPP_ID | Unknown | No | No |  |

_(54 total; showing first 30)_
