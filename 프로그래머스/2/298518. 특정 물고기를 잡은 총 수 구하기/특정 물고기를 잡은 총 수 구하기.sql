SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO f, FISH_NAME_INFO n
WHERE f.FISH_TYPE = n.FISH_TYPE AND n.FISH_NAME in ('BASS', 'SNAPPER');