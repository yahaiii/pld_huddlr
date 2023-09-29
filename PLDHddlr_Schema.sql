-- Create the PLDHuddlr database
CREATE DATABASE PLDHuddlr;

-- Switch to the PLDHuddlr database
USE PLDHuddlr;

-- Create the Users table
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(255) NOT NULL,
    PasswordHash VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    ProfileImageURL VARCHAR(255),
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the Availability table
CREATE TABLE Availability (
    AvailabilityID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT NOT NULL,
    Date DATE NOT NULL,
    TimeSlots VARCHAR(255),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Create the Meetings table
CREATE TABLE Meetings (
    MeetingID INT AUTO_INCREMENT PRIMARY KEY,
    MeetingTitle VARCHAR(255),
    MeetingDescription TEXT,
    MeetingDateTime DATETIME NOT NULL,
    MeetingDuration INT,
    MeetingStatus ENUM('scheduled', 'ongoing', 'completed') DEFAULT 'scheduled',
    Attendees TEXT -- Store attendees in JSON
);

-- Create the Notifications table
CREATE TABLE Notifications (
    NotificationID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT NOT NULL,
    NotificationType ENUM('confirmation', 'reminder', 'other') DEFAULT 'confirmation',
    NotificationContent TEXT,
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    IsRead BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Create the Ratings and Feedback table
CREATE TABLE RatingsAndFeedback (
    RatingID INT AUTO_INCREMENT PRIMARY KEY,
    RatedUserID INT NOT NULL,
    RatingUserID INT NOT NULL,
    Rating INT,
    Feedback TEXT,
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (RatedUserID) REFERENCES Users(UserID),
    FOREIGN KEY (RatingUserID) REFERENCES Users(UserID)
);

-- Create the Topics table
CREATE TABLE Topics (
    TopicID INT AUTO_INCREMENT PRIMARY KEY,
    TopicName VARCHAR(255) NOT NULL
);

-- Create the User Topics (Interests) table
CREATE TABLE UserTopics (
    UserTopicID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT NOT NULL,
    TopicID INT NOT NULL,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (TopicID) REFERENCES Topics(TopicID)
);

-- Create the Analytics table
CREATE TABLE Analytics (
    AnalyticsID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT NOT NULL,
    Action VARCHAR(255),
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);
