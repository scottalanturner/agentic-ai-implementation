## What changes when documents are attached

| Mode | What the model "knows" | Risk profile |
|------|------------------------|--------------|
| **Base model** | Training cutoff + prompt | Generic, confident |
| **Prompt-only** | What you paste | Small context |
| **RAG / knowledge** | Retrieved chunks from **your** library | Better facts; new failure modes |
| **Tools + RAG** | Can fetch fresh data | Ops + security matter |
