# AI Language Learning & Diagnostic Platform

An AI-assisted English learning platform for intermediate and advanced learners (B1-C2), including IELTS candidates. It identifies recurring weaknesses, guides targeted practice, and verifies improvement on unfamiliar material over time.

## Reading First

The first release starts with curated or AI-generated passages and IELTS-style exercises. Objective questions use validated answer keys, and feedback explains answers using evidence from the passage. Reading attempts capture comprehension gaps and unfamiliar vocabulary for follow-up practice.

The first milestone is a complete learning cycle from practice and diagnosis to targeted exercises and reassessment on a new passage.

## How Learning Adapts

- **Personal Language Knowledge Model** tracks mastery and confidence so gaps in evidence stay visible.
- **Error Lifecycle Management** groups mistakes into recurring patterns and tracks improvement through independent practice and delayed reassessment.
- **Cross-Skill Knowledge Transfer** will carry vocabulary and grammar from Reading into Listening, Speaking, and Writing practice.

Writing, Listening, and Speaking follow after the Reading workflow is validated. Full IELTS simulations and personalized study planning are later phases.

## Development Status

The existing backend uses FastAPI, PostgreSQL, async SQLAlchemy, Alembic, Poetry, and Docker Compose. The health endpoint and authentication foundation are in place. Reading is the first planned learning module.
