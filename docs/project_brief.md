# AI Interview Platform – Project Brief

## 1. Project Overview

AI Interview Platform is a web application that helps software engineers prepare for technical interviews through AI-generated interview sessions, automated answer evaluation, personalized feedback, and learning recommendations.

The platform simulates real technical interviews and identifies knowledge gaps by analyzing user responses.

The long-term goal is to create a personal AI interviewer that can conduct, evaluate, and improve interview performance for software engineers.

---

# 2. Problem Statement

Many developers struggle to prepare effectively for technical interviews because:

* They do not know which topics are important.
* They lack realistic interview practice.
* They receive no objective feedback on their answers.
* They cannot easily identify knowledge gaps.
* Mock interviews with real people are expensive or difficult to schedule.

Current interview preparation methods are often passive (reading articles, watching videos, solving tasks) and provide little insight into communication quality and interview readiness.

The platform solves this by providing realistic, personalized, and repeatable interview simulations.

---

# 3. Target Users

Primary Users:

* Junior Backend Developers
* Junior Full Stack Developers
* Computer Science Students
* Career Changers entering Software Engineering

Secondary Users:

* Mid-Level Engineers preparing for job changes
* Developers preparing for FAANG-style interviews
* Recruiters or mentors conducting mock interviews

---

# 4. MVP Scope

The MVP should focus on validating the core idea before introducing advanced infrastructure.

## Authentication

* User registration
* User login
* JWT authentication
* Refresh tokens

## Profile Management

Users can specify:

* Target role
* Experience level
* Preferred technology stack

Example:

* Python Backend
* Junior
* FastAPI + PostgreSQL

## Interview Generation

Generate interview sessions based on:

* Role
* Difficulty
* Technology stack

Example:

"Generate 10 Junior Python Backend questions."

## Question Management

Store generated questions in the database.

Users can:

* Start interview
* View questions
* Submit answers

## AI Evaluation

AI evaluates each answer and provides:

* Score
* Strengths
* Weaknesses
* Suggested improvements

## Interview History

Users can:

* View previous interviews
* Compare results
* Track progress

---

# 5. Non-MVP Features

These features will be implemented after the MVP.

## Redis Caching

Cache generated questions and AI responses.

## RabbitMQ

Asynchronous interview processing.

## Background Workers

Process AI evaluations outside API requests.

## WebSockets

Real-time status updates.

Examples:

* Interview processing
* Evaluation completed
* New feedback available

## Voice Interviews

Users submit audio answers.

Pipeline:

Audio → Speech-to-Text → AI Evaluation

## AWS Deployment

Production cloud deployment.

## GraphQL API

Alternative API interface.

## Learning Roadmaps

Generate personalized study plans.

## Analytics Dashboard

Track:

* Average score
* Topic weaknesses
* Improvement trends

## Interview Scheduling

Recurring interview practice sessions.

---

# 6. Tech Stack

## FastAPI

Purpose:

Backend API framework.

Reasons:

* Modern Python ecosystem
* Async support
* Automatic OpenAPI documentation
* Strong typing support

---

## PostgreSQL

Purpose:

Primary database.

Reasons:

* Relational data fits interview entities well
* Industry standard
* Excellent performance and reliability

---

## SQLAlchemy (Async)

Purpose:

ORM layer.

Reasons:

* Async support
* Industry adoption
* Flexible query construction

---

## Alembic

Purpose:

Database migrations.

Reasons:

* Schema version control
* Safe database evolution

---

## Docker

Purpose:

Containerization.

Reasons:

* Reproducible environments
* Easier deployment
* Consistent local development

---

## OpenAI API

Purpose:

Question generation and answer evaluation.

Reasons:

* Natural language understanding
* Detailed feedback generation

---

## Redis (Future)

Purpose:

Caching and rate limiting.

Reasons:

* Fast in-memory storage
* Reduced AI costs
* Improved response times

---

## RabbitMQ (Future)

Purpose:

Message queue.

Reasons:

* Asynchronous processing
* Decoupled architecture
* Better scalability

---

## AWS (Future)

Services:

* EC2
* RDS
* S3

Reasons:

* Cloud deployment experience
* Production infrastructure skills

---

# 7. Main User Flow

Step 1

User registers.

↓

Step 2

User completes profile.

↓

Step 3

User creates interview session.

↓

Step 4

AI generates interview questions.

↓

Step 5

Questions are stored in database.

↓

Step 6

User answers questions.

↓

Step 7

Answers are submitted.

↓

Step 8

AI evaluates answers.

↓

Step 9

Results are saved.

↓

Step 10

User reviews feedback and improvement suggestions.

↓

Step 11

User starts another interview and tracks progress over time.

---

# 8. Initial Database Entities

## User

Stores platform users.

Fields:

* id
* email
* password_hash
* target_role
* experience_level
* created_at

---

## Interview

Represents one interview session.

Fields:

* id
* user_id
* role
* difficulty
* status
* created_at

Relationship:

User → Many Interviews

---

## Question

Stores generated interview questions.

Fields:

* id
* interview_id
* question_text
* topic
* difficulty

Relationship:

Interview → Many Questions

---

## Answer

Stores user responses.

Fields:

* id
* question_id
* answer_text
* submitted_at

Relationship:

Question → One Answer

---

## Evaluation

Stores AI-generated feedback.

Fields:

* id
* answer_id
* score
* strengths
* weaknesses
* recommendations
* created_at

Relationship:

Answer → One Evaluation

---

# 9. Future Architecture Vision

MVP:

FastAPI → PostgreSQL → OpenAI

Version 2:

FastAPI → RabbitMQ → Workers → OpenAI → PostgreSQL

Version 3:

FastAPI → RabbitMQ → Workers → Redis → PostgreSQL → AWS

The project evolves from a monolithic architecture into a production-style distributed backend system while maintaining a clean and incremental learning path.
