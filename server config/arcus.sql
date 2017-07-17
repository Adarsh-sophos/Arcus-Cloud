-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 03, 2017 at 04:13 PM
-- Server version: 5.7.18
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `arcus`
--

-- --------------------------------------------------------

--
-- Table structure for table `iscsi`
--

CREATE TABLE `iscsi` (
  `id` int(10) UNSIGNED NOT NULL,
  `user_id` int(11) NOT NULL,
  `size` int(11) NOT NULL,
  `clientIP` varchar(50) NOT NULL,
  `state` varchar(10) NOT NULL,
  `iqn` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `iscsi`
--

INSERT INTO `iscsi` (`id`, `user_id`, `size`, `clientIP`, `state`, `iqn`) VALUES
(6, 13, 87, '192.168.43.59', 'logout', 'sudologin_final');

-- --------------------------------------------------------

--
-- Table structure for table `nfs`
--

CREATE TABLE `nfs` (
  `id` int(11) UNSIGNED NOT NULL,
  `user_id` int(11) NOT NULL,
  `driveSize` int(11) NOT NULL,
  `clientIP` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `line` int(11) NOT NULL,
  `state` char(1) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `nfs`
--

INSERT INTO `nfs` (`id`, `user_id`, `driveSize`, `clientIP`, `password`, `line`, `state`, `time`) VALUES
(28, 13, 100, '192.168.43.59', 'redhat', 4, 'u', '2017-07-03 12:39:52'),
(29, 13, 100, '192.168.43.59', 'redhat', 5, 'm', '2017-07-03 12:40:15'),
(30, 13, 60, '192.168.43.59', 'redhat', 6, 'm', '2017-07-03 14:14:57');

-- --------------------------------------------------------

--
-- Table structure for table `snapshot`
--

CREATE TABLE `snapshot` (
  `id` int(10) UNSIGNED NOT NULL,
  `nfs_id` int(11) NOT NULL,
  `snap_name` varchar(50) NOT NULL,
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `snapshot`
--

INSERT INTO `snapshot` (`id`, `nfs_id`, `snap_name`, `time`) VALUES
(1, 28, '03-Jul-2017-18-19-34', '2017-07-03 18:19:37'),
(2, 30, '03-Jul-2017-19-45-25', '2017-07-03 19:45:28'),
(3, 30, '03-Jul-2017-19-46-42', '2017-07-03 19:46:47');

-- --------------------------------------------------------

--
-- Table structure for table `snapshot_iscsi`
--

CREATE TABLE `snapshot_iscsi` (
  `id` int(11) NOT NULL,
  `iscsi_id` int(11) NOT NULL,
  `snap_name` varchar(50) NOT NULL,
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `snapshot_iscsi`
--

INSERT INTO `snapshot_iscsi` (`id`, `iscsi_id`, `snap_name`, `time`) VALUES
(1, 6, '03-Jul-2017-19-36-34', '2017-07-03 19:36:38'),
(2, 6, '03-Jul-2017-19-41-31', '2017-07-03 19:41:37');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(10) UNSIGNED NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(13, 'tom', 'tom'),
(14, 'jack', 'kack'),
(15, 'hello', 'hello'),
(16, 'raja', 'raja'),
(17, 'raja123', 'raja123'),
(18, 'rama', 'rama');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `iscsi`
--
ALTER TABLE `iscsi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `nfs`
--
ALTER TABLE `nfs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `snapshot`
--
ALTER TABLE `snapshot`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `snapshot_iscsi`
--
ALTER TABLE `snapshot_iscsi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `iscsi`
--
ALTER TABLE `iscsi`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `nfs`
--
ALTER TABLE `nfs`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
--
-- AUTO_INCREMENT for table `snapshot`
--
ALTER TABLE `snapshot`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `snapshot_iscsi`
--
ALTER TABLE `snapshot_iscsi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
