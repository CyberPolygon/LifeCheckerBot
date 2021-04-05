WITH team_created_id AS (
	INSERT INTO team(
		team_name
	,	captain_id
	)
	VALUES(
		{team_name}
	,	{captain_id}
	)
	RETURNING
		id
)
UPDATE
	"user"
SET
	team_id = (
		SELECT
			id
		FROM
			team_created_id
	)
WHERE
	id = {captain_id}
RETURNING
	team_id;