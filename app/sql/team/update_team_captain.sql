UPDATE
	team
SET
	captain_id={captain_id}
WHERE
	id={team_id}
RETURNING
	id;