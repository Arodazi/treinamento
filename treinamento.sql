-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 27-Fev-2021 às 21:17
-- Versão do servidor: 5.7.31
-- versão do PHP: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `treinamento`
--

CREATE DATABASE treinamento;
USE treinamento

-- --------------------------------------------------------

--
-- Estrutura da tabela `alunos_etapa01`
--

DROP TABLE IF EXISTS `alunos_etapa01`;
CREATE TABLE IF NOT EXISTS `alunos_etapa01` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_aluno` int(11) DEFAULT NULL,
  `id_salas` int(11) DEFAULT NULL,
  `id_espacos` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_aluno` (`id_aluno`),
  KEY `id_salas` (`id_salas`),
  KEY `id_espacos` (`id_espacos`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `alunos_etapa01`
--

INSERT INTO `alunos_etapa01` (`id`, `id_aluno`, `id_salas`, `id_espacos`) VALUES
(1, 1, 1, 1),
(2, 2, 1, 1),
(3, 3, 1, 1),
(4, 4, 1, 1),
(5, 5, 1, 1),
(6, 6, 1, 1),
(7, 7, 2, 2),
(8, 8, 2, 2),
(9, 9, 2, 2),
(10, 10, 2, 2),
(11, 11, 2, 2),
(12, 12, 2, 2),
(13, 13, 3, 3),
(14, 14, 3, 3),
(15, 15, 3, 3),
(16, 16, 3, 3),
(17, 17, 3, 3);

-- --------------------------------------------------------

--
-- Estrutura da tabela `alunos_etapa02`
--

DROP TABLE IF EXISTS `alunos_etapa02`;
CREATE TABLE IF NOT EXISTS `alunos_etapa02` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_aluno` int(11) DEFAULT NULL,
  `id_salas` int(11) DEFAULT NULL,
  `id_espacos` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_aluno` (`id_aluno`),
  KEY `id_salas` (`id_salas`),
  KEY `id_espacos` (`id_espacos`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `alunos_etapa02`
--

INSERT INTO `alunos_etapa02` (`id`, `id_aluno`, `id_salas`, `id_espacos`) VALUES
(1, 1, 3, 3),
(2, 2, 3, 3),
(3, 3, 3, 3),
(4, 4, 1, 1),
(5, 5, 1, 1),
(6, 6, 1, 1),
(7, 7, 1, 1),
(8, 8, 1, 1),
(9, 9, 1, 1),
(10, 10, 2, 2),
(11, 11, 2, 2),
(12, 12, 2, 2),
(13, 13, 2, 2),
(14, 14, 2, 2),
(15, 15, 2, 2),
(16, 16, 3, 3),
(17, 17, 3, 3);

-- --------------------------------------------------------

--
-- Estrutura da tabela `espacos`
--

DROP TABLE IF EXISTS `espacos`;
CREATE TABLE IF NOT EXISTS `espacos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) DEFAULT NULL,
  `lotacao` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `espacos`
--

INSERT INTO `espacos` (`id`, `nome`, `lotacao`) VALUES
(1, 'cafe', 50),
(2, 'cha', 15),
(3, 'suco', 10);

-- --------------------------------------------------------

--
-- Estrutura da tabela `pessoas`
--

DROP TABLE IF EXISTS `pessoas`;
CREATE TABLE IF NOT EXISTS `pessoas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) DEFAULT NULL,
  `sobrenome` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `pessoas`
--

INSERT INTO `pessoas` (`id`, `nome`, `sobrenome`) VALUES
(1, 'Izadora', 'Borges'),
(2, 'Denise', 'Vargas'),
(3, 'Elisa ', 'Borges'),
(4, 'Laura', 'Vargas'),
(5, 'Barbara', 'Vargas'),
(6, 'Maria', 'da Silva'),
(7, 'Harry', 'Potter'),
(8, 'Hermione', 'Granger'),
(9, 'Ron', 'Weasley'),
(10, 'Alvo', 'Dumbledore'),
(11, 'Tom', 'Marvolo Riddle'),
(12, 'Erica', 'Schweigert'),
(13, 'Minerva', 'McGonagall'),
(14, 'Lily', 'Evans'),
(15, 'Bellatrix', 'Lestrange'),
(16, 'Luna', 'Lovegood'),
(17, 'Draco', 'Malfoy');

-- --------------------------------------------------------

--
-- Estrutura da tabela `salas`
--

DROP TABLE IF EXISTS `salas`;
CREATE TABLE IF NOT EXISTS `salas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) DEFAULT NULL,
  `lotacao` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `salas`
--

INSERT INTO `salas` (`id`, `nome`, `lotacao`) VALUES
(1, 'banana', 10),
(2, 'uva', 10),
(3, 'laranja', 10);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
