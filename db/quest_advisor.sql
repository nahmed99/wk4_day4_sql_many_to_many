DROP TABLE visits;
DROP TABLE users;
DROP TABLE locations;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE locations (
  id SERIAL PRIMARY KEY,
  category VARCHAR(255),
  name VARCHAR(255)
);

-- Data type of 'TEXT' is a long string of text than varchar(255)
-- ON DELETE CASCADE is to ensure no records are left orphaned - referential inegrity.
CREATE TABLE visits (
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id) ON DELETE CASCADE,
  location_id INT REFERENCES locations(id) ON DELETE CASCADE,
  review TEXT
);
