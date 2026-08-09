CREATE TABLE IF NOT EXISTS sensor_data (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_type  TEXT,
    raw_value    INTEGER,
    lux          REAL,
    timestamp    DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO sensor_data (sensor_type, raw_value, lux) VALUES ('CDS', 2847, 695.2);
INSERT INTO sensor_data (sensor_type, raw_value, lux) VALUES ('CDS', 1523, 371.9);
INSERT INTO sensor_data (sensor_type, raw_value, lux) VALUES ('CDS', 3891, 950.1);
SELECT * FROM sensor_data;
SELECT AVG(raw_value) as avg_raw FROM sensor_data;
SELECT MAX(raw_value), MIN(raw_value) FROM sensor_data;

