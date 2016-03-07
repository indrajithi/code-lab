CREATE TABLE student 
(
    snum int primary key,
    sname varchar(12),
    major varchar(5),
    level1 varchar(5)
);

CREATE TABLE faculty
(
    fid int primary key,
    fname varchar(12),
    deptid int
);

CREATE TABLE class
(
    cname varchar(12) primary key,
    time varchar(5),
    room varchar(5),
    fid int,
    foreign key(fid) references faculty(fid)
);

CREATE TABLE enrolled
(
    snum int,
    cname varchar(15),
    primary key(snum,cname),
    foreign key(snum) references student(snum),i
    foreign key(cname) references class(cname)
);

INSERT INTO student  VALUES('1','indra','cse','sr','21');
INSERT INTO student  VALUES('2','pranav','cse','jr','19');
INSERT INTO student  VALUES('3','raju','cse','sr','20');
INSERT INTO student  VALUES('4','sneha','cse','sr','21');
INSERT INTO student  VALUES('5','swathi','cse','jr','23');
INSERT INTO student  VALUES('6', 'sreya','cse','sr','21');
INSERT INTO student  VALUES('7','shreya','cse','jr','22');
INSERT INTO student  VALUES('8','swaraj','cse','jr','22');
INSERT INTO student  VALUES('9','susma','cse','sr','21');

insert into faculty values('101','harshith','10');
insert into faculty values('111','karthik','10');
insert into faculty values('121','danash','10');
insert into faculty values('131','darshan','12');

insert into class values('dbms','2pm','r234', '111');
insert into class values('os','5pm','r128', '112');
insert into class values('ss','1pm','r235', '113');
insert into class values('flat','2pm','r236', '114');
insert into class values('se','3pm','r128', '1112');
insert into class values('cn','4pm','r237', '113');

insert into enrolled values('3','dbms');
insert into enrolled values('4','os');
insert into enrolled values('5','flat');
insert into enrolled values('1','se');
insert into enrolled values('2','ss');
insert into enrolled values('3','flat');
insert into enrolled values('4','os');
insert into enrolled values('6','dbms');
insert into enrolled values('9','cn');
insert into enrolled values('8','se');
insert into enrolled values('7','ss');
insert into enrolled values('9','cn');

