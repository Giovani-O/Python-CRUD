create database user_py;
use user_py;

create table usuario(
	id int primary key auto_increment not null,
	nome varchar(50) not null,
    idade int not null,
    profissao varchar(50) not null,
    salario double(10,2)
);

insert into usuario(nome, idade, profissao, salario) values ("Katarina", 21, "Software Engineer", 7000.00);
insert into usuario(nome, idade, profissao, salario) values ("Jacob", 19, "Fullstack Developer", 3500.00);

select * from usuario;