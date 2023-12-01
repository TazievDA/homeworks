CREATE TABLE IF NOT EXISTS Employee(
	employee_id SERIAL PRIMARY KEY,
	name VARCHAR(120) NOT NULL,
	department VARCHAR(60) NOT NULL
);
CREATE TABLE BossEmployee(
	boss_id SERIAL PRIMARY KEY,
	employee_id INTEGER UNIQUE REFERENCES Employee(employee_id)
);
ALTER TABLE Employee ADD boss INTEGER REFERENCES BossEmployee(boss_id);