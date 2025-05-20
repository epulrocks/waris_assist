# Waris Assist
> Hackathon project by Team Rush 01 - consisting of Saiful, Rais, Harith and Athif - during Alibaba Cloud Malaysia AI Hackathon 2025 at Affin Tower, TRX from 17 - 18 May 2025.

**Let us assist you in your darkest hour.**

Waris Assist is a proof-of-concept AI assistant designed to guide Malaysians through complex government and legal processes following the death of someone close to you.

## Problem Statement

The loss of a loved one is already emotionally overwhelming — yet families must immediately confront a maze of bureaucratic procedures involving over 10 different government agencies, each with their own forms, requirements, and timelines.

This process can stretch across months to a full year, especially in cases involving court hearings, insurance claims, or missing documents. 

We realised that essential information was scattered across various government agency websites or SOP documents, and that most of these websites were not easy to navigate.

![Problem](<Images/Waris_problem.png>)  

## Our Solution: WarisAssist

WarisAssist is an intelligent assistant designed to ease this burden. It offers a unified experience that can:

- **Answer complex, case-specific queries** using Retrieval-Augmented Generation (RAG) from reliable sources like government portals and legal SOPs.
- **Guide users through a step-by-step process**, asking questions sequentially using natural language to gather important context from the user.
- **Track tasks and manage documents** to keep everything organized in one place.
- **Support multilingual interactions**, e.g. Bahasa Malaysia and English.
- **Provide accurate structured information**, like up-to-date contact details and office addresses for relevant government departments.

![Solution](<Images/Waris_solution.png>)  
## Demo

📺 **Watch our presentation**: [YouTube Video](<https://www.youtube.com/watch?v=aufRZzs8sug>)  
📸 **Screenshots**:  
![Screenshot of Assistant UI](<Images/Waris_UI.png>)  


## Technical Architecture

Our prototype is built on a simple stack:

- **Frontend**: [Streamlit](https://streamlit.io/) for chatbot front end coupled with a checklist side panel.
- **Backend + LLM**: [Alibaba Model Studio](https://www.alibabacloud.com/) running Qwen-Max, with RAG implemented using ingested datasets (during Hackathon period).
- **Deployment**: Hosted on an ECS instance (during Hackathon period).
- **Data**: Structured datasets (e.g., contact directories, office locations) with unstructured data (e.g., legal guides, SOPs) to generate context-aware and reliable responses.

![Technical Architecture](<Images/Waris_technical.png>)  

### Future Plans

- Extend WarisAssist to support other complex life events such as divorce, birth registration, and citizenship matters.
- Integrate with official government systems and databases.
- Improve robustness with a redesigned, scalable architecture.

## 📊 Impact Potential

- **Development cost**: RM100,000  
- **Annual maintenance**: RM40,000  
- **Expected savings for JPN**: RM300,000 annually, from a 20% reduction in public enquiries  
- **National value from time savings**: RM3 million per year  

We envision JPN (National Registration Department) as a key implementation partner, given their central role in death registration processes.

![Impact](<Images/Waris_impact.png>)  


