# AI Interview Platform – MVP Specification v1.0

## 1. Functional Requirements

### Authentication

FR-1

A user can register using:

* email
* password

FR-2

A user cannot register with an email that already exists.

FR-3

A user can log in using valid credentials.

FR-4

A user receives JWT access and refresh tokens after successful login.

FR-5

A user can refresh an expired access token using a valid refresh token.

FR-6

Protected endpoints require authentication.

---

### User Profile

FR-7

A user can create and update a profile.

Profile fields:

* target_role
* experience_level
* preferred_stack

FR-8

A user can retrieve their profile information.

---

### Interview Creation

FR-9

A user can create a new interview.

Required fields:

* role
* difficulty

Example:

* Python Backend
* Junior

FR-10

The system generates interview questions using AI.

FR-11

Generated questions are stored in the database.

FR-12

The interview becomes available after question generation succeeds.

---

### Interview Retrieval

FR-13

A user can view all of their interviews.

FR-14

A user can view a specific interview.

FR-15

A user cannot access another user's interviews.

---

### Questions

FR-16

A user can retrieve all questions for an interview.

FR-17

Questions cannot be modified after generation.

---

### Answers

FR-18

A user can submit one answer per question.

FR-19

An answer must contain text.

FR-20

Submitted answers are stored in the database.

FR-21

A user can retrieve previously submitted answers.

---

### Evaluation

FR-22

A user can request interview evaluation.

FR-23

The system sends questions and answers to the AI provider.

FR-24

The system stores evaluation results.

FR-25

Evaluation includes:

* score
* strengths
* weaknesses
* recommendations

FR-26

A user can retrieve interview evaluation results.

---

### Interview History

FR-27

A user can view previous interview sessions.

FR-28

A user can view evaluation results from previous interviews.

---

## 2. Non-Functional Requirements

### API Behavior

NFR-1

The API must return JSON responses.

NFR-2

The API must return appropriate HTTP status codes.

Examples:
fsu
* 200 OK
* 201 Created
* 400 Bad Request
* 401 Unauthorized
* 403 Forbidden
* 404 Not Found
* 422 Validation Error

---

### Validation

NFR-3

The API must validate incoming request data.

NFR-4

Invalid data must return descriptive validation errors.

Example:

Invalid email format should return a validation error.

---

### Security

NFR-5

Passwords must never be stored in plain text.

NFR-6

Passwords must be hashed before storage.

NFR-7

Authenticated users can access only their own resources.

NFR-8

JWT authentication must be required for protected endpoints.

---

### Reliability

NFR-9

Database transactions must rollback on failure.

NFR-10

The application must not crash because of invalid user input.

---

### Documentation

NFR-11

API documentation must be automatically generated using OpenAPI.

NFR-12

Swagger UI must be available.

---

### Maintainability

NFR-13

Business logic must be separated from API routes.

NFR-14

Database access must be separated into repository classes.

NFR-15

Database schema changes must be managed through Alembic migrations.

---

### Containerization

NFR-16

Application must run using Docker Compose.

NFR-17

A new developer should be able to start the application with:

docker compose up

---

## 3. Interview Statuses

An interview can exist in one of the following states.

### CREATED

Interview record exists.

Questions have not been generated yet.

---

### GENERATING_QUESTIONS

AI question generation is in progress.

---

### READY

Questions successfully generated.

User may begin answering.

---

### IN_PROGRESS

User has started submitting answers.

---

### ANSWERS_SUBMITTED

All answers have been submitted.

Interview is ready for evaluation.

---

### EVALUATING

AI evaluation is in progress.

---

### EVALUATED

Evaluation completed successfully.

Results available.

---

### FAILED

Question generation or evaluation failed.

Manual retry may be required.

---

## Allowed Status Transitions

CREATED

↓

GENERATING_QUESTIONS

↓

READY

↓

IN_PROGRESS

↓

ANSWERS_SUBMITTED

↓

EVALUATING

↓

EVALUATED

Failure path:

GENERATING_QUESTIONS

↓

FAILED

or

EVALUATING

↓

FAILED

---

## 4. API Endpoints

### Authentication

POST /auth/register

Register a new user.

---

POST /auth/login

Authenticate user.

---

POST /auth/refresh

Refresh access token.

---

### Profile

GET /profile

Retrieve current user profile.

---

PATCH /profile

Update profile information.

---

### Interviews

POST /interviews

Create new interview.

---

GET /interviews

Retrieve all user interviews.

---

GET /interviews/{interview_id}

Retrieve interview details.

---

POST /interviews/{interview_id}/generate

Generate interview questions.

---

GET /interviews/{interview_id}/questions

Retrieve interview questions.

---

### Answers

POST /questions/{question_id}/answer

Submit answer.

---

GET /questions/{question_id}/answer

Retrieve submitted answer.

---

### Evaluation

POST /interviews/{interview_id}/evaluate

Evaluate interview.

---

GET /interviews/{interview_id}/evaluation

Retrieve evaluation results.

---

### Health Check

GET /health

Application health endpoint.

---

## 5. Out of Scope (MVP Exclusions)

The following features are intentionally excluded from MVP v1.

### Audio Interviews

Users cannot upload voice recordings.

Only text answers are supported.

---

### Speech-to-Text

No transcription functionality.

---

### Video Interviews

No camera recording.

No video uploads.

---

### WebSockets

No real-time updates.

Users will refresh manually.

---

### RabbitMQ

No message queues.

Evaluation happens synchronously.

---

### Redis

No caching.

No rate limiting.

---

### GraphQL

REST API only.

---

### AWS Deployment

Local Docker deployment only.

---

### Social Authentication

No Google login.

No GitHub login.

---

### Email Verification

Users are active immediately after registration.

---

### Password Reset

Forgot-password workflow not included.

---

### Analytics Dashboard

No advanced statistics.

---

### Interview Scheduling

No reminders or calendar integration.

---

### Multi-Language Support

English only.

---

### Admin Panel

No administrative interface.

---

### Team Accounts

Single-user accounts only.

---

### AI Follow-Up Questions

AI generates questions only once.

No dynamic interviewer behavior.

---

## MVP Success Criteria

The MVP is considered complete when:

1. Users can register and log in.
2. Users can create interviews.
3. AI can generate interview questions.
4. Users can answer questions.
5. AI can evaluate answers.
6. Results are stored in PostgreSQL.
7. All functionality runs through Docker Compose.
8. API documentation is available through Swagger.
