select f.fname 
from faculty f
where (select count(e.snum)
        from enrolled e, class c
        where e.cname = c.cname
        and c.fid = f.fid) <5 ;
