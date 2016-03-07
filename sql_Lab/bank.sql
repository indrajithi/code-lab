create table branch
(
    brname varchar(12) primary key,
    brcity varchar(12),
    assets int 
);   

create table account
(
    account int primary key,
    brname varchar(12),
    balance int,
    foreign key (brname) references branch (brname)
);

create table customer
(
    cname varchar(12) primary key,
    cstreet varchar(12),
    ccity varchar(12)
);

create table depositor
(
    cname varchar(12),
    accno int,
    primary key(cname,accno),
    foreign key(cname) references customer(cname),
    foreign key(accno) references account(accno) on delete cascade
);

create table loan
(
    loanno int primary key,
    brname varchar(12),
    amount int,
    foreign key(brname) references branch(brname)
);
 
create table borrower
(   
    cname varchar(12),
    loanno int,
    primary key(cname, loanno),
    foreign key(cname) references customer(cname),
    foreign key(loanno) references loan(loanno)
);



