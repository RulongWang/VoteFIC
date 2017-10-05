drop table if exists voting;
create table voting (
  id integer primary key autoincrement,
  voterid string not null,
  ideanum string not null,
  type string not null,
  value INTEGER not null
);