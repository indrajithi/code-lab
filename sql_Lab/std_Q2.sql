sqlite3 -separator $'\t' -header lab.db "
select c.cname 
from class c 
where c.room = 'r128'
OR c.cname in ( select e.cname from enrolled e 
               group by e.cname having count(*)>5);"
                 

SELECT s.sname FROM student s
WHERE  s.snum IN (
                    SELECT e1.snum 
                    FROM   enrolled e1, enrolled e2, class c1, class c2 
                    WHERE  e1.snum = e2.snum
                    AND    e1.cname = c1.cname
                    AND    e1.cname = c1.cname 
                    AND    c1.time = c2.time
                    AND    e1.cname <> e2.cname
                  );
