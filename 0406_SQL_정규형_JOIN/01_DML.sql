-- users table 생성
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

SELECT COUNT(*) FROM users;

SELECT avg(balance) FROM users;

SELECT last_name, COUNT(*) FROM users GROUP BY last_name;

SELECT last_name, COUNT(*) AS number_of_name FROM users GROUP BY last_name;
-- 위는 원본 테이블이 변경 x--

CREATE TABLE classmates (
	name TEXT NOT NULL,
	age INTEGER NOT NULL,
	address TEXT NOT NULL
);

INSERT INTO classmates (name, age, address)
VAlUES ('홍길동', 23, '서울');

INSERT INTO classmates
VALUES ('김똥개', 23, '서울');

INSERT INTO classmates
VALUES
('김철수', 31, '경기'),
('이영미', 30, '강원'),
('박진성', 26, '전라'),
('최지수', 12, '충청'),
('정요한', 28, '경상');

UPDATE classmates
SET name = '김철수한무두루미',
	address = '제주도'
WHERE rowid = 3;

DELETE FROM classmates WHERE rowid = 2;

SELECT rowid, * FROM classmates;

DELETE FROM classmates WHERE rowid = 5;

DELETE FROM classmates;