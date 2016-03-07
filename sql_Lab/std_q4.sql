SELECT f.fname 
FROM faculty f 
WHERE EXISTS (select c1.room from class c1 where c1.fid = f.fid);
