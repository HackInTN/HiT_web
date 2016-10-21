-- phpMyAdmin SQL Dump
-- version 4.5.0.2deb2
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Sam 24 Octobre 2015 à 11:22
-- Version du serveur :  5.6.25-4
-- Version de PHP :  5.6.14-1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `sql_app`
--

-- --------------------------------------------------------

--
-- Structure de la table `fichier`
--

CREATE TABLE `fichier` (
  `id` int(11) NOT NULL,
  `path` varchar(255) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `idUser` int(11) NOT NULL,
  `idMessage` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `fichier`
--

INSERT INTO `fichier` (`id`, `path`, `nom`, `idUser`, `idMessage`) VALUES
(1, 'user/trololo.jpg\r\n', 'Me', 1, 1),
(2, 'user/chacarron.jpg', 'Me to', 2, 2),
(3, 'admin/flag.jpg', 'The Holy Flag', 3, 3);

-- --------------------------------------------------------

--
-- Structure de la table `message`
--

CREATE TABLE `message` (
  `id` int(11) NOT NULL,
  `idUser` int(11) NOT NULL,
  `message` text NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `message`
--

INSERT INTO `message` (`id`, `idUser`, `message`, `date`) VALUES
(1, 1, 'Song : \r\n<a href="https://www.youtube.com/watch?v=oavMtUWDBTM">https://www.youtube.com/watch?v=oavMtUWDBTM</a>\r\n\r\nLyrics : \r\n\r\nOOOOOOOOOOOOOOOOOOOOOOOOOOWEWAWAAAAAAAAWEWAWAAAAAA\r\nAAAAAAAAWAWAWAAAA\r\nOHOHOHOOOOOOOOOOOOOOOOOOOOOO \r\nOHEWAWAWAWAWAAAAAAAAAAAAAA\r\n\r\nWEWEWEWEWE HOHOHO HOHOHO\r\nWEWEWEWEWE HOHOHO \r\nHOHOHOOOOOOOOOOOOOOOOOOOOOOOOOOOOHOHOHOHOOOOOOOOOO\r\nOOOOOOOOO\r\n\r\nLALALALALALALAAAAAAAAAAAA...\r\nLALALLA LALALAAA LAAAAAAAAAAAAAAAA \r\nLALALAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\r\nA\r\n\r\nLALALALAAAAAAAAAAAAA\r\nLALALALALAAAAAAAAAA\r\nLOLOLOLOOOOOOOOOOOOOOOOOOOOOO LALALALAAAAAAAAAAAAAAAA \r\nLOLAAAAAAAAA OHHOHOHOHOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO OHOHOOHOHO\r\nHOHOHOOOOOOOO\r\nA IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII.. \r\nla lala la la lala lala la la... OLOLOLO \r\nPAPOLOLOPALO HELALOOOOOOOOOOOOOO\r\n\r\nLOLOLOLOLOLOLO... LOLOLOLOLOLO LOLOLOLOLO LOLLLO\r\n\r\nHOHOHOHOHO ! HOHOHOHOHO ! HOHOHOHOHO ! HOHOHOHOHO !\r\nLALALALOLOLAOLOALAOLAALOALAOLOOOOO ! \r\nAAAAAAAAAAAAAAAAAAAAAAH OWOLOOOOOOOOO \r\nLALALOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOLA\r\nALOOOOOO\r\n\r\nOHOHOHOHOOOOOOOOOOOO LALALOOOOOOOOOOOOOOOOOOOOOOOOO \r\nHOOOOOOOOOOOOOWIWOOOOOOO.... LOLOLOLOLOLO OHOHOHOOOOOOOOOOOOOOOOOO...\r\nLOLOLOLOLOLO OOOOOHOHOHOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\r\nOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\r\nOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\r\nOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\r\n! ', '2015-11-20'),
(2, 2, 'Song : \r\n<a href="https://www.youtube.com/watch?v=l12Csc_lW0Q">https://www.youtube.com/watch?v=l12Csc_lW0Q</a>\r\n\r\nLyrics : \r\n\r\nO yea! Sayl Zon jon Macarron.. Yea Maccoron noo...\r\nChaccaron, Chaccaron, Chaccaron, Chaccaron...\r\n\r\n(Chorus:)\r\nObedansosay nonekosay budedai nosai Badereda \r\nnai nosyake sayhoshsai maccaronnosay yakkano no sya madanunosai\r\n\r\n(Verse 1:)\r\nChaccaron Chaccaron nadoneyydadon Chaccaron \r\nChaccaron nadoneyydadon Chaccaroneydagodon nadoneyydadon \r\nChaccaron Chaccaron nadoneyydadon\r\n\r\n\r\n(Chorus:)\r\nObedansosay nonekosay budedai no sayk Badereda nai \r\nnosyake sayhoshsai maccaronnosay yakkano no sya madanunosai\r\n\r\n\r\n(Verse 2:)\r\nChaccaron Chaccaron nadoneyydadon Chaccaron Chaccaron \r\nnadoneyydadon Chaccaroneydagodon nadoneyydagodon \r\nChaccaron Chaccaron nadoneyydadon\r\n\r\n(Break 1:)\r\nChaccaron, Chaccaron, Chaccaron, Chaccaron...\r\n\r\n(Chorus:)\r\nObedansosay nonekosay budedai no sayk Badereda nai \r\nnosyake sayhoshsai maccaronnosay yakkano no sya madanunosai\r\n\r\n(Wierd part 1:)\r\nBukadandudan Bukadandando Bukadandudandandandanna \r\nChaccaron bukabandado bukandangago... eyakudo badabidakon \r\nbutabutadon beatdapadadadatina chaccaron budadadukai \r\nbenna dudaflow... ebedo bada biko dudaflow\r\n\r\n(Verse 3:)\r\nChaccaron Chaccaron nadoneyydadon Chaccaron Chaccaron nadoneyydadon\r\n\r\n(Chorus:)\r\nObedansosay nonekosay budedai no sayk Badereda nai \r\nnosyake sayhoshsai maccaronnosay yakkano no sya madanunosai\r\n\r\n(Verse 3:)\r\nChaccaron Chaccaron nadoneyydadon Chaccaroneydagodon \r\nnadoneyydagodony dakadundadga\r\n\r\n(Break 2:)\r\nChaccaron, Chaccaron, Chaccaron, Chaccaron...\r\n\r\n(Chorus:)\r\nObedansosay nonekosay budedai no sayk Badereda nai nosyake \r\nsayhoshsai maccaronnosay yakkano no sya madanunosai\r\n\r\n(Verse 4:)\r\nChaccaron Chaccaron nadoneyydadon Chaccaron Chaccaron \r\nnadoneyydadon Chaccaroneydagodon nadoneyydadon Chaccaron \r\nChaccaron nadoneyydadon\r\n\r\n(Chorus:)\r\nObedansosay nonekosay budedai no sayk Badereda nai nosyake \r\nsayhoshsai maccaronnosay yakkano no sya madanunosai\r\n\r\n(Verse 5:)\r\nChaccaron Chaccaron nadoneyydadon Chaccaron Chaccaron \r\nnadoneyydadon Chaccaroneydagodon nadoneyydadon Chaccaron \r\nChaccaron nadoneyydadon\r\n\r\n(Different break 1:)\r\nChaccaron Chaccaron... Chaccaron Chaccaron... Chaccaron Chaccaron\r\n\r\n(Wierd part 2:)\r\nBukadandudan Bukadandando Bukadandudandandandanna Chaccaron \r\nbukabandado bukandangago... eyakudo badabidakon butabutadon \r\nbeatdapadadadatina chaccaron budadadukai benna dudaflow... \r\nebedo bada biko dudaflow\r\n\r\n(Verse 6:)\r\nChaccaron Chaccaron nadoneyydadon Chaccaron Chaccaron \r\nnadoneyydadon Chaccaroneydagodon nadoneyydadon Chaccaron Chaccaron nadoneyydadon\r\n\r\n(Chorus:)\r\nObedansosay nonekosay budedai no sayk Badereda nai nosyake \r\nsayhoshsai maccaronnosay yakkano no sya madanunosai\r\n\r\n(Ending:)\r\nChaccaron Chaccaron nadoneyydadon Chaccaronydaccaron \r\nChaccaronydaccaron... bichabanpuka', '2015-11-20'),
(3, 3, 'WTF ? \r\nThis is a good song : <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">https://www.youtube.com/watch?v=dQw4w9WgXcQ</a>', '2015-11-20'),
(4, 3, 'Delete Me please...', '1992-07-09');

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `login` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `prenom` varchar(255) NOT NULL,
  `isAdmin` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `user`
--

INSERT INTO `user` (`id`, `login`, `email`, `password`, `nom`, `prenom`, `isAdmin`) VALUES
(1, 'trololo', 'trololo@lololo.lol', 'Trol0l01ol01OL0l01ol', 'guy', 'Trololo', 0),
(2, 'elmundo', 'elmundo@chacarron.lol', 'bukabandadobukabandadobukabandado', 'Mundo', 'El', 0),
(3, 'oldAdmin', 'admin@revoked.lol', 'administatorusleciraptor', 'admin', 'old', 0);

--
-- Index pour les tables exportées
--

--
-- Index pour la table `fichier`
--
ALTER TABLE `fichier`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `message`
--
ALTER TABLE `message`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `login` (`login`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `fichier`
--
ALTER TABLE `fichier`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT pour la table `message`
--
ALTER TABLE `message`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT pour la table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
