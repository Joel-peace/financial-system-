# Personal Finance Tracker CLI

## Features
- Create financial profiles
- Track retirement savings
- Manage life insurance policies
- Preloaded demo data
- Interactive debugging

## How to Run
```bash
source venv/bin/activate
python -m finance_tracker.cli.main#!/bin/bash

# 1. Create project structure
mkdir -p finance_tracker/{cli,models,helpers} tests && \
touch finance_tracker/__init__.py && \
touch finance_tracker/cli/{__init__.py,main.py} && \
touch finance_tracker/models/{__init__.py,base.py,profile.py,retirement.py,life.py} && \
touch finance_tracker/helpers/{__init__.py,seed.py} && \
touch tests/{__init__.py,test_models.py} && \
touch README.md requirements.txt

# 2. Create virtual environment
python -m venv venv && \
source venv/bin/activate && \
pip install --upgrade pip && \
pip install sqlalchemy pytest ipdb

# 3. Write base model
cat > finance_tracker/models/base.py << 'EOL'
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///finance.db')
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    Base.metadata.create_all(engine)
    print("Database initialized!")
