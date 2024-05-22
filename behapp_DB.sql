-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 15, 2024 at 07:29 PM
-- Server version: 5.7.41
-- PHP Version: 8.1.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vwgroup_behapp1`
--

-- --------------------------------------------------------

--
-- Table structure for table `Assessments`
--

CREATE TABLE `Assessments` (
  `pID` varchar(25) COLLATE utf8_persian_ci NOT NULL,
  `AssessorID` varchar(10) COLLATE utf8_persian_ci NOT NULL,
  `occureDate` varchar(25) COLLATE utf8_persian_ci NOT NULL,
  `occureTime` time NOT NULL,
  `inID` varchar(25) COLLATE utf8_persian_ci NOT NULL,
  `itID` varchar(25) COLLATE utf8_persian_ci NOT NULL,
  `score` varchar(25) COLLATE utf8_persian_ci NOT NULL,
  `status` varchar(20) COLLATE utf8_persian_ci NOT NULL,
  `RecordID` varchar(10) COLLATE utf8_persian_ci NOT NULL,
  `RecordDate` varchar(25) COLLATE utf8_persian_ci NOT NULL,
  `recordTime` time NOT NULL,
  `current` varchar(10) COLLATE utf8_persian_ci NOT NULL,
  `forecastEffectTime` varchar(10) COLLATE utf8_persian_ci NOT NULL,
  `RealEffectTime` varchar(10) COLLATE utf8_persian_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Groups`
--

CREATE TABLE `Groups` (
  `Gcode` varchar(10) COLLATE utf8_persian_ci NOT NULL,
  `Description` varchar(20) COLLATE utf8_persian_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

--
-- Dumping data for table `Groups`
--

INSERT INTO `Groups` (`Gcode`, `Description`) VALUES
('G1', 'پرسنل واحد برق'),
('G2', 'پرسنل واحد مکانیک '),
('G3', 'پرسنل واحد آزمایشگاه'),
('G4', 'پرسنل دفتر فنی'),
('G5', 'G5'),
('G6', 'G6'),
('G7', 'G7'),
('G8', 'G8'),
('G9', 'G9'),
('G10', 'G10'),
('G1000', 'تیم نخبگان'),
('G1100', 'تیم والیبال کارخانه '),
('G1200', 'تیم بررسی مشکلات خط '),
('', ''),
('', ''),
('', ''),
('', '');

-- --------------------------------------------------------

--
-- Table structure for table `GroupsMembers`
--

CREATE TABLE `GroupsMembers` (
  `pID` varchar(10) COLLATE utf8_persian_ci NOT NULL,
  `Gcode` varchar(10) COLLATE utf8_persian_ci NOT NULL,
  `from date` varchar(10) COLLATE utf8_persian_ci NOT NULL,
  `from time` varchar(10) COLLATE utf8_persian_ci NOT NULL,
  `to date` varchar(10) COLLATE utf8_persian_ci NOT NULL,
  `to time` varchar(10) COLLATE utf8_persian_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

--
-- Dumping data for table `GroupsMembers`
--

INSERT INTO `GroupsMembers` (`pID`, `Gcode`, `from date`, `from time`, `to date`, `to time`) VALUES
('کد پرسنلی', 'گروه پرسنل', 'از تاریخ ', 'از ساعت ', 'تا تاریخ ', 'تا ساعت'),
('380101', 'G2', '14020501', '11:20', '', ''),
('380230', 'G1', '14020501', '11:25', '', ''),
('380220', 'G1', '14020501', '11:21', '', ''),
('380235', 'G2', '14020502', '10:20', '', ''),
('380254', 'G3', '14020503', '08:20', '', ''),
('380101', 'G1200', '14020505', '11:20', '', ''),
('380220', 'G1200', '14020506', '11:20', '', ''),
('380400', 'G4', '14020601', '08:10', '', ''),
('', '', '', '', '', ''),
('', '', 'from date', 'from time', 'to date', 'to time');

-- --------------------------------------------------------

--
-- Table structure for table `Indicators`
--

CREATE TABLE `Indicators` (
  `inID` int(10) NOT NULL,
  `ItemType` varchar(30) COLLATE utf8_persian_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

--
-- Dumping data for table `Indicators`
--

INSERT INTO `Indicators` (`inID`, `ItemType`) VALUES
(10, 'حضور و غیاب'),
(15, 'انضباطی'),
(20, 'ایمنی'),
(30, 'مشارکت مثبت'),
(40, 'قوانین'),
(50, 'اخلاق و رفتار'),
(60, 'اموال و ابزار'),
(70, 'آراستگی'),
(80, 'وظایف و مسئولیت ها');

-- --------------------------------------------------------

--
-- Table structure for table `IndicatorsItems`
--

CREATE TABLE `IndicatorsItems` (
  `inID` varchar(10) COLLATE utf8_persian_ci NOT NULL,
  `itID` varchar(10) COLLATE utf8_persian_ci NOT NULL,
  `item` varchar(30) COLLATE utf8_persian_ci NOT NULL,
  `minEffect` varchar(5) COLLATE utf8_persian_ci NOT NULL,
  `defaultEffect` varchar(5) COLLATE utf8_persian_ci NOT NULL,
  `maxEfect` varchar(5) COLLATE utf8_persian_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

--
-- Dumping data for table `IndicatorsItems`
--

INSERT INTO `IndicatorsItems` (`inID`, `itID`, `item`, `minEffect`, `defaultEffect`, `maxEfect`) VALUES
('10', '100', 'عدم حضور بموقع در هنگام شروع ک', '0', '-1', '-3'),
('10', '110', 'ترک کار قبل از زمان پایان کار ', '-1', '-1', '-3'),
('10', '120', 'عدم حضوربدون مرخصی که بعدا مرخ', '0', '-0.2', '-1'),
('10', '130', 'عدم حضور بدون مرخصی که بعدا مر', '0', '-0.5', '-1.5'),
('10', '140', 'غیبت', '-1', '-3', '-6'),
('20', '100', 'عدم رعایت موارد ایمنی فردی', '-1', '-2', '-4'),
('20', '110', 'انجام امور غیر ایمن فردی', '0', '-1', '-4'),
('20', '120', 'انجام امور غیر ایمن و خطر زا ب', '-1', '-3', '-6'),
('20', '130', 'بروز حادثه فردی', '-1', '-2', '-4'),
('20', '140', 'بروز حادثه در قسمت', '0', '-1', '-4'),
('30', '100', 'حل مشکلات قسمت', '1', '2', '5'),
('30', '110', 'خلاقیت و نوآوری در جهت منافع س', '0', '3', '10'),
('30', '120', 'انجام اضافه کاری های لازم', '1', '2', '3'),
('30', '130', 'حضور در زمان احضار اضطراری', '0', '2', '4'),
('30', '140', 'عدم انجام اضافه کاری های لازمه', '-1', '-3', '-4'),
('30', '150', 'عدم حضور در زمان احضار اضطراری', '-1', '-2', '-4'),
('30', '160', 'ارزیابی مناسب و متناسب پرسنل ز', '1', '3', '5'),
('30', '170', 'عدم ارزیابی مناسب و متناسب پرس', '0', '-1', '-5'),
('40', '100', 'عدم اطاعت از دستورات مافوق', '-1', '-3', '-4'),
('40', '110', 'استعمال دخانیات در محل کار', '-1', '-2', '-4'),
('50', '100', 'عدم رعایت حسن اخلاق در برخورد ', '-1', '-3', '-4'),
('50', '110', 'عدم رعایت حسن اخلاق در برخورد ', '-1', '-2', '-5'),
('50', '120', 'عدم رعایت حسن اخلاق در برخورد ', '0', '-1', '-3'),
('50', '130', 'پاسخ مناسب به رفتار نامناسب هم', '1', '2', '3'),
('50', '140', 'نزاع با همکاران', '-1', '-3', '-4'),
('50', '150', 'عدم رعایت صداقت در گفتار ', '-1', '-2', '-4'),
('60', '100', 'حفظ و نگهداری مطلوب دستگاه های', '-1', '-2', '-5'),
('60', '101', 'عدم حفظ و نگهداری مطلوب دستگاه', '0', '-1', '-3'),
('60', '110', 'حفظ و بکارگیری مطلوب ابزار آلا', '1', '2', '5'),
('60', '111', 'عدم حفظ و بکارگیری مطلوب ابزار', '-1', '-3', '-4'),
('60', '120', 'صرفه جویی و جلوگیری از اتلاف م', '-1', '-2', '-5'),
('60', '121', 'عدم صرفه جویی و اتلاف منابع ', '0', '-1', '-3'),
('70', '100', 'آراستگی چشمگیر فردی', '1', '2', '5'),
('70', '101', 'عدم آراستگی فردی', '0', '-1', '-4'),
('70', '110', 'آراستگی محیط کار فردی', '1', '2', '3'),
('70', '110', 'عدم آراستگی محیط کار فردی', '-1', '-2', '-5'),
('70', '120', 'رعایت چشمگیر نظم و نظافت معابر', '1', '3', '4'),
('70', '121', 'عدم رعایت نظم و نظافت معابر و ', '0', '-1', '-4'),
('80', '100', 'انجام چشمگیر وظایف ', '0', '1', '3'),
('80', '101', 'عدم انجام شرح وظایف ', '0', '-2', '-4'),
('80', '110', 'رعایت چشمگیر موارد مرتبط با کی', '1', '2', '5'),
('80', '111', 'عدم رعایت موارد مرتبط با کیفیت', '-1', '-3', '-4'),
('80', '120', 'انجام اقداماتی که از بروز خسار', '-1', '-2', '-5'),
('80', '121', 'بی دقتی که منجر به بروز خسارت ', '0', '-1', '-3'),
('80', '130', 'انجام اقداماتی که از بروز خسار', '0', '1', '3'),
('80', '131', 'بی دقتی که منجر به بروز خسارت ', '-1', '-2', '-5'),
('80', '140', 'انجام اقداماتی که از بروز خسار', '1', '4', '6'),
('80', '141', 'بی دقتی که منجر به بروز خسارت ', '0', '-2', '-4'),
('80', '150', 'اجرای صحیح و بموقع دستور مافوق', '1', '2', '3'),
('80', '151', 'عدم اجرای صحیح و بموقع دستور م', '0', '-1', '-4'),
('80', '160', 'اطلاع رسانی صحیح و بموقع که مو', '1', '2', '5'),
('80', '161', 'دادن اطلاعات ناصحیح که موجب تص', '-1', '-2', '-5'),
('', '170', '', '', '', ''),
('', '', '', '', '', ''),
('', '', '', '', '', ''),
('', '', '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `overheads`
--

CREATE TABLE `overheads` (
  `pID` int(10) NOT NULL,
  `overheadLevel` int(10) NOT NULL,
  `overheadID` int(10) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

--
-- Dumping data for table `overheads`
--

INSERT INTO `overheads` (`pID`, `overheadLevel`, `overheadID`) VALUES
(380101, 1, 380550),
(380101, 2, 380650),
(380101, 3, 380900),
(380220, 1, 380500),
(380220, 2, 380600),
(380220, 3, 380900),
(380230, 1, 380500),
(380230, 2, 380600),
(380230, 3, 380900),
(380235, 1, 380550),
(380235, 2, 380650),
(380235, 3, 380900),
(380400, 1, 380420),
(380400, 2, 380430);

-- --------------------------------------------------------

--
-- Table structure for table `personnel`
--

CREATE TABLE `personnel` (
  `Name` varchar(20) COLLATE utf8_persian_ci DEFAULT NULL COMMENT 'نام',
  `Family` varchar(30) COLLATE utf8_persian_ci DEFAULT NULL COMMENT 'فامیل',
  `pID` int(10) NOT NULL COMMENT 'کد پرسنلی'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

--
-- Dumping data for table `personnel`
--

INSERT INTO `personnel` (`Name`, `Family`, `pID`) VALUES
('رضا', 'رضایی', 380101),
('حسین', 'حسینی', 380220),
('چمشید', 'جمشیدی', 380230),
('اسد ', 'اسدی', 380235),
('جواد', 'جوادی', 380400),
('امیر', 'امیری', 380420),
('ضیا', 'ضیائی', 380500),
('رمضان', 'رمضانی', 380550),
('مستاجر', 'مستاجرانی', 380600),
('معلم', 'معلمی', 380650),
('ملکوت', 'ملکوتی', 380900);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `personnel`
--
ALTER TABLE `personnel`
  ADD UNIQUE KEY `pID` (`pID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
