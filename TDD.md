# Technical Design Document

## Library Management System

### 1. Architectural Overview

#### 1.1 High-level Architecture

The library management system will follow a layered architecture within a monolithic FastAPI application.

```mermaid
┌─────────────────────────────────────────────────────────┐
│                   Weather Forecast Service              │
│                                                         │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐    │
│  │  Web Layer  │   │Service Layer│   │  Data Layer │    │
│  │(Frontend   /│<─>│  (Services) │<─>│(Repos)      │    │
│  │  program )  │   │             │   │             │    │
│  └─────────────┘   └─────────────┘   └─────────────┘    │
│          ▲                 ▲                ▲           │
│          │                 │                │           │
└──────────┼─────────────────┼────────────────┼───────────┘
           │                 │                │
           ▼                 │                ▼
┌─────────────────┐          │         ┌──────────────────┐
│    Web Browser  │          │         │    Database      │
└─────────────────┘          │         └──────────────────┘
                             ▼
                    ┌──────────────────┐
                    │ RESTful API      │
                    │ graphQL API      │
                    └──────────────────┘
```

#### 1.2 Design Principles

- **Seperation of Concerns**: Clear sepaeration between the UI, application logic and data access.
- **Single Responsibility**: Each component and logic handle a single task.
- **DRY principle**: Reusable non-repeating components
- **Fail Gracefully**: Handle errors and API failures efficiently.

### 2. Technology Stack

#### 2.1 Backend

- **Programming Language**: Python 3.13
- **Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Database**: MySQL
- **API client**:
- **Caching**: Redis cache
- **Testing**:
- **Logging**:

#### 2.2 Frontend

- **CSS Framework**: Bootstrap  or Tailwind CSS for styling
- **JavaScript**: Minimal vanilla JavaScript for interactivity

### 3. Data Model

#### 3.1 Entity Relationship Diagram

```mermaid

┌─────────────┐     ┌────────────────┐      ┌────────────────────┐
│   User      |     |      Books     |      |     History        |  
├─────────────┤     ├────────────────┤      ├────────────────────┤
| id          |     | id             |      | id                 |
| username    |     | title          |      | event              |
| password    |     | author         |      | sentBy             | 
| role        |     | available      |      | receivedBy         |
| createdAt   |     | genre          |      | createdAt          |
| lastLogin   |     | create         |      └────────────────────┘
└─────────────┘     | createdAt      |
                    | lastUpdated    |
                    └────────────────┘

```

#### 3.2 Detailed Entity Description

1. **User**:

    - This entity represents who is making use of the system
    - The user is role-based with two distinctive roles, the base users and the admin (librarian)
    - With proper authentication and authorization set up, the base users should not have the same privileges as the admin.
    - Actions that can be performed by an admin:
        a. Perform CRUD operations on books.
        b. View borrowed books and who borrowed it.
        c. Track the due-dates of borrowed books.
        d. Generate a PDF/CSV report on books
        e. Adjust the due date of a book.
    - Actions that can be performed by a base user:
        a. View books available in the library.
        b. Borrow a book.
        c. Track due dates of borrowed books.
    - One-to-Many relationship with the books entity. i.e One user can borrow more than one books.

2. **Books**:

    - THis is the primary entity representing the books of the library.
    - One-to-One relationship with the User entity.

3. **History**:

    - This entity stores the various events taking place in the system.
    - The admin can generate a report on the history.
