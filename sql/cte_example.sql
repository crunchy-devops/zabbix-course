WITH level4 AS (SELECT * FROM account WHERE
frequent_flyer_id IN (
                        SELECT frequent_flyer_id FROM frequent_flyer WHERE level =4
                     ))
SELECT * FROM booking WHERE account_id IN
(SELECT account_id FROM level4)