question_set_dict = {
    
    'question_1' : {
    
        'question' : \
            """Display all shows (include the show title) with a rating more than or equal to 5
        - Which shows from this data had more than 1 season?
        [[ PLEASE NOTE THAT THIS QUESTION HAS BEEN SLIGHTLY MODIFIED 
            because there are no shows with ratings less than or equal to 5 ]]
            """ ,
        
        'query' : \
            """SELECT 
                    sa.title,
                    sa.rating,
                    CASE WHEN sf.season_count > 1 THEN 'True' ELSE 'False' END AS has_more_than_one_season
                FROM 
                    series_average sa
                LEFT JOIN 
                    (SELECT 
                        key, 
                        COUNT(DISTINCT season) AS season_count
                    FROM 
                        seasons_full
                    GROUP BY 
                        key) sf ON sa.code = sf.key
                WHERE sa.rating >= 5;
            """
    },


    'question_2' : {
    
        'question' : \
            """Display the show(s) that have the highest rating count and the lowest rank
        - How many episodes do these shows have?
        - How many seasons do these shows have?
            """ ,
        
        'query' : \
            """--sql
            WITH HighestRatingCount AS (
                SELECT title, "rating count"
                FROM series_average
                WHERE "rating count" = (SELECT MAX(CAST(REPLACE("rating count", ',', '') AS INTEGER)) FROM series_average)
            ),
            LowestRank AS (
                SELECT title, rank
                FROM series_average
                WHERE rank = (SELECT MIN(rank) FROM series_average)
            ),
            EpisodesAndSeasons AS (
                SELECT 
                    s.title,
                    COUNT(DISTINCT e.season) AS "number of seasons",
                    COUNT(*) AS "number of episodes"
                FROM seasons_full s
                JOIN episode_ratings e ON s.key = e.code
                GROUP BY s.title
            )

            SELECT 
                'Highest Rating Count' AS Criteria, 
                h.title AS Shows,
                SUM(e."number of seasons") AS TotalSeasons,
                SUM(e."number of episodes") AS TotalEpisodes
            FROM HighestRatingCount h
            LEFT JOIN EpisodesAndSeasons e ON h.title = e.title

            UNION ALL

            SELECT 
                'Lowest Rank' AS Criteria, 
                l.title AS Shows,
                SUM(e."number of seasons") AS TotalSeasons,
                SUM(e."number of episodes") AS TotalEpisodes
            FROM LowestRank l
            LEFT JOIN EpisodesAndSeasons e ON l.title = e.title;
            """
    },
    
    
    'question_3' : {
    
        'question' : \
            """Display the show(s) that have the lowest rating count and the highest rank
        - How many episodes do these shows have?
        - How many seasons do these shows have?
            """ ,
        
        'query' : \
            """--sql
            WITH LowestRatingCount AS (
                SELECT title, "rating count"
                FROM series_average
                WHERE "rating count" = (SELECT MIN(CAST(REPLACE("rating count", ',', '') AS INTEGER)) FROM series_average)
            ),
            HighestRank AS (
                SELECT title, rank
                FROM series_average
                WHERE rank = (SELECT MAX(rank) FROM series_average)
            ),
            EpisodesAndSeasons AS (
                SELECT 
                    s.title,
                    COUNT(DISTINCT e.season) AS "number of seasons",
                    COUNT(*) AS "number of episodes"
                FROM seasons_full s
                JOIN episode_ratings e ON s.key = e.code
                GROUP BY s.title
            )

            SELECT 
                'Lowest Rating Count' AS Criteria, 
                l.title AS Show,
                e."number of seasons" AS TotalSeasons,
                e."number of episodes" AS TotalEpisodes
            FROM LowestRatingCount l
            LEFT JOIN EpisodesAndSeasons e ON l.title = e.title

            UNION ALL

            SELECT 
                'Highest Rank' AS Criteria, 
                h.title AS Show,
                e."number of seasons" AS TotalSeasons,
                e."number of episodes" AS TotalEpisodes
            FROM HighestRank h
            LEFT JOIN EpisodesAndSeasons e ON h.title = e.title;
            """
    }
    
}