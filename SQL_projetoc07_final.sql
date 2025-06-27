drop schema if exists mydb;
create schema if not exists mydb;
use mydb;
set sql_safe_updates = 0;

-- tabela chef (relacao 1:N com receita, 1:1 com restaurante)
create table if not exists chef ( 
  idchef int not null auto_increment,
  nome varchar(45) not null,
  especialidade varchar(45) not null,
  experiencia varchar(45) not null,
  primary key (idchef)
);

-- tabela restaurante (relacao 1:1 com chef, 1:N com pedido)
create table if not exists restaurante ( 
  idrestaurante int not null auto_increment,
  nome varchar(45) not null,
  endereco varchar(45) not null,
  idchef int not null unique,
  primary key (idrestaurante),
  foreign key (idchef) references chef(idchef)
  on delete cascade
);

-- tabela cliente (relacao 1:N com pedido)
create table if not exists cliente (
  idcliente int not null auto_increment,
  nome varchar(45) not null,
  telefone varchar(45) not null,
  endereco varchar(45) not null,
  email varchar(45) not null,
  senha varchar(45) not null,
  primary key (idcliente)
);

-- tabela produto (relacao N:N com receita)
create table if not exists produto ( 
  idproduto int not null auto_increment,
  tipo varchar(45) not null,
  quantidade varchar(45) not null,
  primary key (idproduto)
);

-- tabela receita (relacao 1:N com chef, N:N com produto)
create table if not exists receita ( -- 
  idreceita int not null auto_increment,
  dificuldade varchar(45) not null,
  nacionalidade varchar(45) not null,
  idchef int not null,
  primary key (idreceita),
  foreign key (idchef) references chef(idchef)
  on delete cascade
);

-- tabela receita_has_produto (relacao n:n)
create table if not exists receita_has_produto ( 
  idreceita int not null,
  idproduto int not null,
  primary key (idreceita, idproduto),
  foreign key (idreceita) references receita(idreceita)
  on delete cascade,
  foreign key (idproduto) references produto(idproduto)
  on delete cascade
);

-- tabela pedido (1:N com cliente, 1:N com restaurante, 1:1 com avaliacao) 
create table if not exists pedido ( 
  idpedido int not null auto_increment,
  precototal float not null,
  pagamento varchar(45) not null,
  idcliente int not null,
  idrestaurante int not null,
  primary key (idpedido),
  foreign key (idcliente) references cliente(idcliente)
  on delete cascade,
  foreign key (idrestaurante) references restaurante(idrestaurante)
  on delete cascade
);

-- tabela avaliacao (relacao 1:1 com pedido)
create table if not exists avaliacao (
  idavaliacao int not null auto_increment,
  nota varchar(45) not null,
  descricao varchar(45),
  idpedido int unique,
  primary key (idavaliacao),
  foreign key (idpedido) references pedido(idpedido)
  on delete cascade
);

-- insercoes
insert into chef (nome, especialidade, experiencia) values ('carlos souza', 'italiana', '10 anos');
insert into chef (nome, especialidade, experiencia) values ('ana lima', 'francesa', '7 anos');

insert into restaurante (nome, endereco, idchef) values ('chips', 'rua das flores, 123', 1);
insert into restaurante (nome, endereco, idchef) values ('toca da raposa', 'av. central, 456', 2);

  insert into cliente (nome, telefone, endereco, email, senha) values ('joao silva', '1111-1111', 'rua a', 'joao@email.com', '1234');
  insert into cliente (nome, telefone, endereco, email, senha) values ('maria oliveira', '2222-2222', 'rua b', 'maria@email.com', '5678');

insert into produto (tipo, quantidade) values ('tomate', '10kg');
insert into produto (tipo, quantidade) values ('queijo', '5kg');

insert into receita (dificuldade, nacionalidade, idchef) values ('media', 'italiana', 1);
insert into receita (dificuldade, nacionalidade, idchef) values ('alta', 'francesa', 2);

insert into receita_has_produto (idreceita, idproduto) values (1, 1);
insert into receita_has_produto (idreceita, idproduto) values (2, 2);

insert into pedido (precototal, pagamento, idcliente, idrestaurante) values (100.0, 'cartao', 1, 1);
insert into pedido (precototal, pagamento, idcliente, idrestaurante) values (150.0, 'dinheiro', 2, 2);

insert into avaliacao (nota, descricao, idpedido) values ('5', 'excelente', 1);
insert into avaliacao (nota, descricao, idpedido) values ('4', 'muito bom', 2);

-- atualizacoes
update chef set experiencia = '11 anos' where nome = 'carlos souza';
update chef set especialidade = 'mediterranea' where nome = 'ana lima';

update restaurante set nome = 'estancia santa rita' where nome = 'toca da raposa';
update restaurante set endereco = 'av. europa, 999' where nome = 'chips';

update cliente set telefone = '9999-9999' where nome = 'joao silva';
update cliente set endereco = 'rua c' where nome = 'maria oliveira';

update produto set quantidade = '12kg' where tipo = 'tomate';
update produto set tipo = 'queijo parmesao' where tipo = 'queijo';

update receita set dificuldade = 'facil' where nacionalidade = 'italiana';
update receita set nacionalidade = 'espanhola' where dificuldade = 'alta';

update pedido set precototal = 110.0 where idpedido = 1;
update pedido set pagamento = 'pix' where idpedido = 2;

update avaliacao set nota = '3' where idavaliacao = 1;
update avaliacao set descricao = 'bom' where idavaliacao = 2;

