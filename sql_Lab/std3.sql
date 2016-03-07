create table student (
    regno varchar(12) primary key,
    name varchar(12),
    major varchar(12),
    bdate date
);

create table course (
    courseid int primary key,
    ename varchar(5),
    dept varchar(5)
);

create table enrolled
(
    regno varchar(12),
    courseid int,
    sem int,
    marks int,
    primary key(regno , courseid),
    foreign key(regno) references student(regno),
    foreign key(courseid) references course(courseid)
);

create table text
(
    bookisbn int primary key,
    booktitle varchar(12),
    publisher varcahr(12),
    author varchar(12)
);
create table bookadp(
    courseid int,
    sem int,
    bookisbn int,
    primary key(courseid,sem),
    foreign key(courseid) references course(courseid),
    foreign key(bookisbn) references text(bookisbn)
);
