# Consolidated Note around EDA

## Tactical Steps
Target -> Personal Injury -> severe+, severe-
### Crash Report
Row Count: 13,689
Grain of table: acc_uuid
Keys -> acc_rpt_num,
Example Name duplicated in same acc_rpt_num - speculate this is "Driver" Name, 
where key may be passengers 
Information Rich Fields: 
    * Age, 
    * Personal Injury
    * Safety Device (Imbalanced)
    * Date
    * Troop
Fields to Feature Engineer:
    * Person City/State -> extract State
    * Time -> Cosine/Sine
    * County -> Large/Medium/Small
### Crash Information 
Row Count: 13,689
Grain of table: acc_uuid
Low Entropy (via High Cardinality) 
    * Investigated By (Not in Summary)
    * Location
Lowish Data Quality :
    * Missingness (GPS 1/3 missing) -(Not in Summary)
Fields to Feature Engineer:
    County -> 115 -> map to big, medium, small
    High Entropy Fields:
    Troop
Overall -> doesn't provides too much additional info from Summary - besides indicated above

### Injury Information
Row Count: 13,689
Grain of table: Crash Report + Name


Check in SQL: 
So - it seems injury information is per crash report; Name may be all involved parties. 

Main issue is Juvenile 
Useful Column
    * Involvement (Driver, Occupant, Other)
Low Information
    * Disposition (change for text analytics)
Feature Engineering 
    * Veh. # (mostly 1 55%, 2-16%) (single versus multi-car)
    * 

### Vehicle Information

Similiar issue as Injury Information

A couple approaches --> injury information
acc_ui + veh # 
appears --> it's specific to driver?

Low Information
    * Vehicle Information (may be candidate for feature engineering (e.g. year, brand))
    * Disposition (Car)
    * Insurance (Feature Eng. Candidate - national versus regional... so many surprising)
Useful Columns"
    * Damage
    * Driver Gender
    * Driver Age
    * Vehicle Direction

Plan -> Summary Report -> Injury Report -> Add Vehicle Information

### Misc. Information

Free form text -> may be interesting from 
text analytics purpose