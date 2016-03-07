create table aircraft(
    aid int primary key,
    aname int varchar(12),
    crange int
);

create table flights
(
    flno int,
    flfrom varchar(12),
    flto varchar(12),
    distance int,
    departs timestamp,
    arrives timestamp,
    price int,
    foreign key(flno) references aircraft(aid)
);

create table employees
(
    eid int primary key,
    ename varchar(12),
    salary int
);

create table certified
(
    eid int,
    aid int,
    primary key(eid,aid),
    foreign key(eid) references employees(eid),
    foreign key(aid) references aircraft(aid)
);

