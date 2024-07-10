-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 09, 2024 at 01:31 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codebuster`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(15) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `email`, `phone_num`, `msg`, `date`) VALUES
(1, 'First post', 'first.post@gmail.com', '1234567890', 'I am new to db', '2023-09-21 17:51:55'),
(2, 'myname', 'myname@gmail.com', '1234567890', 'test text', '2023-09-22 14:12:09'),
(3, 'secondname', 'secondname@gmail.com', '9876543210', 'text test', '2023-09-22 14:35:55'),
(4, 'secondname', 'secondname@gmail.com', '9876543210', 'tezt', '2023-09-22 14:36:55'),
(5, 'testname', 'testname@gmail.com', '6549873210', 'doesn\'t matter', '2023-09-22 14:39:52');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `subheading` text NOT NULL,
  `tagline` text NOT NULL,
  `slug` text NOT NULL,
  `content` text NOT NULL,
  `img_file` varchar(25) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `subheading`, `tagline`, `slug`, `content`, `img_file`, `date`) VALUES
(1, 'My first post!', 'Stocks/Shares', 'About stocks ', 'first-post', 'Plain and simple, stock is a share in the ownership of a company. Stock represents a claim on the company\'s assets and earnings. As you acquire more stock, your ownership stake in the company becomes greater. Whether you say shares, equity, or stock, it all means the same thing.', 'post-bg.jpg', '2024-07-04 00:33:55'),
(2, 'Second post', 'ChatGPT', 'About ChatGPT', 'second-post', 'Chat-GPT, which stands for Chat Generative trained Transformer, is a large language model–based chatbot developed by Open-AI and launched on November 30, 2022, which enables users to refine and steer a conversation towards a desired length, format, style, level of detail, and language used. Successive prompts and replies, known as prompt engineering, are considered at each conversation stage as a context.[', 'post-sample-image.jpg', '2024-07-04 00:08:10'),
(3, 'Science', 'Space exploration', 'India and Space', 'post-3', 'On 18 November 2008, the Moon Impact probe was released from Chandrayaan-1 at a height of 100 km (62 mi). During its 25-minute descent, Chandra\'s Altitudinal Composition Explorer (CHACE) recorded evidence of water in 650 mass spectra readings gathered during this time.[33] On 24 September 2009 Science journal reported that the Chandrayaan-1 had detected water ice on the Moon.[34]\r\n\r\nChandrayaan-2 was launched on 22 July 2019. It was a partial success: The team wanted to send an additional lander with rover Vikram with the original orbiter in it, to mark India\'s terrestrial presence on Moon, but the signal connection was lost about 2.1 km (1.3 mi) above the lunar surface. Over several months team tried to resume contact with lander, but ended up with no success. Later, by the late February 2020, it was claimed that an Indian software engineer from Chennai living in USA studied the NASA data of the proposed crashed site and found the Lander.\r\n\r\nChandrayaan-3 is a next planned mission of sending only the lander with rover inside on the Moon, with the Japan\'s JAXA. It was delayed due to COVID-19 pandemic', 'mars.jpg', '2024-07-05 14:44:08');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
