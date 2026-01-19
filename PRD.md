# Project requirements documents

## Library Management System (LMS)

### 1. Project Overview

The libraty management system is a program that helps to automate a library workflow.

### 2. Users Stories

1. As a user, I want to be able to search for a book.
2. As a user, I want to be able to borrow books through the program.
3. As a user, I want to be able to see the current status of a book.
4. As a librarian, I want to be able to track the dates on borrowed books.
5. As a librarian, I want to be able to generate reports on popular books (probably most borrowed, highest review, etc), borrowed books and inventory.

### 3. Functional Requirements

#### 3.1 Authentication and Authorization

- This is a role-based system.
- A user should not have the same role as a librarian, for example, adding a book, removing a book, adjusting the due date of a book, etc.

#### 3.2 Search and filtering capabilities

- Implementation of search function and a filteration system based on title, author, genre, availability of book.

#### 3.3 Handle borrowing logic

- Implement a logic to streamline borrowing and returning of books.
- The logic should be able to tell when a borrowed book has not been returned before its due date.
- When a book is borrowed, it becomes unavailable or the quantity is reduced.

#### 3.4 Generate reports

- Admin should be able to generate a report on popular books, overdue (borrowed books past its due date) list
- Admin should be able to generate reports on inventory status
- Generated reports should have the option of being exported to CSVs / PDFs.

### 4. Non-Functional Requirements

#### 4.1 Speed

- Response should be returned with a load time < 3 seconds.

#### 4.2 Reliability

- Available books should not be shown as unavailable and vice versa.
- Authentication and authorization should be properly handled.

#### 4.3 Scalability

- System should be designed to handle an increasing number of books and users.
