-- Optional: psql "$DATABASE_URL" -f data/demo_seed.sql
-- Gives DataAgent a tiny read-only table to query in demos.

CREATE TABLE IF NOT EXISTS course_demo_facts (
    id SERIAL PRIMARY KEY,
    topic TEXT NOT NULL,
    detail TEXT NOT NULL
);

INSERT INTO course_demo_facts (topic, detail)
SELECT 'Course code', 'ISYS 398U — Agentic AI Implementation'
WHERE NOT EXISTS (SELECT 1 FROM course_demo_facts WHERE topic = 'Course code');

INSERT INTO course_demo_facts (topic, detail)
SELECT 'Voice stack', 'This demo uses OpenAI Realtime over WebSockets with the Agents SDK.'
WHERE NOT EXISTS (SELECT 1 FROM course_demo_facts WHERE topic = 'Voice stack');

INSERT INTO course_demo_facts (topic, detail)
SELECT 'MCP', 'The DataAgent uses @modelcontextprotocol/server-postgres in read-only mode.'
WHERE NOT EXISTS (SELECT 1 FROM course_demo_facts WHERE topic = 'MCP');
