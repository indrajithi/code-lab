sqlite3 -separator $'\t' -header lab.db "
select s.sname 
from student s, class c, faculty f, enrolled e
where f.fname = 'harshith'
and f.fid = c.fid
and c.cname = e.cname
and e.snum = s.snum
and s.level1 = 'jr'
";

