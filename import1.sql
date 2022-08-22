LOAD DATA INFILE '/home/bahruz/projects/tutorial/bahruz-aghalar/Hudson_Link/agency.txt'
INTO TABLE schedule_agency
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;