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
    * RTPN data from e-commerce payment provider
    * Transaction request data from Ecommerce payment forms
    * Transaction request data from select authorized UO Departments\
    * (see also) figure 2016-11-22-004
* MySQL database will be populated with batch/nightly/periodic updates from:
    * UO Central IS Quikpay reporting ()
    * (see also) figure 2016-11-22-004



#### Technical elements

* Specific-purpose accounts will be established for write access
* Specific-purpose accounts will be provisioned for read-only access
* Approximately five tables will be used with varying access for native MySQL privileges
* SSH tunneling may be required/provisioned for entire database access
* Permission and access model for row-level read/write will be established for each table.
