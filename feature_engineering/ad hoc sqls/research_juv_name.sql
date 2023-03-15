	--12127, 12123
    select DISTINCT dcr.acc_rpt_num, dcr.acc_uuid, 
	coalesce(dcr.Name, ii.Name) name,  
	coalesce(dcr."Personal Injury", ii."Injury Type") injury_type, 
	coalesce(dcr.Age, ii.Age) age,
	coalesce(dcr."Person City/State", ii."City/State") city_state,
	dcr."Safety Device" AS safety_device, 
    dcr.Date AS date, 
    dcr.Time AS time, 
    dcr.Troop AS troop, 
    ii.Gender AS gender,
	ii."Veh. #" as veh_num, 
	ii."Involvement" AS involvement
	from daily_crash_report dcr
	left outer join injury_information ii on dcr.acc_uuid = ii.acc_uuid  --13751, inner(10129)
	and dcr.Name = ii.Name 
	and dcr.Age = ii.Age 
	and dcr."Person City/State" = ii."City/State"	
	where dcr.Name != 'JUVENILE,'
	AND dcr.NAME NOT LIKE 'UNKNOWN%'
	
	select * from daily_crash_report where Name != 'JUVENILE,' AND NAME NOT LIKE 'UNKNOWN%' - 12033
