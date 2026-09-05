-- =========================================================
-- RouteRover Database Setup
-- Rebuilt from RouteRoverApp.py logic (users + tourist_locations)
-- Run this whole file once to recreate the database.
-- =========================================================

DROP DATABASE IF EXISTS RouteRover;
CREATE DATABASE RouteRover;
USE RouteRover;

-- -------------------------------------------------
-- users table (matches: username, password_hash lookups)
-- -------------------------------------------------
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);

-- Sample login so you can test right away:
--   username: testuser
--   password: password123
-- (hash generated with bcrypt, same library your app uses)
INSERT INTO users (username, password_hash) VALUES
('testuser', '$2b$12$7HCnolbDHXmP9Ez9VQcsVuS3UvGX/Xf8oAuOQkuC5/x24Altmam9.');

-- -------------------------------------------------
-- tourist_locations table
-- Column order matches how the app reads results by index:
-- location[1]=name, location[2]=country, location[3]=city,
-- location[4]=description, location[5]=latitude, location[6]=longitude
-- -------------------------------------------------
CREATE TABLE tourist_locations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    country VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    description TEXT,
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6)
);

INSERT INTO tourist_locations (name, country, city, description, latitude, longitude) VALUES
('Burj Khalifa', 'UAE', 'Dubai', 'The tallest building in the world, offering an observation deck with panoramic views of the city and coastline.', 25.197197, 55.274376),
('Dubai Marina', 'UAE', 'Dubai', 'A modern waterfront district lined with skyscrapers, yachts, and a lively promenade.', 25.080000, 55.140000),
('Sheikh Zayed Grand Mosque', 'UAE', 'Abu Dhabi', 'One of the largest mosques in the world, known for its white marble domes and intricate design.', 24.412796, 54.475011),
('Louvre Abu Dhabi', 'UAE', 'Abu Dhabi', 'An art and civilization museum celebrated for its striking dome that filters light like a "rain of light".', 24.533300, 54.398100),
('Petra', 'Jordan', 'Petra', 'An ancient city carved into rose-colored rock, famous for the Treasury facade and Nabataean history.', 30.328500, 35.444400),
('Wadi Rum', 'Jordan', 'Wadi Rum', 'A vast desert valley of red sand and dramatic sandstone mountains, popular for jeep tours and camping.', 29.576200, 35.420600),
('Amman Citadel', 'Jordan', 'Amman', 'A historic hilltop site with Roman, Byzantine, and Umayyad ruins overlooking the capital.', 31.954400, 35.934200),
('Souq Waqif', 'Qatar', 'Doha', 'A traditional market with narrow alleys, spice stalls, textiles, and lively cafes.', 25.286700, 51.533300),
('The Pearl-Qatar', 'Qatar', 'Doha', 'An artificial island of marinas, upscale shopping, and waterfront dining.', 25.369900, 51.551700),
('Kuwait Towers', 'Kuwait', 'Kuwait City', 'Iconic water towers on the Gulf coastline, a symbol of modern Kuwait.', 29.389700, 48.000000),
('Grand Mosque of Kuwait', 'Kuwait', 'Kuwait City', 'The largest mosque in Kuwait, notable for its grand dome and traditional Islamic architecture.', 29.376900, 47.987800),
('Bahrain Fort', 'Bahrain', 'Manama', 'A UNESCO World Heritage archaeological site with layers of civilization dating back 4,000 years.', 26.228500, 50.522800),
('Manama Souq', 'Bahrain', 'Manama', 'A bustling traditional market known for gold, spices, and textiles near the old harbor.', 26.234000, 50.586000),
('Muttrah Souq', 'Oman', 'Muscat', 'One of the oldest marketplaces in the Arab world, known for frankincense, silver, and textiles.', 23.615000, 58.593700),
('Nizwa Fort', 'Oman', 'Nizwa', 'A 17th-century fort with a massive circular tower, once a center of trade and defense.', 22.933300, 57.533300),
('Masmak Fortress', 'Saudi Arabia', 'Riyadh', 'A clay and mudbrick fort central to the founding of the modern Saudi state.', 24.630800, 46.714100),
('AlUla', 'Saudi Arabia', 'AlUla', 'A historic desert region home to the Nabataean tombs of Hegra, Saudi Arabia''s first UNESCO site.', 26.610000, 37.920000),
('Jeita Grotto', 'Lebanon', 'Jeita', 'A spectacular system of limestone caves with underground chambers and a subterranean river.', 33.942200, 35.645300),
('Baalbek', 'Lebanon', 'Baalbek', 'Ruins of monumental Roman temples, including the Temple of Jupiter, among the best-preserved in the world.', 34.005900, 36.203900),
('Mutanabbi Street', 'Iraq', 'Baghdad', 'A historic street lined with bookstores and outdoor book stalls, long considered the heart of Baghdad''s literary life.', 33.340000, 44.420000);

-- =========================================================
-- Quick sanity check queries (optional, safe to delete)
-- =========================================================
-- SELECT DISTINCT city FROM tourist_locations ORDER BY city;
-- SELECT * FROM tourist_locations WHERE city IN ('Dubai','Abu Dhabi');
