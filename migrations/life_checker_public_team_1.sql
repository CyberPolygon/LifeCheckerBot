create table team
(
    id         serial      not null
        constraint team_pk
            primary key,
    team_name  varchar(30) not null,
    captain_id integer     not null
);

alter table team
    owner to postgres;

create unique index team_captain_id_uindex
    on team (captain_id);

create unique index team_id_uindex
    on team (id);

create unique index team_name_uindex
    on team (team_name);

INSERT INTO public.team (id, team_name, captain_id) VALUES (11, '[LIFE] Laboratory', 215496538);