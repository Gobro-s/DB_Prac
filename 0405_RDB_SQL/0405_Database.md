## INDEX
1. 데이터의 시대
2. 데이터베이스
3. 관계형 데이터베이스
4. DBMS
5. SQL

---
## 1. 데이터의 시대
###### 데이터 : **저장**이나 **처리**에 효율적인 형태로 변환된 정보
### 무한하게 증가하는 데이터
- 매일 초당 2억개의 메일 전송되며 3만명이 넷플릭스를 시청
- 배달의 민족 월평균 주문 약 6천만건(2020)
- 전세계 모든 데이터의 약 90%는 2015년 이후 생산된 것(IBM)
- "2025년 전세계 데이터 생성량 175 ZB에 이를 것" (Seagate 2017)
- 우리는 매 순간 데이터를 생성해 내고 있고 무한하게 증가하는 데이터를  "잘" 저장하고 관리하는 기술이 필요

### 파일을 이용한 데이터 관리
- 우리는 일반적으로 데이터를 파일에 저장
- 장점
	- 운영체제에 관계 없이 어디에서나 쉽게 사용 가능
	- 이메일이나 메신저를 이용해 간편하게 전송 가능
- 단점
	- 성능과 보안적 측면에서 한계가 명확
	- 대용량 데이터를 다루기에 적합하지 않음
	- 데이터를 구조적으로 정리하기에 어려움
	- 확장이 불가능한 구조

### 표(스프레드시트)를 이용한 데이터 관리
- 스프레드 시트(엑셀 시트)을 사용
- 컬럼(열)을 통해 데이터의 유형을 지정하고 레코드(행)을 통해 구체적인 데이터 값을 포함
- 무한하게 커질 수 없음
- 데이터 보안 측면, 무결성 측면에서의 단점

---
## 2. 데이터베이스
###### 정보들이 잘 조직화 된 데이터 모음
###### "A database is an organized collection of data"

#### DBMS : 데이터베이스를 조작하는 프로그램.
- 데이터를 모으고 꺼내쓰기 용이한 software

### 데이터베이스
#### 데이터베이스의 종류
- SQL (관계형 데이터베이스) vs NoSQL (비관계형 데이터베이스)

#### 관계형 데이터베이스
- 표 형식으로 된 데이터베이스

#### 비관계형 데이터베이스
- NoSQL 의 No는 "No"가 아닌 "Not only"
- 관계형 데이터베이스의 한계(형식의 제한 , 관계 표현 의무, 추후 수정 및 확장이 어려움)를 극복하기 위해 조금 더 유연한 데이터베이스
- 실제로 많이 쓰이는 데이터베이스로, **서브 데이터베이스**로 두고 **빠른 처리, 확장**이 필요한 기능에서 사용하는 경우가 많음
- 채팅, 소셜 관계, 실시간 사진, 메신저 처리, 실시간 추천 등
- 일반적으로 메인 데이터베이스는 역사와 전통의 관계형 데이터베이스를 사용

#### 데이터베이스 시작하기
- 데이터베이스를 조작하는 언어 : SQL(Structured Query Language)

---
## 3. 관계형 데이터베이스
- 우리가 사용하는 서비스는 결국 데이터베이스를 사용한 CRUD의 반복
	- 회원가입 및 탈퇴( C와 D)
	- 프로필 조회 및 수정 (R 과 U)
	- 새로운 피드 작성 (C)
	- 좋아요 및 팔로우( C D 와 C D)
	- 등등....
	- 결국 CRUD

### 관계형 데이터베이스
#### 관계형 데이터베이스(RDB)
- 데이터를 테이블, 행, 열 등으로 나누어 구조화하는 방식
- 구조화해서 저장하므로 보다 체계적으로 데이터를 저장하고 관리할 수 있음
- 자료를 여러 테이블로 나누어서 관리하고, 테이블간 관계를 설정해 여러 데이터를 조작할 수 있음
- 데이터의 무결성(정확성, 일관성)유지에 장점이 있음
- SQL을 사용하여 데이터를 조회하고 조작

#### 관계형 데이터베이스의 구조
1. 스키마
2. 테이블
	1. 필드
	2. 레코드
	3. 기본 키

#### 1. 스키마(Schema)
- 테이블의 구조(Structure)
- 데이터베이스에서 자료의 구조, 표현 방법, 관계 등 전반적인 명세를 기술한 것

#### 2. 테이블(Table) (Relation)
- 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
- 관계(Relation)라고도 부름
1. 필드(field)
	1. 속성, 컬럼(Column)
2. 레코드(record)
		1. 튜플, 행(Row)
![[Table.png]]

#### 필드(Field) (Column, Attribute)
- 속성 혹은 컬럼(column)
- 각 필드에는 고유한 데이터 형식(타입)이 지정됨

#### 레코드(Record) (Row, Tuple)
- 튜플 혹은 행(row)
- 테이블의 데이터는 레코드에 저장됨

#### PK(Primary Key)
- 기본 키
- 각 레코드의 고유한 값
	- **각각의 데이터를 구분할 수 있는 고유의 값**
- 기술적으로 다른 항목과 절대로 중복될 수 없는 단일 값(unique)
- 데이터베이스 관리 및 테이블 간 관계 설정 시 주요하게 활용

#### FK(Foreign Key)
- 외래 키
- 한 테이블의 속성 중 **다른 테이블의 레코드를 식별할 수 있는 키**(보통 다른테이블의 PK값을 설정)
- 다른 테이블의 기본 키를 참조
- 참조하는 테이블의 속성 1개의 값은, 참조되는 측 테이블의 레코드 값에 대응됨
- 각 레코드에서 서로 다른 테이블 간의 관계를 만드는 데 사용할 수 있음

#### DBMS
데이터베이스를 쉽게 조작할 수 있게 해주는 소프트웨어

---
## 5. SQL
###### SQL(Structured Query Language)
- 관계형 데이터베이스에서 데이터를 관리하기 위해 사용하는 언어
	- **== 데이터베이스 관리 + CRUD 하는 언어**

### SQL Commands
#### SQL Commands 종류
- 명령어는 특성에 따라 다음 세 가지 그룹으로 분류
	1. DDL (Data Definition Language)
		1. 테이블 정의에 관한 명령어
	2. DML (Data Manipulation Language)
		1. 데이터 조작(수정 및 삭제)에 관한 명령어
	3. DCL (Data Control Language)
		1. 데이터베이스 조작(권한 설정, 접근 제어)에 관한 명령어

|분류|개념|SQL 키워드|
|---|---|---|
|DDL - 데이터 정의 언어|관계형 데이터베이스 구조(테이블, 스키마)를 정의(생성, 수정 및 삭제)하기 위한 명령어|CREATE, DROP, ALTER|
|DML - 데이터 조작 언어| 데이터를 조작(추가, 조회, 변경, 삭제)하기 위한 명령어|INSERT, SELECT, UPDATE, DELETE|
|DCL - 데이터 제어 언어| 데이터의 보안, 수행제어, 사용자 권한 부여 등을 정의하기 위한 명령어|GRANT, REVOKE, COMMIT, ROLLBACK|
*SQLite는 파일로 관리되는 DB이기 때문에 SQL을  이용한 접근 제한이 아닌 운영 체제의 파일 접근 권한으로만 제어 가능, SQLite에는 권한 설정을 담당하는 GRANT(권한 부여)와 REVOKE(권한 회수)는 지원하지 않아 DCL 부분은 우선 생략하고 학습한다.*

### SQL Syntax
```sql
-- SQL Syntax 예시

SELECT column_name FROM table_name;
```
- 모든 SQL 문 (statement)는 SELECT, INSERT, UPDATE 등과 같은 키워드로 시작하고, 하나의 statement는 **세미콜론(;)**으로 끝남
	- 세미콜론은 각 SQL문을 구분하는 표준 방법
- SQL 키워드는 대소문자를 구분하지 않음
	- 즉, SELECT == select
	- 하지만 대문자로 작성하는 것이 권장
- SQL에 대한 세부적인 문법 사항들은 DDL, DML을 진행하며 익혀본다.

[참고] Statement & Clause
- Statement(문)
	- 독립적으로 실행할 수 있는 완전한 코드 조각
	- statement는 clasue로 구성됨
- Clause(절)
	- statement의 하위 단위
```sql
SELECT column_name FROM table_name;
```
- SELECT statement라 부름
- 이 statement는 다음과 같이 2개의 clause로 구성 됨
	- SELECT column_name
	- FROM table_name

---
## DDL
- 사전 준비
	- SQLite3설치 (공용문서참조)
	- VScode SQLite 확장 프로그램 설치 확인
	- C드라이브에 SQLite3 폴더 생성 후 SQLite3 파일 복 붙
	- 바탕화면에서 VScode로 .bashrc 파일 생성 후 **alias sqlite3="winpty sqlite3"** 작성
	- 시스템 환경 변수 편집 에서 환경 변수-시스템변수-path-새로만들기-**C:\\sqlite" 작성
	- bash 창에서 sqlite3 입력시 sqlite> 나오면 완료 (안되면 winpty sqlite3 입력)
- 이후 준비
	1. 데이터베이스 mydb.sqlite3 파일 생성 {파일명은 자유}
	2. DDL.sql 파일 생성 {파일명은 자유}
	3. vscode 실행 후 DDL.sql 화면에서 마우스 우측 버튼 클릭
		1. Use Database 선택 
		2. 데이터베이스 목록에서 mydb.sqlite3 선택

### CREATE TABLE
#### CREATE TABLE statement
- "Create a new table in the database."
- 데이터베이스에 새 테이블을 만듦
```SQL
/*
CREATE TABLE table_name(
  column_1 data_type constraints,
  column_2 data_type constraints,
  column_3 data_type constraints
)*/

--예시

--DDL.sql
CREATE TABLE contacts(
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE
);
```
- Query 실행하기
	- 실행하고자 하는 명령문에 커서를 두고 마우스 우측 버튼
	- "Run Selected Query" 선택
	- 명령문을 모두 선택 할 필요 없으며, 실행하고자 하는 명령문 안에 커서가 올라가 있으면 가능
	- 쿼리 실행 후 테이블 및 스키마 확인
	- ![[스키마확인.png]]

### SQLite Data Types
#### Data Types 종류
1. NULL
	1. NULL value
	2. 정보가 없거나 알 수 없음을 의미(missing information or unknown)
2. INTEGER
	1. 정수
	2. 크기에 따라 0, 1, 2, 3, 4, 5, 6 또는 8바이트와 같은 가변 크기를 가짐
3. REAL
	1. 실수
	2. 8바이트 부동 소수점을 사용하는 10진수 값이 있는 실수
4. TEXT
	1. 문자 데이터
5. BLOB(Binary Large Object)
	1. 입력된 그대로 저장된 데이터 덩어리(대용 타입 없음)
	2. 바이너리 등 멀티미디어 파일
	3. 예시
		1. 이미지 데이터
[참고] Boolean type
- SQLite에는 별도의 Boolean 타입이 없음
- 대신 Boolean 값은 정수 0(false)과 1(true)로 저장됨

#### Type Affinity (읽어보기)
- 타입 선호도
- 특정 컬럼에 저장된 데이터에 권장되는 타입
- 데이터 타입 작성 시 SQLite의 5가지 데이터 타입이 아닌 다른 데이터 타입을 선언한다면, 내부적으로 각 타입의 지정된 선호도에 따라 5가지 선호도로 인식 됨
	1. INTEGER
	2. TEXT
	3. BLOB
	4. REAL
	5. NUMERIC
![[Type Affinity.png]]
외울 필요 없다~
- 타입 선호도 존재 이유
	- 다른 데이터베이스 엔진 간의 호환성을 최대화
	- 정적이고 엄격한 타입을 사용하는 데이터베이스의 SQL문을 SQLite에서도 작동하도록 하기 위함

#### Constraints
- "제약조건"
- 입력하는 자료에 대해 제약을 정함
- 제약에 맞지 않다면 입력이 거부됨
- 사용자가 원하는 조건의 데이터만 유지하기 위한 즉, 데이터의 무결성을 유지하기 위한 보편적인 방법으로 테이블의 특정 컬럼에 설정하는 제약
- 이를 통해 데이터 무결성 설정 가능
1. NOT NULL
	1. 컬럼이 NULL 값을 허용하지 않도록 지정
	2. 기본적으로 테이블의 모든 컬럼은 NOT NULL 제약 조건을 명시적으로 사용하는 경우를 제외하고는 NULL 값을 허용함
2. UNIQUE
	1. 컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록 함
	2. PK(유일키)랑 다른거임
3. PRIMARY KEY
	1. 테이블에서 행의 고유성을 식별하는 데 사용되는 컬럼
	2. 각 테이블에는 하나의 기본키만 있음
	3. 함시적으로 NOT NULL 제약조건이 포함되어 있다.
	4. **INTEGER 타입에만 사용 가능**
	5. 예시
```sql
CREATE TABLE table_name(
  id INTEGER PRIMARY KEY,
)
```
4. AUTOINCREMENT
	1. 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지
	2. INTEGER PRIMARY KEY 다음에 작성하면 해당 rowid를 다시 재사용하지 못하도록 함
	3. Django에서 테이블 생성 시 id컬럼에 기본적으로 사용하는 제약 조건
	4. 예시
```sql
CREATE TABLE table_name(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
)
```
5. 기타 Constraints

#### rowid의 특징
- 테이블을 생성할 때마다 rowid라는 암시적 자동 증가 컬럼이 자동으로 생성됨
- 테이블의 행을 고유하게 식별하는 64비트 부호 있는 정수 값
- 테이블에 새 행을 삽입할 때마다 정수 값을 자동으로 할당
	- 값은 1에서 시작
	- 데이터 삽입 시에 rowid 또는 INTEGER PRIMARY KEY 컬럼에 명시적으로 값이 지정되지 않은 경우, SQLite는 테이블에서 가장 큰 rowid보다 하나 큰 다음 순차 정수를 자동으로 할당(AUTOINCREMENT와 관계 없이)
- 만약 INTEGER PRIMARY KEY 키워드를 가진 컬럼을 직접 만들면 이 컬럼은 rowid 컬럼의 별칭(alias)이 됨
	- 즉, 새 컬럼 이름으로 rowid에 액세스 할 수 있으며 rowid 이름으로도 여전히 액세스 가능
- 데이터가 최대 값에 도달하고 새 행을 삽입하려고 하면 SQLite는 사용되지 않는 정수를 찾아 사용(Limits in SQLite - [https://www.sqlite.org/limits.html](https://www.sqlite.org/limits.html)
- 만약 SQLite가 사용되지 않은 정수를 찾을 수 없으면 SQLITE_FULL 에러가 발생
	- 또한 일부 행을 삭제하고 새 행을 삽입하면 SQLite는 삭제된 행에서 rowid 값을 재사용하려고 시도

---
## ALTER TABLE
- "Modify the structure of an existing table"
- 기존 테이블의 구조를 수정(변경)
- SQLite의 ALTER TABLE 문을 사용하면 기존 테이블을 다음과 같이 변경 가능
	1. *Rename* a table
	2. *Rename* a column
	3. *Add* a new column to a table
	4. *Delete* a column
- (https://www.sqlite.org/lang_altertable.html) 참조

명령어 이것저것 실습
#### DDL 정리
- "데이터 정의 언어"
- CREATE TABLE
	- 데이터 타입과 제약 조건
- ALTER TABLE
	- RENAME
	- RENAME COLUMN
	- ADD COLUMN
	- DROP COLUMN
- DROP TABLE

---
## DML
- 테이블에 해당 csv 파일 데이터를 import 해서 사용
- DML을 통해 데이터를 조작하기(CRUD)
- INSERT, SELECT, UPDATE, DELETE
- '' * '' means 전부 다!

-> 158p 까지 실습.