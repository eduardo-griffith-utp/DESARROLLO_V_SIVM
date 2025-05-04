create table if not exists Session(
	id_session int primary key not null,
	name_session varchar(20)
);


create table if not exists MediaContent(
	id_media int primary key not null,
	user_id int not null,
	route_path varchar(64),
	type_content varchar(30),
	description varchar(50),
	date_uploaded datetime not null
);

create table if not exists AnalysisResult(
	id_results int primary key not null,
	media_is int not null,
	detected_labes varchar(50),
	date_analysis datetime not null
);

create table if not exists QueryHistory(
	id_query int primary key not null,
	media_id int not null,
	date_consultation datetime not null,
	counter int not null
);

create table if not exists Items(
	id_items int primary key not null,
	media_id int not null,
	name varchar(30) not null,
	description text not null
);

create table if not exists ItemTags(
	id_tag int primary key not null,
	item_id int not null,
	tag_name varchar(30) not null
);
