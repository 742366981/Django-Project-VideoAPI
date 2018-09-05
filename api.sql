use api;

-- 电影
create table movie
(
id int not null auto_increment,
movie_img varchar(255) not null,
movie_name varchar(100) not null unique,
director varchar(50) not null,
staring varchar(200) not null,
movie_type varchar(20) not null,
area varchar(20) not null,
languages varchar(30) not null,
release_time varchar(50) not null,
update_time varchar(30) not null,
summary varchar(2000) not null,
play_url varchar(255) not null,
primary key (id)
);

-- 电视剧
create table tv
(
tv_img varchar(255) not null,
tv_name varchar(100) not null unique,
director varchar(50) not null,
staring varchar(200) not null,
tv_type varchar(20) not null,
area varchar(20) not null,
languages varchar(30) not null,
release_time varchar(50) not null,
update_time varchar(30) not null,
summary varchar(2000) not null,
primary key (tv_name)
);

-- 综艺
create table shows
(
show_img varchar(255) not null,
show_name varchar(100) not null unique,
director varchar(50) not null,
staring varchar(200) not null,
show_type varchar(20) not null,
area varchar(20) not null,
languages varchar(30) not null,
release_time varchar(50) not null,
update_time varchar(30) not null,
summary varchar(2000) not null,
primary key (show_name)
);

-- 动漫
create table animation
(
animation_img varchar(255) not null,
animation_name varchar(100) not null unique,
director varchar(50) not null,
staring varchar(200) not null,
animation_type varchar(20) not null,
area varchar(20) not null,
languages varchar(30) not null,
release_time varchar(50) not null,
update_time varchar(30) not null,
summary varchar(2000) not null,
primary key (animation_name)
);

-- 福利
create table fuli
(
id int not null auto_increment,
fuli_img varchar(255) not null,
fuli_name varchar(100) not null unique,
director varchar(50) not null,
staring varchar(200) not null,
fuli_type varchar(20) not null,
area varchar(20) not null,
languages varchar(30) not null,
release_time varchar(50) not null,
update_time varchar(30) not null,
summary varchar(2000) not null,
play_url varchar(255) not null,
primary key (id)
);

-- 电视剧集数
create table tv_list
(
id int not null auto_increment,
tv_name varchar(100) not null,
num varchar(30) not null,
play_url varchar(255) not null unique,
primary key (id),
foreign key (tv_name) references tv (tv_name)
);

-- 综艺期数
create table show_list
(
id int not null auto_increment,
show_name varchar(100) not null,
num varchar(30) not null,
play_url varchar(255) not null unique,
primary key (id),
foreign key (show_name) references shows (show_name)
);

-- 动漫集数
create table animation_list
(
id int not null auto_increment,
animation_name varchar(100) not null,
num varchar(30) not null,
play_url varchar(255) not null unique,
primary key (id),
foreign key (animation_name) references animation (animation_name)
);