# Overview

This writeup enumerates the top-level requirements for deployment, hosting and maintenance of an e-commerce system to UO Central Drupal Hosting (hereinafter "target_system"). This e-commerce system is currently provisioned and designed by the UO Business Affairs Office.

## System Requirements

This writeup assumes the following minumum requirements for the target_system:

* MySQL innodb database version 5.4.x or newer (prefer 5.7.x)
* PHP version 5.3.3 or newer (prefer PHP 5.6.x)
* Linux server RHEL 6.8 or newer
* Drupal CMS 7.52 or newer

## System Elements

This writeup assumes the following core elements for the target_system.

Some elements may be hosted on servers other than those provided by UO Central Drupal Hosting. Some elements may be optionally added to or removed from UO Central Drupal Hosting. This is specified in this writeup, whenever and wherever such may be the case.

The following diagram serves as the primary visual template for enumerating the elements of the target_system.

* [chart-000](https://github.com/dreftymac/public.lab/blob/master/topic/ecommuod/image/specchart000.png)

![specchart-000](https://cloud.githubusercontent.com/assets/4074354/20541457/31c16106-b0b2-11e6-8cef-00d62e2b28d2.png)

### Element 001: Ecommerce Forms and Ecommerce Reporting

* Consists of one or more Drupal CMS websites
* Ecommerce Forms currently rely on Drupal7 CMS with enumerated contrib modules and content types
* Ecommerce Reporting currently relies on Drupal7 CMS with enumerated contrib modules and content types

### Element 002: MySQL database with approx five tables for read-write access

#### Operational elements

* MySQL database will be populated with real-time updates from:
    * Real-Time-Payment-Notification (hereinafter "RTPN") data from e-commerce payment provider
    * Transaction request data from Ecommerce payment forms
    * Transaction request data from select authorized UO Departments\
    * (see also) figure 2016-11-22-004

* MySQL database will be populated with batch/nightly/periodic updates from:
    * UO Central IS Quikpay reporting (see also joey@)
    * (see also) figure 2016-11-22-004

* MySQL database will provide real-time updates to:
    * Drupal CSM via Drupal Migrate Module
    * (see also) figure 2016-11-22-004

#### Technical elements

* Specific-purpose accounts will be established for write access
* Specific-purpose accounts will be provisioned for read-only access
* Approximately five tables will be used with varying access for native MySQL privileges
* SSH tunneling may be required/provisioned for entire database access
* Permission and access model for row-level read/write will be established for each table.

### Element 003: WEB-API Transaction Handler and related elements

* Web-based API for handling incoming transaction requests (via REST-API or otherwise)
* Web-based API for handling incoming RTPN payment notifications (via https)

#### Operational elements

* Incoming RTPNs currently obtained over https to specific URL configured in Quikpay Portal
* Incoming EOD batch reports currently obtained from UO Central IS (see also joey@)

### Element 004: External Interop with the system

* Select UO departments may be authorized to submit payment transaction requests (Figure 2016-11-22-004a)
* Quikpay Portal is authorized to send RTPNs to a specific URL or set of URLs at UO (Figure 2016-11-22-004b)
* UO Central IS is authorized to send End Of Day batch files (hereinafter "EOD") to a single-purpose Linux account over SCP (Figure 2016-11-22-004c)

### Element 005: EOD/RTPN/Batches and Transaction Interop

* Currently the EOD/RTPN input requires shell scripts for parsing and loading.
* These may be transitioned to MySQL load-data-infile queries for easier maintenance and better performance/throughput.

### Element 006: Drupal CMS Migrate process

* Currently the target_system requires routine updates from MySQL to Drupal Migrate, in order to convert the external content into Drupal nodes.
* The Migrate process requires crontab entries in order to routinely refresh the Drupal CMS as frequently as every few minutes.





* ![figure-001](https://cloud.githubusercontent.com/assets/4074354/20542606/331a7e48-b0b7-11e6-8058-1705782d9dfc.png =250x250)
* ![figure-002](https://cloud.githubusercontent.com/assets/4074354/20542611/35bea926-b0b7-11e6-8cbc-33d65f64b961.png =250x250)
* ![figure-003](https://cloud.githubusercontent.com/assets/4074354/20542614/38d7543c-b0b7-11e6-9327-aff428b16086.png =250x250)
* ![figure-004](https://cloud.githubusercontent.com/assets/4074354/20542619/3cfdcbb8-b0b7-11e6-93ba-1c5ed049e408.png =250x250)
* ![figure-005](https://cloud.githubusercontent.com/assets/4074354/20542625/420c2cb2-b0b7-11e6-99a6-500eb144db53.png =250x250)
* ![figure-006](https://cloud.githubusercontent.com/assets/4074354/20542629/462bc532-b0b7-11e6-9a56-83b8ff74a7c0.png =250x250)
