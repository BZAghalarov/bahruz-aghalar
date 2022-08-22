-- LOAD DATA INFILE '/home/bahruz/projects/tutorial/bahruz-aghalar/Hudson_Link/agency.txt'
-- INTO TABLE schedule_agency
-- FOR FIELDS TERMINATED BY ','
-- ENCLOSED BY '"'
-- LINES TERMINATED BY '\n'
-- IGNORE 1 ROWS;


COPY schedule_agency
FROM '/home/bahruz/projects/tutorial/bahruz-aghalar/cedarsystems/Hudson_Link/agency.txt'
DELIMITER ','
CSV HEADER;

