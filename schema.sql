DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS domains;
DROP TABLE IF EXISTS subdomains;
DROP TABLE IF EXISTS ip_addresses;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE domains (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE subdomains (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    domain_id INTEGER,
    FOREIGN KEY (domain_id) REFERENCES domains(id)
);

CREATE TABLE ip_addresses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    address TEXT NOT NULL,
    subdomain_id INTEGER,
    FOREIGN KEY (subdomain_id) REFERENCES subdomains(id)
);


INSERT INTO user (username, password) VALUES ('admin', 'scrypt:32768:8:1$UmKDPSt2rzrn6B1k$88827de5daf879f176e01ee08a16f2e83e58cddc1c056bf41ad57a828ed1c635550746b62c20086b15715522ca1a0e2db2bea5bb76fff771dbd804f5094b8347');
