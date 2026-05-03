CREATE DATABASE music_analytics_portfolio;

USE music_analytics_portfolio;

CREATE TABLE artists (
    artist_id INT PRIMARY KEY,
    artist_name VARCHAR(100),
    country VARCHAR(100),
    main_genre VARCHAR(100)
);

CREATE TABLE songs (
    song_id INT PRIMARY KEY,
    song_title VARCHAR(100),
    artist_id INT,
    release_year INT,
    song_genre VARCHAR(100),
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
);

CREATE TABLE streaming_stats (
    stat_id INT PRIMARY KEY,
    song_id INT,
    platform VARCHAR(100),
    country VARCHAR(100),
    streams INT,
    unique_listeners INT,
    saves INT,
    skips INT,
    completed_plays INT,
    playlist_streams INT,
    playlist_reach INT,
    FOREIGN KEY (song_id) REFERENCES songs(song_id)
);

INSERT INTO artists 
(artist_id, artist_name, country, main_genre)
VALUES
(1, 'Rema', 'Nigeria', 'Afrobeats'),
(2, 'Asake', 'Nigeria', 'Amapiano-Fuji'),
(3, 'Ayra Starr', 'Nigeria', 'Afropop'),
(4, 'Omah Lay', 'Nigeria', 'Afro-fusion'),
(5, 'Burna Boy', 'Nigeria', 'Afrofusion');

INSERT INTO songs 
(song_id, song_title, artist_id, release_year, song_genre)
VALUES
(101, 'Calm Rise', 1, 2026, 'Afrobeats'),
(102, 'Lagos Nights', 2, 2026, 'Amapiano-Fuji'),
(103, 'Rush Again', 3, 2026, 'Afropop'),
(104, 'Soft Life', 4, 2026, 'Afro-fusion'),
(105, 'City Boys II', 5, 2026, 'Afrofusion');

INSERT INTO streaming_stats 
(stat_id, song_id, platform, country, streams, unique_listeners, saves, skips, completed_plays, playlist_streams, playlist_reach)
VALUES
(1, 101, 'Spotify', 'Nigeria', 750000, 400000, 60000, 90000, 570000, 180000, 900000),
(2, 102, 'Spotify', 'Nigeria', 600000, 310000, 55000, 72000, 450000, 210000, 1200000),
(3, 103, 'Spotify', 'Nigeria', 700000, 280000, 84000, 56000, 595000, 175000, 700000),
(4, 104, 'Spotify', 'Nigeria', 360000, 250000, 20000, 70000, 230000, 60000, 400000),
(5, 105, 'Spotify', 'Nigeria', 850000, 500000, 75000, 110000, 650000, 300000, 1500000);

-- Query 1: Rank songs by total streams
SELECT
    s.song_title,
    a.artist_name,
    st.streams
FROM streaming_stats st
JOIN songs s
    ON st.song_id = s.song_id
JOIN artists a
    ON s.artist_id = a.artist_id
ORDER BY st.streams DESC;

-- Query 2: Calculate music KPIs
SELECT
    s.song_title,
    a.artist_name,
    st.platform,
    st.country,
    st.streams,
    st.unique_listeners,
    ROUND(st.streams * 1.0 / st.unique_listeners, 2) AS streams_per_listener,
    ROUND(st.saves * 100.0 / st.unique_listeners, 2) AS save_rate_percent,
    ROUND(st.skips * 100.0 / st.streams, 2) AS skip_rate_percent,
    ROUND(st.completed_plays * 100.0 / st.streams, 2) AS completion_rate_percent,
    ROUND(st.playlist_streams * 100.0 / st.playlist_reach, 2) AS playlist_conversion_percent
FROM streaming_stats st
JOIN songs s
    ON st.song_id = s.song_id
JOIN artists a
    ON s.artist_id = a.artist_id
ORDER BY save_rate_percent DESC;

-- Query 3: Find investment-ready songs
SELECT
    s.song_title,
    a.artist_name,
    ROUND(st.saves * 100.0 / st.unique_listeners, 2) AS save_rate_percent,
    ROUND(st.skips * 100.0 / st.streams, 2) AS skip_rate_percent,
    ROUND(st.completed_plays * 100.0 / st.streams, 2) AS completion_rate_percent
FROM streaming_stats st
JOIN songs s
    ON st.song_id = s.song_id
JOIN artists a
    ON s.artist_id = a.artist_id
WHERE 
    (st.saves * 100.0 / st.unique_listeners) > 20
    AND (st.skips * 100.0 / st.streams) < 10
    AND (st.completed_plays * 100.0 / st.streams) > 80;

-- Query 4: Total streams by artist
SELECT
    a.artist_name,
    SUM(st.streams) AS total_streams
FROM streaming_stats st
JOIN songs s
    ON st.song_id = s.song_id
JOIN artists a
    ON s.artist_id = a.artist_id
GROUP BY a.artist_name
ORDER BY total_streams DESC;

-- Query 5: Average save rate by genre
SELECT
    s.song_genre,
    ROUND(AVG(st.saves * 100.0 / st.unique_listeners), 2) AS avg_save_rate_percent
FROM streaming_stats st
JOIN songs s
    ON st.song_id = s.song_id
GROUP BY s.song_genre
ORDER BY avg_save_rate_percent DESC;
