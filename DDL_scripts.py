# DDL statements for creating tables
ddl_query__series_average = """--sql
CREATE TABLE series_average (
    code TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    rating DECIMAL,
    "rating count" INTEGER,
    rank INTEGER,
    "rating mean" DECIMAL
);
"""

ddl_query__seasons_full = """--sql
CREATE TABLE seasons_full (
    key TEXT,
    title TEXT,
    season INTEGER,
    "rating mean" DECIMAL,
    "number of episodes" INTEGER,
    FOREIGN KEY(key) REFERENCES "series average"(code)
);
"""

ddl_query__episode_ratings = """--sql
CREATE TABLE episode_ratings (
    season INTEGER,
    episode INTEGER,
    rating DECIMAL,
    code TEXT,
    FOREIGN KEY(code) REFERENCES "series average"(code)
);
"""

