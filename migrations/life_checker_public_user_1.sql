create table "user"
(
    id              integer not null
        constraint user_pk
            primary key,
    team_id         integer
        constraint user_team_id_fk
            references team,
    full_name       varchar(80),
    phone_number    varchar(12),
    university_name varchar(30),
    study_group     varchar(10),
    telegram        varchar(48),
    github          varchar(48),
    vkontakte       varchar(48),
    email           varchar(48),
    tshirt_size     varchar(4)
);

alter table "user"
    owner to postgres;

create unique index user_id_uindex
    on "user" (id);

create unique index user_email_uindex
    on "user" (email);

create unique index user_github_uindex
    on "user" (github);

create unique index user_phone_number_uindex
    on "user" (phone_number);

create unique index user_telegram_uindex
    on "user" (telegram);

INSERT INTO public."user" (id, team_id, full_name, phone_number, university_name, study_group, telegram, github, vkontakte, email, tshirt_size) VALUES (215496538, null, 'Николенко Роман Евгеньевич', '+79834578656', 'СИБГУТИ', 'АВ-82', 'madwayz1337', 'https://github.com/madwayz1337', 'https://vk.com/madwayz1337', 'djurball@list.ru', 'L');