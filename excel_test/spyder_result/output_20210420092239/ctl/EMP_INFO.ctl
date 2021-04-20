LOAD DATA
INFILE ~
INSERT INTO EMP_INFO
(
emp_id,
emp_name,
emp_name_kana,
update_date DATE to_char(to_date(:update_date,'YYYY/MM/DD')),
)