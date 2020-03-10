DROP TABLE IF EXISTS WORKS;

CREATE TABLE WORKS(
id text PRIMARY KEY,
title text,
subtitle text,
-- authors[] text // author role,
-- translated_titles[] text // translated string,
-- subjects[] text,
-- subject_places[] text,
-- subject_times[] text,
-- subject_people[] text,
--description text, #### INSUPPORTER
-- dewey_number[] text,
-- lc_classifications[] text,
first_sentence  text,
-- original_languages[] text // language,
-- other_titles[] text,
first_publish_date text,
-- links[] text // links,
notes text,
cover_edition text -- edition,
-- covers[] text)
)