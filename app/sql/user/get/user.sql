SELECT
	id
,   team_id
,	full_name
,	phone_number
,	university_name
,	study_group
,	telegram
,	github
,	vkontakte
,	email
,	tshirt_size
FROM
	"user"
WHERE
	id = '{id}';